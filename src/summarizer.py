import json
from datetime import date

import anthropic

from src.config import get_env, load_sources
from src.fetcher import Article

# Override with ANTHROPIC_MODEL if needed (default: current Sonnet)
DEFAULT_MODEL = "claude-sonnet-5"


def _build_prompt(articles: list[Article], brain: dict) -> str:
    config = load_sources()
    brands = ", ".join(config["brands"])
    today = date.today().strftime("%A, %B %d, %Y")

    articles_text = ""
    for i, a in enumerate(articles, 1):
        articles_text += f"""
--- Article {i} ---
Source: {a.source}
Title: {a.title}
URL: {a.url}
Published: {a.published.isoformat()}
Summary: {a.summary}
"""

    # Brain for dedup: topic titles + existing action items only
    brain_for_prompt = [
        {
            "id": t.get("id"),
            "title": t.get("title"),
            "action_items": t.get("action_items") or t.get("bullets") or [],
        }
        for t in brain.get("topics", [])[:100]
    ]
    brain_summary = json.dumps(brain_for_prompt, indent=2)

    return f"""You are an expert SEO analyst preparing a skimmable weekday morning briefing for Brandon, who manages SEO for these rental/property management brands: {brands}.

Today is {today}.

## Your task

1. Read the EXISTING BRAIN — past topics and action items we've already captured.
2. Read today's NEW ARTICLES from tracked feeds (last 24 hours, diversified across sources).
3. Consolidate into distinct TOPICS (not one card per article — group related coverage).
4. Skip only pure fluff / product ads with no SEO insight. Prefer completeness: if something is useful research, a Google change, AI-search finding, or a testable idea, include it.
5. If a topic already exists in the brain, treat it as an UPDATE and only add net-new action items.
6. Cite the best primary source URL for each topic (prefer Google/official docs when available).

## Topic title rules
Use short, sortable labels like:
- "Schema"
- "AI Citations"
- "Google Algorithm Update"
- "AI Overviews"
- "Local SEO / GBP"
- "GSC Reporting"
- "Structured Data — Video"
NOT long article headlines.

## Action item rules
- High-level projects, audits, or concepts to test
- Do NOT name specific brand domains (no turbotenant.com, etc.)
- Keep each action item to one concise sentence
- 1–3 action items per topic for today's email; brain updates can reuse those same items

## Response format

Return ONLY valid JSON:
{{
  "todays_insights": [
    {{
      "type": "new" | "update",
      "topic": "Short Topic Title",
      "summary": "1-2 sentence summary of what changed or was learned.",
      "action_items": [
        "High-level project, audit, or test idea",
        "Another action item if useful"
      ],
      "source": "Source name",
      "url": "https://article-url"
    }}
  ],
  "brain_updates": {{
    "topics": [
      {{
        "id": "kebab-case-slug-matching-topic",
        "title": "Same Short Topic Title",
        "action_items": [
          "Only net-new action items to append to the brain for this topic"
        ]
      }}
    ]
  }},
  "no_news_summary": "If nothing worth reporting, a brief note explaining why."
}}

Be comprehensive: include every distinct actionable topic worth capturing (often 8–25 on a busy day). Do not aggressively truncate to a short "top N" list — missing useful analysis is worse than a longer email. Prefer breadth across sources when quality is equal.

## EXISTING BRAIN
{brain_summary if brain_summary.strip() != "[]" else "Empty — this is the first run."}

## NEW ARTICLES
{articles_text if articles_text.strip() else "No new articles found."}
"""


def generate_briefing(articles: list[Article], brain: dict) -> dict:
    if not articles:
        return {
            "todays_insights": [],
            "brain_updates": {"topics": []},
            "no_news_summary": "No new articles were published in the last 24 hours across your tracked feeds.",
        }

    client_kwargs = {"api_key": get_env("ANTHROPIC_API_KEY")}
    workspace_id = get_env("ANTHROPIC_WORKSPACE_ID", "")
    if workspace_id:
        client_kwargs["default_headers"] = {"anthropic-workspace-id": workspace_id}

    client = anthropic.Anthropic(**client_kwargs)
    model = get_env("ANTHROPIC_MODEL", DEFAULT_MODEL)
    prompt = _build_prompt(articles, brain)

    try:
        response = client.messages.create(
            model=model,
            max_tokens=16000,
            thinking={"type": "disabled"},
            messages=[{"role": "user", "content": prompt}],
        )
    except anthropic.NotFoundError as exc:
        raise RuntimeError(
            f"Anthropic model not found: {model}. "
            "Set ANTHROPIC_MODEL to a valid model ID (e.g. claude-sonnet-5)."
        ) from exc
    except anthropic.BadRequestError as exc:
        message = str(exc).lower()
        if "credit balance" in message:
            raise RuntimeError(
                "Anthropic API credit balance is too low. "
                "Add credits at https://console.anthropic.com/settings/billing"
            ) from exc
        if "workspace" in message:
            raise RuntimeError(
                "This Anthropic API key requires a workspace ID. "
                "Add GitHub secret ANTHROPIC_WORKSPACE_ID (looks like wrkspc_...), "
                "or create a workspace-scoped key in the Anthropic console."
            ) from exc
        raise

    raw = _extract_text(response).strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()

    return json.loads(raw)


def _extract_text(response) -> str:
    """Pull the assistant text from a Messages response (skip thinking blocks)."""
    parts = []
    for block in response.content:
        if getattr(block, "type", None) == "text":
            parts.append(block.text)
    if not parts:
        raise RuntimeError("Claude returned no text content in the response.")
    return "\n".join(parts)
