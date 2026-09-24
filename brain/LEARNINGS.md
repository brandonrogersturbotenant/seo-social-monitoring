# SEO Brain — Running Learnings

Condensed action playbook. Revised each morning — bullets are updated in place, not appended forever.

## 2026 Google Ranking Factors

- Prioritize original content/data assets, content quality, and backlink acquisition over marginal technical fixes on already-healthy sites — these rank as top factors in expert surveys.

## Affiliate/Partner Brand Bidding Leakage

- Build a recurring search test list to detect partners bidding on brand terms in paid ads.
- Capture ad evidence and match violations to specific partner/affiliate accounts.
- Run this audit periodically given affiliate/comparison-site prevalence in the PM software niche.

## AI Agent Resource Discovery (ARD)

- Use Lighthouse 13.5's ARD audit as an early diagnostic, not a compliance signal — its checks diverge from the emerging community ARD standard.
- Re-audit sites once the ARD standard finalizes rather than relying on current Lighthouse scores.

## AI Citation Behavior

- Optimize to become one of the fewer, higher-quality sources AI engines actually cite rather than chasing overall mention volume, as models increasingly cite fewer sources per answer despite broader web searching.

## AI Content Quality Control

- Mandate human editorial review gates for all AI-assisted content across blogs and help centers to protect E-E-A-T and avoid quality regressions.

## AI Crawler Access & Traffic Measurement

- Hold off on blocking AI bots (GPTBot, ClaudeBot, PerplexityBot, etc.) — commonly cited AI-referral metrics have unknown/incomplete denominators; wait for first-party log data.
- Verify CDN and per-engine settings directly: Cloudflare governs bots by broad category, its 'Disallow AI Training' toggle exempts Googlebot, and Bing won't honor these signals until early 2027.
- Manage publisher AI-payment models separately: Google's AI Contribution Pilot, Cloudflare's pay-per-crawl, and Microsoft's framework are incompatible systems requiring independent decisions.

## AI Overviews / AI Search Measurement Strategy

- Abandon rigid position (1-10) tracking on AIO/AI Mode-exposed queries — Search Console block flattening distorts position data, and Google's own guidance is to focus on outcomes (visits/conversions), not rank.
- Build citation-to-conversion and clicks-per-citation KPIs (composite, harder-to-game metrics) rather than raw AI mention/citation counts.
- Structure content briefs around nested sub-query/query fan-out coverage to capture AI-driven long-tail traffic; revalidate as Google's fan-out frameworks (e.g., R4T-Diffusion) expand.
- Optimize local/informational pages for AI citation: write clean citable passages, use descriptive alt text, and only publish verifiable, current numbers/stats.
- Add visible last-updated dates/changelogs to key pages and periodically re-verify AI-cited facts (pricing, legal/compliance) against live pages to counter stale AI answer snapshots.

## AI-Era Content Validation Workflow

- Identify decision gaps competitors/AI summaries haven't addressed and fill them with original, proprietary knowledge.
- Prove claims with evidence/data before publishing, especially on YMYL legal and investment guide content, to differentiate from AI-summarized competitor content.

## Canonical Tag Hygiene

- Run periodic canonical tag audits across all brand domains, especially syndicated content, partner integrations, and shared templates, to catch cross-domain misconfigurations before they cause silent de-indexing.

## Google AI Contribution Pilot

- Watch Search Console for pilot access to Google's AI Contribution Pilot program.
- Note it pays only for direct content contribution to AI answers, not standard citations/links — temper monetization expectations from rising citation volume alone.
- Treat this pilot as a reason to avoid blocking AI crawlers until its impact and eligibility are better understood.

## Google Algorithm Update

- Treat unconfirmed ranking volatility spikes with skepticism — recent swings have been linked to Google's scraper/bot-blocking crackdowns, not core updates.
- Validate any suspected update impact against GSC clicks/impressions before making content or technical changes.
- For the confirmed September 2026 spam update, only attribute drops to it if a site engages in policy-violating practices; monitor through the multi-week global rollout.

## Google Indexing API Delays

- Do not build listing-freshness strategy dependent on timely Indexing API approval — precedent shows months-long, undocumented review waits.

## Google Search Profile Badges

- Add Search Profile badge widgets to named-author pages to let users follow creators/publishers directly into Search.
- Pair with the lowered 10K-follower eligibility threshold to capture follow-based visibility as traffic patterns shift.

## GSC Reporting

- Flag anomalous indexing count drops as likely reporting bugs before launching technical audits, but keep monitoring given elevated indexing complaints.
- Use the new Multimodal vs Text-based filter in the Web search Performance report to baseline image-search contribution on listing-photo and infographic-heavy pages.

## Local SEO / GBP

- Use new GBP post view counts (Search + Maps, 18-month lookback) to benchmark and optimize post content types on local/regional pages.
- Apply early for GBP API access given confirmed processing delays if planning bulk/multi-location integrations.
- Monitor automated spam-review-removal alerts as an early signal of review manipulation, and verify legitimate negative reviews weren't wrongly removed.
- Implement near-daily monitoring of GBP suggested edits — Google may auto-apply unrejected edits after 4 days.
- Confirm current process with GBP support before relying on self-service for closure status changes, since that option appears removed without notice.

## Product Page Copy for AI Agents

- Audit pricing/feature pages to ensure differentiator messaging exists in prose, not just schema/feed data, so AI shopping agents don't default to generic summaries.

## Publisher Organic Traffic Decline

- Prioritize investment in direct channels (email, app, community) to hedge against accelerating YoY organic search/Discover referral decline.

## Schema — Video Structured Data

- Add creator/author properties to VideoObject schema on any video content to strengthen E-E-A-T signals.
- Coordinate with Search Profile badge rollout for named authors/creators across video and article content.
