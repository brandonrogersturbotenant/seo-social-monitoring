"""SEO Morning Brief — daily RSS monitoring pipeline."""

import sys
from collections import Counter

from src.brain import (
    apply_brain_updates,
    filter_unprocessed,
    load_brain,
    mark_processed,
    save_brain,
)
from src.emailer import send_briefing
from src.fetcher import diversify_articles, fetch_recent_articles
from src.summarizer import generate_briefing


def run() -> None:
    print("SEO Morning Brief — starting run\n")

    # 1. Fetch articles from last 24 hours
    print("1. Fetching RSS feeds (last 24h)...")
    articles = fetch_recent_articles(hours=24)
    by_source = Counter(a.source for a in articles)
    print(f"   Found {len(articles)} articles across all feeds")
    if by_source:
        print("   By source: " + ", ".join(f"{k}={v}" for k, v in sorted(by_source.items())))

    # 2. Load brain and filter already-processed
    brain = load_brain()
    new_articles = filter_unprocessed(articles, brain)
    print(f"   {len(new_articles)} are new (not previously processed)")

    # 3. Diversify across sources, then generate briefing
    print("\n2. Generating briefing with Claude...")
    articles_to_process = diversify_articles(new_articles)
    briefing = generate_briefing(articles_to_process, brain)
    insights = briefing.get("todays_insights", [])
    print(f"   {len(insights)} topics")

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
