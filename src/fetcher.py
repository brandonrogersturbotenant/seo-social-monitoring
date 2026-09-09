from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

import feedparser
import httpx

from src.config import load_sources


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
    # Strip basic HTML tags for a cleaner prompt
    import re

    text = re.sub(r"<[^>]+>", " ", summary)
    return " ".join(text.split())[:500]


def fetch_recent_articles(hours: int = 24) -> list[Article]:
    config = load_sources()
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    seen_urls: set[str] = set()
    articles: list[Article] = []

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; SEOBriefBot/1.0; +https://github.com/brandonrogersturbotenant/seo-social-monitoring)"
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
