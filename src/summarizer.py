import json
from datetime import date

import anthropic

from src.config import get_env, load_sources
from src.fetcher import Article

# Override with ANTHROPIC_MODEL if needed (default: current Sonnet)
DEFAULT_MODEL = "claude-sonnet-5"
MAX_ARTICLES_PER_RUN = 20


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

    brain_summary = json.dumps(brain.get("topics", [])[:30], indent=2)

    return f"""You are an expert SEO analyst preparing a weekday morning briefing for Brandon, who manages SEO for these rental/property management brands: {brands}.

Today is {today}.

## Your task

1. Read the EXISTING BRAIN below — these are past learnings we've already captured.
2. Read today's NEW ARTICLES from the last 24 hours.
3. For each article, determine if it contains genuinely new SEO knowledge, or if it updates/extends something already in the brain.
4. Produce actionable insights — not just summaries. Tell Brandon what to DO or TEST on his sites when relevant.

## Rules
- Skip fluff, product announcements with no SEO insight, and duplicate coverage of the same news.
- If a topic is already in the brain but has a new angle, data point, or case study, mark it as an UPDATE and append to that topic.
- Tie insights to specific brands when there's a clear connection (e.g., local SEO → turbotenant.com, YMYL content → ipropertymanagement.com).
- Keep today's insights to the most valuable 3-8 bullets. Quality over quantity.
- Write for a senior SEO practitioner — be specific and technical when warranted.

## EXISTING BRAIN (topics already captured)
{brain_summary if brain_summary.strip() != "[]" else "Empty — this is the first run."}

## NEW ARTICLES (last 24 hours)
{articles_text if articles_text.strip() else "No new articles found."}

## Response format

Return ONLY valid JSON with this structure:
{{
  "todays_insights": [
    {{
      "type": "new" | "update",
      "headline": "Short actionable headline",
      "detail": "1-2 sentences with the insight and suggested action",
      "source": "Source name",
      "url": "Article URL",
      "relevant_brands": ["turbotenant.com"]
    }}
  ],
  "brain_updates": {{
    "topics": [
      {{
        "id": "kebab-case-slug",
        "title": "Topic title",
        "bullets": ["Bullet with date prefix like 'Sep 2026: ...'"],
        "sources": ["Source name"],
        "relevance_to_brands": ["turbotenant.com"]
      }}
    ]
  }},
  "no_news_summary": "If nothing worth reporting, a brief note explaining why (e.g., quiet news day)."
}}"""


def generate_briefing(articles: list[Article], brain: dict) -> dict:
    if not articles:
        return {
            "todays_insights": [],
            "brain_updates": {"topics": []},
            "no_news_summary": "No new articles were published in the last 24 hours across your tracked feeds.",
        }

    if len(articles) > MAX_ARTICLES_PER_RUN:
        print(f"   Limiting to {MAX_ARTICLES_PER_RUN} most recent articles (of {len(articles)})")
        articles = articles[:MAX_ARTICLES_PER_RUN]

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
            max_tokens=4096,
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

    raw = response.content[0].text.strip()
    # Handle markdown code fences if Claude wraps JSON
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()

    return json.loads(raw)
