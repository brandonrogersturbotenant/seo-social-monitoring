from datetime import date

import httpx

from src.config import get_env, load_sources


def _build_html(briefing: dict, brain: dict) -> str:
    config = load_sources()
    today = date.today().strftime("%A, %B %d, %Y")
    insights = briefing.get("todays_insights", [])
    topics = brain.get("topics", [])

    html = f"""
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 680px; margin: 0 auto; color: #1a1a1a;">
      <h1 style="font-size: 22px; border-bottom: 2px solid #2563eb; padding-bottom: 8px;">
        SEO Morning Brief — {today}
      </h1>
    """

    if insights:
        html += f'<h2 style="font-size: 16px; color: #2563eb; margin-top: 24px;">Today\'s Actionable Insights ({len(insights)})</h2>'
        for item in insights:
            badge = "UPDATE" if item.get("type") == "update" else "NEW"
            badge_color = "#d97706" if badge == "UPDATE" else "#16a34a"
            brands = item.get("relevant_brands", [])
            brand_text = f'<br><em style="color:#666;">Relevant to: {", ".join(brands)}</em>' if brands else ""

            html += f"""
            <div style="margin: 16px 0; padding: 12px 16px; background: #f8fafc; border-left: 3px solid {badge_color}; border-radius: 4px;">
              <span style="font-size: 11px; font-weight: 600; color: {badge_color};">{badge}</span>
              <strong style="display: block; margin-top: 4px;">{item["headline"]}</strong>
              <p style="margin: 6px 0 0; font-size: 14px; line-height: 1.5;">{item["detail"]}</p>
              {brand_text}
              <p style="margin: 8px 0 0; font-size: 12px; color: #888;">
                Source: <a href="{item.get("url", "#")}" style="color: #2563eb;">{item.get("source", "Unknown")}</a>
              </p>
            </div>
            """
    else:
        summary = briefing.get("no_news_summary", "Quiet news day — no significant SEO updates in your feeds.")
        html += f'<p style="font-size: 14px; color: #666; margin-top: 16px;">{summary}</p>'

    # Brain section
    recent_topics = topics[:15]
    if recent_topics:
        html += '<h2 style="font-size: 16px; color: #2563eb; margin-top: 32px;">Running Brain (Recently Updated)</h2>'
        html += '<p style="font-size: 13px; color: #666;">Accumulated learnings from past briefings.</p>'
        for topic in recent_topics:
            bullet_count = len(topic.get("bullets", []))
            last = topic.get("last_updated", "unknown")
            latest_bullet = topic["bullets"][-1] if topic.get("bullets") else ""
            html += f"""
            <div style="margin: 12px 0; padding: 10px 14px; background: #fafafa; border-radius: 4px;">
              <strong style="font-size: 14px;">{topic["title"]}</strong>
              <span style="font-size: 12px; color: #888;"> — {bullet_count} bullet{"s" if bullet_count != 1 else ""}, updated {last}</span>
              <p style="margin: 4px 0 0; font-size: 13px; color: #444;">{latest_bullet}</p>
            </div>
            """

    brands = ", ".join(config["brands"])
    html += f"""
      <hr style="margin: 32px 0; border: none; border-top: 1px solid #e5e5e5;">
      <p style="font-size: 12px; color: #999;">
        Tracking {len(config["rss_feeds"])} RSS feeds for {brands}.
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
        subject += f" ({len(insights)} insights)"

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
