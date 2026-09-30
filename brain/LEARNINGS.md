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
- Track NLWeb/ASK protocol and WebMCP adoption as complementary agentic-web discovery/commerce mechanisms; assess whether checkout/lead-gen forms are agent-accessible.
- Evaluate llms.txt as a low-cost experiment, but confirm actual crawler adoption before investing significant effort.

## AI Agent SEO Tooling (MCP / Claude Code)

- Pilot MCP-based/agentic SEO tools and Claude Code workflows on one brand site to automate detection and fixing of schema mismatches, stale links, and content briefs.
- Prioritize highest-value use cases (GSC analysis, internal linking audits, technical fixes) before scaling to all domains.
- Evaluate agentic workflow tooling against manual process time savings before broad adoption.

## AI Citations

- Optimize to become one of the fewer, higher-quality sources AI engines actually cite rather than chasing overall mention volume.
- Treat AEO as an extension of core technical SEO (crawlability, indexability, usefulness) rather than a separate discipline — fix foundational issues first.
- Audit how LLMs describe brand positioning/differentiators vs. current messaging and refresh key pages to close any 'positioning lag.'
- Pursue third-party trust signals (Wikipedia presence, podcast appearances, Reddit engagement) via PR as a deliberate AI-citation-building tactic.
- Use a diagnostic framework (missing from conversations / losing recommendations / wrong topic associations / outdated info / inaccessible content) to triage visibility gaps before picking tactics.

## AI Content Quality Control

- Mandate human editorial review gates for all AI-assisted content across blogs and help centers to protect E-E-A-T and avoid quality regressions.
- Audit AI-assisted content for spam-pattern signals (thin, unoriginal, mass-produced pages) given Google's active AI-content spam detection (SAFE) enforcement.
- Benchmark internal AI content production volume/workflow against industry norms (now ~93% of marketers use AI in content creation) to ensure quality controls scale with volume.

## AI Crawler Access & Traffic Measurement

- Hold off on blocking AI bots (GPTBot, ClaudeBot, PerplexityBot, etc.) — commonly cited AI-referral metrics have unknown/incomplete denominators; wait for first-party log data.
- Verify CDN and per-engine settings directly: Cloudflare governs bots by broad category, its 'Disallow AI Training' toggle exempts Googlebot, and Bing won't honor these signals until early 2027.
- Manage publisher AI-payment models separately and temper expectations: Google's AI Contribution Pilot covers only ~100 publishers paying ~0.1% of ad revenue, distinct from Cloudflare's pay-per-crawl and Microsoft's framework.
- Supplement robots.txt with terms-of-service language for unwanted shopping/browser agents, since robots.txt directives alone can't distinguish agents from real visitors.
- Test publishing sourced, structured brand-context content aimed at AI crawlers (machine-layer approach) on one property and measure recommendation/citation rate change.

## AI Localization/Translation Quality

- Benchmark leading LLMs directly against human translators for any planned multilingual content expansion.
- Select translation workflow (model vs. human vs. hybrid) per content type based on task-specific performance rather than defaulting to human-only.

## AI Overviews / AI Search Measurement Strategy

- Abandon rigid position (1-10) tracking on AIO/AI Mode-exposed queries — focus on outcomes (visits/conversions), not rank.
- Segment AIO link interactions by destination (web vs AI Mode) in GSC, since rising AIO link counts don't guarantee proportional web traffic.
- Adopt a structured metrics framework covering brand presence, answer accuracy, and attribution, layered with citation-to-conversion and clicks-per-citation KPIs rather than reporting mention counts alone.
- Structure content briefs around nested sub-query/query fan-out coverage to capture AI-driven long-tail traffic.
- Add visible last-updated dates/changelogs to key pages and periodically re-verify AI-cited facts (pricing, legal/compliance) against live pages, since AIOs now increasingly surface on branded queries too.

## AI Search Attribution

- Move away from pure click-based attribution for AI-driven traffic; build value-based measurement (conversion value per AI-referred visit) — reinforced by reports confirming AI chat interfaces drive minimal click-through.
- Segment analytics to compare AI-referral traffic value against standard organic, since AI-referred visitors can convert at multiples of average organic value.
- Report exposure to stakeholders as visibility + commercial/traffic-dependency data combined, not raw citation/visibility counts alone.

## AI-Era Content Validation Workflow

- Identify decision gaps competitors/AI summaries haven't addressed and fill them with original, proprietary knowledge.
- Prove claims with evidence/data before publishing, especially on YMYL legal and investment guide content, to differentiate from AI-summarized competitor content.

## Audience Data Quality for AI Agents

- Audit first-party audience/segment data quality feeding any AI-driven personalization, targeting, or agent-facing tools.
- Treat audience/data hygiene as a prerequisite for AI visibility strategy, not just an ads/marketing concern.

## Canonical Tag Hygiene

- Run periodic canonical tag audits across all brand domains, especially syndicated content, partner integrations, and shared templates, to catch cross-domain misconfigurations before they cause silent de-indexing.

## Google AI Contribution Pilot

- Watch Search Console for pilot access, but keep expectations minimal — confirmed payouts are ~100 publishers receiving roughly 0.1% of ad revenue.
- Note it pays only for direct content contribution to AI answers, not standard citations/links — temper monetization expectations from rising citation volume alone.
- Treat this pilot as a reason to avoid blocking AI crawlers until its impact and eligibility are better understood, not as a revenue strategy.

## Google Algorithm Update

- Treat unconfirmed ranking volatility spikes with skepticism — some past swings have been linked to bot-blocking crackdowns rather than core updates.
- For the confirmed September 2026 spam update, check GSC clicks/impressions for weekend (9/25-9/27) impact and only attribute drops to it if policy-violating practices (including AI content spam flagged by SAFE) are present.
- Continue monitoring through the full two-week global rollout before finalizing any content/technical remediation.

## Google Indexing API Delays

- Do not build listing-freshness strategy dependent on timely Indexing API approval — precedent shows months-long, undocumented review waits.

## Google Search Profile Badges

- Keep Search Profile badge widgets live on named-author pages for mobile, since the Follow button was removed from desktop results but remains on mobile.
- Delay heavier investment in desktop-specific Search Profile UX until the feature stabilizes.
- Pair with the lowered 10K-follower eligibility threshold to capture follow-based visibility as traffic patterns shift.

## GSC Reporting

- Flag anomalous indexing count drops as likely reporting bugs before launching technical audits, but keep monitoring given elevated indexing complaints.
- Use the new Multimodal vs Text-based filter in the Web search Performance report to baseline image-search contribution on listing-photo and infographic-heavy pages.
- Re-baseline desktop vs. mobile CTR trends now that the prior Search Console logging error has been resolved, and segment CTR analysis by device going forward.
- Discount any GA anomalies during known outage windows before drawing performance conclusions.
- Enable app conversion tracking in GA cross-channel reports if a companion app exists, for unified attribution.

## Local SEO / GBP

- Use new GBP post view counts (Search + Maps, 18-month lookback) to benchmark and optimize post content types on local/regional pages.
- Apply early for GBP API access given confirmed processing delays if planning bulk/multi-location integrations.
- Monitor automated spam-review-removal alerts as an early signal of review manipulation, and verify legitimate negative reviews weren't wrongly removed.
- Implement near-daily monitoring of GBP suggested edits — Google may auto-apply unrejected edits after 4 days.
- Adjust review-monitoring workflows now that Google Maps requires sign-in to read/sort/leave all reviews, which may break scraping-based tools.

## Product Page Copy for AI Agents

- Audit pricing/feature pages to ensure differentiator messaging exists in prose, not just schema/feed data, so AI shopping agents don't default to generic summaries.

## Publisher Organic Traffic Decline

- Prioritize investment in direct channels (email, app, community) to hedge against accelerating YoY organic search/Discover referral decline.

## Schema — Video Structured Data

- Add creator/author properties to VideoObject schema on any video content to strengthen E-E-A-T signals.
- Coordinate with Search Profile badge rollout for named authors/creators across video and article content.

## Technical SEO Process

- Review internal technical SEO audit workflows for prioritization and follow-through gaps, not just checklist/tooling coverage.
- Assign clear ownership and remediation SLAs for recurring audit findings across brand sites.
