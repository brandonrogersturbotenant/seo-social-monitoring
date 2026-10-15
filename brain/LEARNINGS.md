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
- Track NLWeb/ASK protocol, WebMCP, and WordPress's canonical MCP Adapter as complementary agentic-web discovery/commerce mechanisms; pilot the MCP Adapter on a WordPress property and assess whether checkout/lead-gen forms are agent-accessible.
- Deprioritize llms.txt investment — a 300K-domain study found no measurable impact on AI visibility or citations; don't build strategy around it.

## AI Agent SEO Tooling (MCP / Claude Code)

- Pilot MCP-based/agentic SEO tools (e.g., Semrush MCP + Claude for site-audit analysis) and Claude Code workflows on one brand site to automate detection and fixing of schema mismatches, stale links, and content briefs.
- Split audit work into deterministic automated checks, a local LLM for explanation, and human judgment for final calls rather than full automation.
- Test low-stakes, high-volume tasks against local/on-device models (e.g., Gemini Nano) to cut API costs before defaulting to frontier-model tooling.
- Evaluate agentic workflow tooling against manual process time savings before broad adoption.

## AI Citations

- Optimize to become one of the fewer, higher-quality sources AI engines actually cite rather than chasing overall mention volume; favor primary-source, original-data content as citation patterns shift.
- Treat AEO as an extension of core technical SEO (crawlability, indexability, usefulness, correct schema) rather than a separate discipline — fix foundational issues first.
- Mine first-party customer support/FAQ queries to surface exact phrasing that earns citations, and build content blocks around it.
- Run citation gap-analysis (via Semrush or Bing's Topics Portfolio queries-missing-your-site view) to identify which third parties get cited when the brand is missing, and target content/outreach at closing those gaps.
- Check AI brand-recommendation and citation presence in non-English languages relevant to target markets, not just English.

## AI Content Quality Control

- Mandate human editorial review gates for all AI-assisted content across blogs and help centers, extended to titles, alt text, and other metadata per Google's updated guidance.
- Audit AI-assisted content for spam-pattern signals (thin, unoriginal, mass-produced pages) and accelerate this given a predictive model now flagging a ~97% chance of a Panda-style update targeting exactly this within a month.
- Document a formal fact-check sign-off step in the editorial workflow before publishing any AI-assisted content.
- Verify no author bios or bylines use fabricated/deceptive authorship information per Google's explicit warning.
- Review outreach/PR/citation-building tactics against Anthropic's updated Claude usage policy explicitly targeting manipulative 'seeding' of sources to influence AI answers.

## AI Crawler Access & Traffic Measurement

- Hold off on blocking AI bots (GPTBot, ClaudeBot, PerplexityBot, etc.) — commonly cited AI-referral metrics have unknown/incomplete denominators; wait for first-party log data.
- Ensure sitemaps use discoverable default naming and maintain active RSS feeds, since AI training crawlers typically can't be directly submitted to but do access sitemaps/RSS per Google's own logs.
- Verify CDN and per-engine settings directly: Cloudflare governs bots by broad category, its 'Disallow AI Training' toggle exempts Googlebot, and Bing won't honor these signals until early 2027.
- Manage publisher AI-payment models separately and temper expectations: Google's AI Contribution Pilot (now at 400 partner publications), Cloudflare's Monetization Gateway/Pay Per Use, and Microsoft's framework are immature, incompatible programs.
- Audit form-submission and lead-gen endpoints for bot-abuse protection, given confirmed cases of AI agents bypassing site restrictions and submitting real forms during testing.

## AI Diagnostic Reliability

- Treat AI-generated SEO root-cause diagnoses (e.g., for traffic drops) as hypotheses requiring human verification against GSC/analytics, not conclusions.
- Maintain an internal triage checklist (crawling, tracking, algorithm, manual action, migration/site-quality issues) so teams don't over-rely on confident-sounding but unverified AI answers.

## AI Localization/Translation Quality

- Benchmark leading LLMs directly against human translators for any planned multilingual content expansion.
- Select translation workflow (model vs. human vs. hybrid) per content type based on task-specific performance rather than defaulting to human-only.

## AI Overviews / AI Search Measurement Strategy

- Abandon rigid position (1-10) tracking on AIO/AI Mode-exposed queries — focus on outcomes (visits/conversions), not rank; note AIOs can trigger even on typo/no-match queries.
- Re-audit branded query AIOs weekly, factoring in Google's latest link-placement changes (inline links moved higher, expanded Preferred Source carousels); strengthen presence on commonly-cited third parties (Wikipedia, YouTube, review sites) where displacement occurs.
- Adopt a structured metrics framework covering brand presence, answer accuracy, and attribution, layered with citation-to-conversion and clicks-per-citation KPIs rather than reporting mention counts alone.
- Structure content briefs around nested sub-query/query fan-out coverage to capture AI-driven long-tail traffic, noting studies show only a minority of queries actually trigger fan-out expansion.
- Cross-check any third-party rank-tracking data against GSC directly, since Google's anti-scraping defenses (including reported 'poisoned' results served to trackers) are increasingly breaking third-party tools.

## AI Paid Media Compliance

- Audit default AI automation settings in Google/Meta ad accounts for compliance risk given fair housing/financial-services ad regulations relevant to rental and property management advertising.
- Document organizational AI usage policies for paid media teams to avoid platform-default settings creating unreviewed compliance exposure.
- Review updated Google Ads Data Strength best practices (first-party data, Data Manager, AI-powered campaigns) and align account setups accordingly.

## AI Search Attribution

- Move away from pure click-based attribution for AI-driven traffic; build value-based measurement (conversion value per AI-referred visit, assisted conversions, survey-based influence data).
- Update analytics referral rules to capture Gemini's new UTM parameters and segment Gemini traffic value against standard organic and other AI referral sources.
- Build fallback referrer-domain detection for ChatGPT traffic now that OpenAI has dropped UTM parameters from ChatGPT links as of GPT-6, breaking prior tracking methods.
- Report exposure to stakeholders as visibility + commercial/traffic-dependency data combined, not raw citation/visibility counts alone.
- Build budget narratives around revenue, risk reduction, and infrastructure value (not clicks/rankings) to justify continued SEO/AEO investment despite traffic declines.

## AI Shopping Agent Readiness

- Audit plan/pricing/product pages for plain-text answers to common transactional questions (cancellation, billing, trial terms, fees) rather than relying solely on structured data.
- Benchmark brand pages against the agent-readiness failure patterns found in the 122-store Shopify study.
- Monitor Google's new Universal Cart/Universal Commerce Protocol for future relevance to transactional rental/application flows, even though not yet directly applicable.

## AI Visibility Monitoring Tools

- Pilot an AI-visibility dashboard (Semrush-style or dedicated platforms like Peec AI/Scrunch AI) that cross-references AI citation presence against actual Google click performance; use seoClarity's 8-platform comparison framework to guide vendor shortlisting.
- Use rising AI crawler traffic volume (per Cloudflare Radar-type data) as justification for budget toward dedicated AI-visibility monitoring rather than ad hoc checks.
- Use Bing Webmaster Tools' Topics Portfolio to find queries where competitors are cited but the brand isn't, and prioritize content fixes against that gap list.
- Consider earmarking Q4 budget specifically for AI-visibility/citation-gap initiatives with a defined Feb proof-of-impact checkpoint.

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

## Content Distribution System

- Assign a named distribution owner to every major content asset at publish time.
- Build a repeatable 90-day post-publish checklist (outreach, syndication, internal linking, PR) aimed at earning backlinks and AI citations.
- Review underperforming older content against this checklist to re-ignite distribution rather than only focusing on new launches.

## Core Web Vitals — Soft Navigation

- Identify SPA/dashboard-style sections on brand sites that use client-side route changes without full page loads.
- Monitor CrUX experimental soft navigation metrics for these sections ahead of expected Search Console integration.

## Feed / Rendered Listing Data Integrity

- Audit live listing/product SERP presentation (prices, sale badges, images) against current source feed data to catch Google's cached/derived data mismatches.
- Set a recurring spot-check process for high-value listing pages comparing rendered search results to the actual feed.
- Throttle high-churn feed fields (price, availability) to avoid more-than-daily changes now that Merchant Center may disapprove (not just update) frequently-changing products on mismatch detection.
- Deprioritize emergency fixes for low-quality listing images since Google confirmed poor image quality alone no longer blocks Search/Ads inclusion.
- If using Merchant Center video uploads, watch for the current 'stuck in preview processing' bug and avoid repeated re-uploads until Google resolves it.

## Google AI Contribution Pilot

- Watch Search Console for pilot access, but keep expectations minimal — confirmed payouts are under 0.1% of ad revenue with unclear/inconsistent calculation methods across the now-400 participating publications.
- Note it pays only for direct content contribution to AI answers, not standard citations/links — temper monetization expectations from rising citation volume alone.
- Treat this pilot as a reason to avoid blocking AI crawlers until its impact and eligibility are better understood, not as a revenue strategy.

## Google Algorithm Update

- Check GSC Manual Actions report across all brand properties given reported enforcement uptick now that the September 2026 spam update has fully completed.
- Treat a prediction model's ~97% signal of an imminent Panda-style update as a trigger to accelerate (not wait on) AI-content spam-pattern and fake-author audits.
- Only attribute ranking drops to a spam update if policy-violating practices (including AI content spam) are present; treat unconfirmed volatility spikes with skepticism.
- Set clear milestones before reacting to future update rollouts — separate early volatility from lasting losses rather than making reactive site changes mid-rollout.
- When post-migration indexing stalls or old URLs reappear, evaluate underlying site quality (not just redirects/canonicals) and expect migration processing to legitimately take 4+ months before escalating.

## Google Indexing API Delays

- Do not build listing-freshness strategy dependent on timely Indexing API approval — precedent shows months-long, undocumented review waits.

## Google Manual Actions

- Check the GSC Manual Actions report across all brand properties given reported recent uptick in enforcement following the completed September spam update.
- Audit syndicated, partner, affiliate, and UGC content for policy compliance as a precaution.

## Google Search Profile Badges

- Keep Search Profile badge widgets live on named-author pages for mobile, since the Follow button was removed from desktop results but remains on mobile.
- Delay heavier investment in desktop-specific Search Profile UX until the feature stabilizes.
- Pair with the lowered 10K-follower eligibility threshold to capture follow-based visibility as traffic patterns shift.

## GSC Reporting

- Flag anomalous indexing count drops and broken date-picker behavior (e.g., stuck end-date bugs) as likely reporting bugs before launching technical audits, but keep monitoring given elevated indexing complaints.
- Use the new multi-select country filter in Performance reports to build grouped regional views instead of checking countries one at a time.
- Use the new Multimodal vs Text-based filter in the Web search Performance report to baseline image-search contribution on listing-photo and infographic-heavy pages.
- Track Preferred Source subscriber-count emails as a new baseline KPI, and re-baseline desktop vs. mobile CTR trends now that the prior logging error has been resolved.
- Don't over-react to 'Couldn't fetch' sitemap errors alone; verify via URL inspection/live test since the error may not reflect Google's actual fetch ability.

## Helpful Content Guidelines — Main Content & Fake Authors

- Audit key templates against Google's newly clarified Main Content definition to ensure substantive, original content (not boilerplate/ads/nav) is the clear primary focus.
- Verify all published author bios/profiles are real, accurate, and not fabricated or templated placeholders, per Google's explicit warning against deceptive authorship information.
- Tie this audit into existing E-E-A-T and author schema initiatives given Google's increased scrutiny and a predictive model flagging a likely Panda-style update within a month.

## Large Site Indexing / Aggregator Pages

- If any brand property functions as a large listing/directory/aggregator site, audit the ratio of crawled-to-indexed pages rather than assuming crawl volume signals health.
- Consolidate, de-duplicate, or add unique value to thin aggregator-style pages to improve indexation rates.
- Confirm homepage and key hub pages carry sufficiently unique, substantive content to avoid aggregator-style indexing suppression.

## Local SEO / GBP

- Use new GBP post view counts (Search + Maps, 18-month lookback) to benchmark and optimize post content types on local/regional pages.
- Review all GBP post and listing content against the updated advertising/solicitation prohibited-content policy to avoid suspension risk.
- Apply early for GBP API access given confirmed processing delays if planning bulk/multi-location integrations.
- Monitor automated spam-review-removal alerts and near-daily suggested-edit queues (auto-applied after 4 days if unrejected).
- Confirm WhatsApp messaging is connected on listings where it supports lead flow, and audit multi-location pages against a single-source-of-truth record model feeding page, GBP, schema, and directory listings.

## Local Service Ads Lead Reporting

- Review updated LSA 'how leads work' documentation against current billing/dispute practices for any brand running Local Service Ads.
- Re-train local ops/support staff on what now qualifies as a billable phone lead and how lead-quality credits are handled.

## PDF SEO / AEO

- Audit brand PDFs for text-based (not scanned-image) content to ensure crawlability and indexing.
- Verify links and images inside key PDFs are being processed/indexed correctly via URL inspection.
- Consider republishing high-value PDF guides as HTML pages to improve AI Mode/AEO citation potential and ranking flexibility.

## Product Page Copy for AI Agents

- Audit pricing/feature pages to ensure differentiator messaging exists in prose, not just schema/feed data, so AI shopping agents don't default to generic summaries.
- Verify policy/FAQ content (cancellation, billing, trial terms) is plainly readable in page text, since real-world agent testing shows agents fail transactional questions even on 'agent-ready' stores.

## Publisher Organic Traffic Decline

- Prioritize investment in direct channels (email, app, community) to hedge against accelerating YoY organic search/Discover referral decline.
- Benchmark visibility trend against vertical-wide SaaS decline (~1/3 YoY loss reported) and real-estate-category movers to contextualize brand performance.
- Prepare for further Discover volatility as Google rebuilds it into an AI-driven 'Concierge' experience with tighter YouTube integration.

## Rank Tracking Reliability

- Cross-check any third-party rank-tracking tool output against GSC Performance data given ongoing, worsening scraper-blocking and reported result 'poisoning' aimed at rank-tracking bots.
- Build contingency/redundancy into visibility reporting workflows rather than relying on a single rank-tracking vendor.

## Schema — AI Visibility Mistakes

- Audit schema across key templates for completeness and content-match accuracy (not just validator pass/fail), since mismatches actively hurt AI visibility.
- Prioritize fixing missing/outdated/mismatched structured data on pages targeted for AEO/AI citation.

## Schema — Review Snippets

- Check whether any health/safety-adjacent brand content falls into categories where Google may be suppressing review rich snippets despite valid markup.
- Avoid over-investing in review schema for affected content verticals until Google clarifies scope of the change.

## Schema — Video Structured Data

- Add creator/author properties to VideoObject schema on any video content to strengthen E-E-A-T signals.
- Coordinate with Search Profile badge rollout for named authors/creators across video and article content.

## Static Site SEO Gaps

- Audit any static-site-generator-based brand property or microsite for manually-required canonicals, sitemaps, redirects, metadata, schema, and 404 handling that CMS plugins normally automate.
- Weigh Astro-style islands architecture for any new lightweight/microsite builds where CWV performance is a priority.

## Technical SEO Process

- Review internal technical SEO audit workflows for prioritization and follow-through gaps, not just checklist/tooling coverage.
- Assign clear ownership and remediation SLAs for recurring audit findings across brand sites.
- Apply scientific-method discipline (clear hypothesis, control group, adequate sample size, confounder checks) when designing and interpreting SEO experiments.

## UGC Fresh Data Program

- Review Google's new documentation on UGC fresh-data partnerships to determine eligibility criteria for any brand forum, reviews, or community content.
- Audit UGC sections for freshness, structure, and update cadence to position for potential inclusion in similar data-sharing arrangements.

## WordPress Platform Maintenance

- Confirm all WordPress-based brand properties are updated to the latest patched core version promptly after security releases, including Jetpack 16.3's accessibility/security update.
- Verify critical workflows (e.g., image uploads) post-update to catch regressions before they affect content publishing.
- Evaluate newly added Jetpack blocks (Latest Videos Playlist, video discovery, appointment scheduling) for applicability to relevant brand pages.
- Immediately audit for and patch the All In One SEO (AIOSEO) plugin if in use, given two medium-severity unauthenticated-attacker vulnerabilities.
- Update to Yoast SEO 28.7 where used and test post-update for regressions from its deprecated-code cleanup; evaluate new AI-assisted title/meta/social-preview editing features.
