from datetime import date
from html import escape

import httpx

from src.config import get_env, load_sources


def _build_html(briefing: dict, brain: dict) -> str:
    config = load_sources()
    today = date.today().strftime("%A, %B %d, %Y")
    insights = briefing.get("todays_insights", [])
    topics = sorted(brain.get("topics", []), key=lambda t: (t.get("title") or "").lower())

    html = f"""
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 680px; margin: 0 auto; color: #1a1a1a; font-size: 14px; line-height: 1.45;">
      <h1 style="font-size: 20px; border-bottom: 2px solid #2563eb; padding-bottom: 8px; margin-bottom: 8px;">
        SEO Morning Brief — {today}
      </h1>
    """

    if insights:
        html += f'<p style="color:#666; margin: 0 0 16px;">{len(insights)} topics</p>'
        html += '<ol style="padding-left: 22px; margin: 0;">'
        for item in insights:
            topic = escape(item.get("topic") or item.get("headline") or "Topic")
            summary = escape(item.get("summary") or item.get("detail") or "")
            source = escape(item.get("source", "Unknown"))
            url = escape(item.get("url", "#"), quote=True)
            brainworthy = item.get("brainworthy", True)
            badge = "ACTION" if brainworthy else "FYI"
            badge_color = "#16a34a" if brainworthy else "#6b7280"
            action_items = item.get("action_items") or []
            if not action_items and item.get("detail"):
                action_items = [item["detail"]]

            if action_items:
                actions_html = "<ul style='margin: 4px 0 0; padding-left: 18px;'>"
                for action in action_items:
                    actions_html += f"<li style='margin: 2px 0;'>{escape(action)}</li>"
                actions_html += "</ul>"
            else:
                actions_html = " <em>None — awareness only</em>"

            html += f"""
            <li style="border: 2px solid #000; padding: 12px 14px; margin: 0 0 12px;">
              <strong style="display: block; margin-bottom: 6px;">
                <span style="font-size: 10px; font-weight: 700; letter-spacing: 0.04em; color: {badge_color}; margin-right: 8px;">{badge}</span>
                {topic}
              </strong>
              <ul style="margin: 0; padding-left: 18px; list-style-type: disc;">
                <li style="margin: 2px 0;"><strong>Summary:</strong> {summary}</li>
                <li style="margin: 2px 0;">
                  <strong>Action Items:</strong>{actions_html}
                </li>
                <li style="margin: 2px 0;">
                  <strong>Source:</strong>
                  <a href="{url}" style="color: #2563eb;">{source}</a>
                </li>
              </ul>
            </li>
            """        html += "</ol>"
    else:
        summary = escape(
            briefing.get(
                "no_news_summary",
                "Quiet news day — no significant SEO updates in your feeds.",
            )
        )
        html += f'<p style="color: #666; margin-top: 16px;">{summary}</p>'

    if topics:
        html += '<h2 style="font-size: 16px; color: #2563eb; margin-top: 28px; margin-bottom: 4px;">Running Brain</h2>'
        html += '<p style="font-size: 13px; color: #666; margin-top: 0;">Condensed action playbook — revised each run (not a chronicle).</p>'
        html += '<ol style="padding-left: 22px; margin: 0;">'
        for topic in topics:
            title = escape(topic.get("title") or topic.get("id") or "Topic")
            items = topic.get("action_items") or topic.get("bullets") or []
            html += f'<li style="margin: 0 0 14px;"><strong>{title}</strong>'
            if items:
                html += '<ul style="margin: 4px 0 0; padding-left: 18px;">'
                for item in items:
                    html += f'<li style="margin: 2px 0;">{escape(item)}</li>'
                html += "</ul>"
            else:
                html += '<div style="color:#888; font-size:13px;">(no action items yet)</div>'
            html += "</li>"
        html += "</ol>"

    brands = ", ".join(config["brands"])
    html += f"""
      <hr style="margin: 28px 0; border: none; border-top: 1px solid #e5e5e5;">
      <p style="font-size: 12px; color: #999;">
        Tracking {len(config["rss_feeds"])} RSS feeds · Brands: {escape(brands)}.
        <br>Manage sources in <code>config/sources.yaml</code> on GitHub.
      </p>
    </div>
    """
    return html


def send_briefing(briefing: dict, brain: dict) -> None:
    config = load_sources()
    today = date.today().strftime("%A, %B %d, %Y")
    insights = briefing.get("todays_insights", [])
    subject = f"SEO Morning Brief — {today}"
    if insights:
        subject += f" ({len(insights)} topics)"

    email_to = get_env("EMAIL_TO", config["delivery"]["email"])
    email_from = get_env("RESEND_FROM", "onboarding@resend.dev")
    api_key = get_env("RESEND_API_KEY")

    html = _build_html(briefing, brain)

    response = httpx.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "from": email_from,
            "to": [email_to],
            "subject": subject,
            "html": html,
        },
        timeout=30,
    )

    if response.status_code >= 400:
        raise RuntimeError(f"Resend API error ({response.status_code}): {response.text}")

    print(f"  Email sent to {email_to}")
