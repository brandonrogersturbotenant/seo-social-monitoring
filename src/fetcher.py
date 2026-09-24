from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
import re

import feedparser
import httpx

from src.config import load_sources

# Prefer completeness: include many posts, but still round-robin so
# high-volume publishers (SER, SEJ) don't crowd out quieter sources.
MAX_PER_SOURCE = 15
MAX_ARTICLES_PER_RUN = 100


@dataclass
class Article:
    title: str
    url: str
    source: str
    published: datetime
    summary: str


def _parse_published(entry: dict) -> datetime | None:
    for field in ("published_parsed", "updated_parsed"):
        parsed = entry.get(field)
        if parsed:
            return datetime(*parsed[:6], tzinfo=timezone.utc)

    for field in ("published", "updated"):
        raw = entry.get(field)
        if raw:
            try:
                return parsedate_to_datetime(raw).astimezone(timezone.utc)
            except (TypeError, ValueError):
                continue
    return None


def _clean_summary(entry: dict) -> str:
    summary = entry.get("summary", "") or entry.get("description", "")
    text = re.sub(r"<[^>]+>", " ", summary)
    return " ".join(text.split())[:500]


def fetch_recent_articles(hours: int = 24) -> list[Article]:
    config = load_sources()
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    seen_urls: set[str] = set()
    articles: list[Article] = []

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "application/rss+xml, application/xml, text/xml, */*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }
    with httpx.Client(timeout=30, follow_redirects=True, headers=headers) as client:
        for feed in config["rss_feeds"]:
            name = feed["name"]
            url = feed["url"]
            try:
                response = client.get(url)
                response.raise_for_status()
                parsed = feedparser.parse(response.text)
            except Exception as exc:
                print(f"  [warn] Failed to fetch {name}: {exc}")
                continue

            for entry in parsed.entries:
                link = entry.get("link", "").strip()
                if not link or link in seen_urls:
                    continue

                published = _parse_published(entry)
                if published is None or published < cutoff:
                    continue

                seen_urls.add(link)
                articles.append(
                    Article(
                        title=entry.get("title", "Untitled").strip(),
                        url=link,
                        source=name,
                        published=published,
                        summary=_clean_summary(entry),
                    )
                )

    articles.sort(key=lambda a: a.published, reverse=True)
    return articles


def diversify_articles(
    articles: list[Article],
    max_total: int = MAX_ARTICLES_PER_RUN,
    max_per_source: int = MAX_PER_SOURCE,
) -> list[Article]:
    """Round-robin across sources so high-volume feeds don't monopolize the brief."""
    if not articles:
        return []

    by_source: dict[str, list[Article]] = defaultdict(list)
    for article in articles:
        by_source[article.source].append(article)

    for source in by_source:
        by_source[source].sort(key=lambda a: a.published, reverse=True)

    # Prefer quieter/priority sources first in the rotation by taking
    # one from each source before allowing extras from any source.
    selected: list[Article] = []
    selected_urls: set[str] = set()
    per_source_counts: dict[str, int] = defaultdict(int)

    # Pass 1: one newest article per source
    sources_by_newest = sorted(
        by_source.keys(),
        key=lambda s: by_source[s][0].published,
        reverse=True,
    )
    for source in sources_by_newest:
        if len(selected) >= max_total:
            break
        article = by_source[source][0]
        selected.append(article)
        selected_urls.add(article.url)
        per_source_counts[source] = 1

    # Pass 2: fill remaining slots round-robin, respecting per-source cap
    changed = True
    while len(selected) < max_total and changed:
        changed = False
        for source in sources_by_newest:
            if len(selected) >= max_total:
                break
            if per_source_counts[source] >= max_per_source:
                continue
            for article in by_source[source]:
                if article.url in selected_urls:
                    continue
                selected.append(article)
                selected_urls.add(article.url)
                per_source_counts[source] += 1
                changed = True
                break

    selected.sort(key=lambda a: a.published, reverse=True)

    source_summary = ", ".join(
        f"{src}={count}" for src, count in sorted(per_source_counts.items())
    )
    print(f"   Diversified to {len(selected)} articles ({source_summary})")
    return selected
