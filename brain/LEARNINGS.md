# SEO Brain — Running Learnings

Condensed action playbook. Revised each morning — bullets are updated in place, not appended forever.

## 2026 Google Ranking Factors

- Prioritize original content/data assets, content quality, and backlink acquisition over marginal technical fixes on already-healthy sites — these rank as top factors in expert surveys.

## Accessibility & SEO

- Run an accessibility audit (semantic HTML, alt text, heading structure, ARIA labels, keyboard navigation) on key page templates as a dual-purpose SEO/accessibility improvement.

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
- Test low-stakes, high-volume tasks against local/on-device models (e.g., Gemini Nano) to cut API costs before defaulting to frontier-model tooling.

## AI Citations

- Optimize to become one of the fewer, higher-quality sources AI engines actually cite rather than chasing overall mention volume.
- Treat AEO as an extension of core technical SEO (crawlability, indexability, usefulness, correct schema) rather than a separate discipline — fix foundational issues first.
- Mine first-party customer support/FAQ queries to surface exact phrasing that earns citations, and build content blocks around it.
- Pursue third-party trust signals (Wikipedia presence, podcast appearances, Reddit engagement) via PR as a deliberate AI-citation-building tactic.
- Use a diagnostic framework (missing from conversations / losing recommendations / wrong topic associations / outdated info / inaccessible content) to triage visibility gaps before picking tactics.

## AI Content Quality Control

- Mandate human editorial review gates for all AI-assisted content across blogs and help centers, now explicitly extended to titles, alt text, and other metadata per Google's updated guidance.
- Audit AI-assisted content for spam-pattern signals (thin, unoriginal, mass-produced pages) given Google's active AI-content spam detection (SAFE) enforcement.
- Document a formal fact-check sign-off step in the editorial workflow before publishing any AI-assisted content.
- Benchmark internal AI content production volume/workflow against industry norms to ensure quality controls scale with volume.

## AI Crawler Access & Traffic Measurement

- Hold off on blocking AI bots (GPTBot, ClaudeBot, PerplexityBot, etc.) — commonly cited AI-referral metrics have unknown/incomplete denominators; wait for first-party log data.
- Verify CDN and per-engine settings directly: Cloudflare governs bots by broad category, its 'Disallow AI Training' toggle exempts Googlebot, and Bing won't honor these signals until early 2027.
- Manage publisher AI-payment models separately and temper expectations: Google's AI Contribution Pilot pays some sites under 0.1% of ad revenue with unclear calculation methods; Cloudflare's new Monetization Gateway/Pay Per Use beta and Microsoft's framework are separate, immature programs.
- Supplement robots.txt with terms-of-service language for unwanted shopping/browser agents, since robots.txt directives alone can't distinguish agents from real visitors.
- Test publishing sourced, structured brand-context content aimed at AI crawlers (machine-layer approach) on one property and measure recommendation/citation rate change.

## AI Localization/Translation Quality

- Benchmark leading LLMs directly against human translators for any planned multilingual content expansion.
- Select translation workflow (model vs. human vs. hybrid) per content type based on task-specific performance rather than defaulting to human-only.

## AI Overviews / AI Search Measurement Strategy

- Abandon rigid position (1-10) tracking on AIO/AI Mode-exposed queries — focus on outcomes (visits/conversions), not rank.
- Segment AIO link interactions by destination (web vs AI Mode) in GSC, and watch for newly-tested AIO URL tracking parameters that could enable AIO-specific click attribution.
- Adopt a structured metrics framework covering brand presence, answer accuracy, and attribution, layered with citation-to-conversion and clicks-per-citation KPIs rather than reporting mention counts alone.
- Structure content briefs around nested sub-query/query fan-out coverage to capture AI-driven long-tail traffic.
- Audit branded-query AIOs (now present on ~83% of branded searches) for third-party source displacement, and strengthen presence on commonly-cited third parties (Wikipedia, YouTube, review sites).

## AI Search Attribution

- Move away from pure click-based attribution for AI-driven traffic; build value-based measurement (conversion value per AI-referred visit).
- Update analytics referral rules to capture Gemini's new UTM parameters and segment Gemini traffic value against standard organic and other AI referral sources.
- Report exposure to stakeholders as visibility + commercial/traffic-dependency data combined, not raw citation/visibility counts alone.

## AI-Era Content Validation Workflow

- Identify decision gaps competitors/AI summaries haven't addressed and fill them with original, proprietary knowledge.
- Prove claims with evidence/data before publishing, especially on YMYL legal and investment guide content, to differentiate from AI-summarized competitor content.
- Test writing precise, unambiguous 'technical manual' style passages on key guide/help pages to improve LLM parsing and citation accuracy.

## Audience Data Quality for AI Agents

- Audit first-party audience/segment data quality feeding any AI-driven personalization, targeting, or agent-facing tools.
- Treat audience/data hygiene as a prerequisite for AI visibility strategy, not just an ads/marketing concern.

## Canonical Tag Hygiene

- Run periodic canonical tag audits across all brand domains, especially syndicated content, partner integrations, and shared templates, to catch cross-domain misconfigurations before they cause silent de-indexing.
- For any statically-generated site or section, confirm canonicals, sitemaps, redirects, and 404 handling are manually implemented since CMS plugin automation won't apply.

## Google AI Contribution Pilot

- Watch Search Console for pilot access, but keep expectations minimal — confirmed payouts are under 0.1% of ad revenue with unclear/inconsistent calculation methods across participants.
- Note it pays only for direct content contribution to AI answers, not standard citations/links — temper monetization expectations from rising citation volume alone.
- Treat this pilot as a reason to avoid blocking AI crawlers until its impact and eligibility are better understood, not as a revenue strategy.

## Google Algorithm Update

- Treat unconfirmed ranking volatility spikes with skepticism — some past swings have been linked to bot-blocking crackdowns rather than core updates.
- For the confirmed September 2026 spam update (two waves: ~9/25-9/27 and 9/30), check GSC clicks/impressions across both windows and only attribute drops to it if policy-violating practices (including AI content spam flagged by SAFE) are present.
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

## Helpful Content Guidelines — Main Content & Fake Authors

- Audit key templates to ensure Main Content (not boilerplate, ads, or navigation) is substantive, original, and clearly the primary focus, per Google's rater-aligned definition.
- Verify all published author bios/profiles are real, accurate, and not fabricated or templated placeholders.
- Tie this audit into existing E-E-A-T and author schema initiatives given Google's increased scrutiny on both fronts.

## Local SEO / GBP

- Use new GBP post view counts (Search + Maps, 18-month lookback) to benchmark and optimize post content types on local/regional pages.
- Apply early for GBP API access given confirmed processing delays if planning bulk/multi-location integrations.
- Monitor automated spam-review-removal alerts as an early signal of review manipulation, and verify legitimate negative reviews weren't wrongly removed.
- Implement near-daily monitoring of GBP suggested edits — Google may auto-apply unrejected edits after 4 days.
- If running Local Service Ads, audit served locations against configured service areas (confirmed targeting bug) and verify the new default-hidden phone number display isn't suppressing call conversions.

## Product Page Copy for AI Agents

- Audit pricing/feature pages to ensure differentiator messaging exists in prose, not just schema/feed data, so AI shopping agents don't default to generic summaries.

## Publisher Organic Traffic Decline

- Prioritize investment in direct channels (email, app, community) to hedge against accelerating YoY organic search/Discover referral decline.
- Benchmark visibility trend against vertical-wide SaaS decline (~1/3 YoY loss reported) and real-estate-category movers to contextualize brand performance.

## Schema — AI Visibility Mistakes

- Audit schema across key templates for completeness and content-match accuracy (not just validator pass/fail), since mismatches actively hurt AI visibility.
- Prioritize fixing missing/outdated/mismatched structured data on pages targeted for AEO/AI citation.

## Schema — Video Structured Data

- Add creator/author properties to VideoObject schema on any video content to strengthen E-E-A-T signals.
- Coordinate with Search Profile badge rollout for named authors/creators across video and article content.

## Static Site SEO Gaps

- Audit any static-site-generator-based brand property or microsite for manually-required canonicals, sitemaps, redirects, metadata, schema, and 404 handling that CMS plugins normally automate.

## Technical SEO Process

- Review internal technical SEO audit workflows for prioritization and follow-through gaps, not just checklist/tooling coverage.
- Assign clear ownership and remediation SLAs for recurring audit findings across brand sites.
