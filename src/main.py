"""SEO Morning Brief — daily RSS monitoring pipeline."""

import sys

from src.brain import (
    apply_brain_updates,
    filter_unprocessed,
    load_brain,
    mark_processed,
    save_brain,
)
from src.emailer import send_briefing
from src.fetcher import fetch_recent_articles
from src.summarizer import generate_briefing


def run() -> None:
    print("SEO Morning Brief — starting run\n")

    # 1. Fetch articles from last 24 hours
    print("1. Fetching RSS feeds (last 24h)...")
    articles = fetch_recent_articles(hours=24)
    print(f"   Found {len(articles)} articles across all feeds")

    # 2. Load brain and filter already-processed
    brain = load_brain()
    new_articles = filter_unprocessed(articles, brain)
    print(f"   {len(new_articles)} are new (not previously processed)")

    # 3. Generate briefing with Claude (processes up to 20 articles per run)
    print("\n2. Generating briefing with Claude...")
    from src.summarizer import MAX_ARTICLES_PER_RUN

    articles_to_process = new_articles[:MAX_ARTICLES_PER_RUN]
    briefing = generate_briefing(articles_to_process, brain)
    insights = briefing.get("todays_insights", [])
    print(f"   {len(insights)} actionable insights")

    # 4. Update brain
    print("\n3. Updating brain...")
    apply_brain_updates(brain, briefing.get("brain_updates", {}))
    mark_processed(brain, [a.url for a in articles_to_process])
    save_brain(brain)
    print(f"   Brain now has {len(brain.get('topics', []))} topics")

    # 5. Send email
    print("\n4. Sending email...")
    send_briefing(briefing, brain)

    print("\nDone.")


if __name__ == "__main__":
    try:
        run()
    except Exception as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        sys.exit(1)
