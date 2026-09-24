import json
from datetime import date

import anthropic

from src.config import get_env, load_sources
from src.fetcher import Article

# Override with ANTHROPIC_MODEL if needed (default: current Sonnet)
DEFAULT_MODEL = "claude-sonnet-5"
MAX_BRAIN_ITEMS_PER_TOPIC = 5


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

    brain_for_prompt = [
        {
            "id": t.get("id"),
            "title": t.get("title"),
            "action_items": t.get("action_items") or t.get("bullets") or [],
        }
        for t in brain.get("topics", [])
    ]
    brain_summary = json.dumps(brain_for_prompt, indent=2)

    return f"""You are an expert SEO analyst preparing a skimmable weekday morning briefing for Brandon, who manages SEO for these rental/property management brands: {brands}.

Today is {today}.

## Your tasks

### A) Today's briefing (top of email)
1. Read EXISTING BRAIN and NEW ARTICLES.
2. Consolidate into distinct TOPICS (group related coverage; not one card per article).
3. Skip only pure fluff / product ads with no SEO insight. Prefer completeness.
4. Cite the best primary source URL per topic (prefer Google/official docs when available).
5. Mark each topic with brainworthy true/false (see rules below).

Include BOTH:
- Actionable work we can do on brand websites (schema, content, CWV, local/GBP, internal linking, AI citation strategy, measurement, crawler policy, etc.)
- Interesting "cool new feature" / industry FYI items worth knowing today

### B) Revised Running Brain (bottom of email) — ACTIONABLE ONLY
The brain is a durable playbook of things we can act on across our brand websites.
It is NOT a dumping ground for every interesting Google feature.

Every run, return a COMPLETE revised brain covering:
- All existing brain topics that are still website-actionable (rewritten condensed), PLUS
- Any NEW topics from today where brainworthy=true

Do NOT add cool-new-feature / FYI-only items to the brain.
If an existing brain topic is no longer actionable (pure product announcement with nothing to do on our sites), drop it.

Brain style rules:
- 2–5 punchy, action-oriented bullets per topic (REPLACES the prior list for that topic).
- When new info arrives about an existing idea, UPDATE that bullet in place — do not append another historical note.
- Drop redundant bullets; merge overlapping ones.
- Do NOT start bullets with dates like "Sep 2026:" or "Sep 2026 (24th):".
- Do NOT name specific brand domains.
- Style example (good):
  - "Hold off on blocking AI bots (GPTBot, ClaudeBot, etc.): Popular AI referral metrics are inaccurate. Wait for first-party log data before restricting access."
  - "Verify CDN & search engine settings directly: Cloudflare manages bots by broad category rather than individually. Plus, settings like Disallow AI Training exempt Googlebot and won't affect Bing until early 2027."
  - "Manage publisher models separately: Google's AI Contribution Pilot, Cloudflare's pay-per-crawl, and Microsoft's framework are incompatible — a decision for one won't apply to the others."
- Style example (bad): long "Sep 2026 (18th): Source says..." chronicle entries.

### brainworthy rules
Set brainworthy=true when the topic implies durable work on our sites, e.g.:
- audits, tests, content/structure changes, schema, CWV, local/GBP ops, measurement/KPI changes, crawler/CDN policy, citation/AEO strategy

Set brainworthy=false when it's mainly awareness / a cool feature with nothing clear to implement yet, e.g.:
- UI experiments we can't control, conference announcements, vendor product launches, speculative features with no site action

FYI items still appear in todays_insights — they just must NOT appear in brain_updates.

## Topic title rules (today + brain)
Short sortable labels: "Schema", "AI Citations", "Google Algorithm Update", "AI Overviews", "Local SEO / GBP", "GSC Reporting", "AI Crawler Access".
NOT long article headlines.

## Today's action item rules
- High-level projects, audits, or concepts to test (or "None — FYI only" style empty list for pure awareness items)
- No brand domain names
- 1–3 concise action items per topic when brainworthy; optional/empty for FYI

## Response format

Return ONLY valid JSON:
{{
  "todays_insights": [
    {{
      "type": "new" | "update",
      "topic": "Short Topic Title",
      "summary": "1-2 sentence summary of what changed or was learned.",
      "action_items": ["...", "..."],
      "source": "Source name",
      "url": "https://article-url",
      "brainworthy": true
    }}
  ],
  "brain_updates": {{
    "topics": [
      {{
        "id": "kebab-case-slug",
        "title": "Short Topic Title",
        "action_items": [
          "Complete revised condensed bullets for this topic (2-5 max) — this REPLACES the prior list"
        ]
      }}
    ]
  }},
  "no_news_summary": "If nothing worth reporting today, a brief note."
}}

Be comprehensive on today's insights (often 8–25 topics on a busy day). Prefer breadth across sources when quality is equal.
brain_updates.topics must include every KEPT existing actionable brain topic (rewritten) plus new brainworthy topics only.

## EXISTING BRAIN
{brain_summary if brain_summary.strip() != "[]" else "Empty — this is the first run."}

## NEW ARTICLES
{articles_text if articles_text.strip() else "No new articles found — still revise/condense the existing brain (actionable topics only)."}
"""


def generate_briefing(articles: list[Article], brain: dict) -> dict:
    # Always call Claude so the brain can be revised/condensed every run,
    # even on quiet news days.
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
