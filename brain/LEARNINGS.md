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

- Use Lighthouse 13.5's ARD audit and similar vendor AI-discoverability audits as early diagnostics, not compliance signals — re-audit once the community ARD standard finalizes.
- Track NLWeb/ASK protocol, WebMCP, and WordPress's canonical MCP Adapter as complementary agentic-web discovery/commerce mechanisms; pilot the MCP Adapter on a WordPress property and assess whether checkout/lead-gen forms are agent-accessible.
- Review robots.txt and bot-detection logic for connector/cloud-browser-based personal AI agents that bypass traditional crawler user-agent patterns.
- Deprioritize llms.txt investment — a 300K-domain study found no measurable impact on AI visibility or citations.

## AI Agent SEO Tooling (MCP / Claude Code)

- Pilot MCP-based/agentic SEO tools and Claude Code workflows on one brand site to automate detection and fixing of schema mismatches, stale links, and content briefs.
- Split audit work into deterministic automated checks, a local LLM for explanation, and human judgment for final calls rather than full automation.
- Test low-stakes, high-volume tasks against local/on-device models to cut API costs before defaulting to frontier-model tooling.
- Evaluate agentic workflow tooling against manual process time savings before broad adoption.

## AI Citations

- Reframe KPIs around appearing more often over time, not holding a permanent citation — citation volatility is normal and shifts with model updates.
- Optimize to become one of the fewer, higher-quality sources AI engines actually cite rather than chasing overall mention volume; favor primary-source, original-data content.
- Audit key pages to deliver the direct answer in the opening 1-2 sentences, since AI-cited pages more often answer the question immediately.
- Build a rapid-response process to detect and correct factually wrong brand claims in AI Overviews/answers using clear, direct Q&A-style corrections on owned pages.
- Mine first-party query sources (support tickets, call transcripts, chat logs) to surface exact phrasing that earns citations, and run gap-analysis against competitor citations.

## AI Content Parity / Shadow Web Risk

- Audit any content served specifically to AI crawlers/feeds (llms.txt, hidden data feeds, AI-only pages) for factual parity with the public-facing site.
- Avoid cloaking-adjacent practices where AI systems see different claims/data than human visitors — treat as a long-term trust and policy risk, not just a technical shortcut.

## AI Content Quality Control

- Mandate human editorial review gates for all AI-assisted content across blogs and help centers, extended to titles, alt text, and other metadata.
- Audit AI-assisted content for spam-pattern signals (thin, unoriginal, mass-produced pages) given expanding spam enforcement to UGC-adjacent platforms and tools.
- Document a formal fact-check sign-off step before publishing AI-assisted content, with visible sourcing and honest product-limitation statements.
- Verify no author bios or bylines use fabricated/deceptive authorship information.
- Audit commercial/decision pages for whether they actually answer buyer questions, not just recite brand descriptions.

## AI Crawler Access

- Hold off on blocking AI bots — commonly cited AI-referral metrics have unknown/incomplete denominators; wait for first-party log data.
- Run a server log analysis to confirm which AI crawlers (GPTBot, ClaudeBot, PerplexityBot) actually hit key templates and whether pages render correctly for them.
- Audit key templates for server-side rendering or static HTML fallbacks since ChatGPT, Claude, and Perplexity still largely fail to render JavaScript.
- Check whether brand sites are blocked by OpenAI's Aura safety check and gather evidence to request a review if ChatGPT agent browsing fails.
- Separate crawling-access decisions (robots.txt) from AI-training-use decisions — robots.txt only governs crawling, not downstream content use.

## AI Diagnostic Reliability

- Treat AI-generated SEO root-cause diagnoses as hypotheses requiring human verification against GSC/analytics, not conclusions.
- Maintain an internal triage checklist (crawling, tracking, algorithm, manual action, migration/site-quality issues) so teams don't over-rely on confident-sounding but unverified AI answers.

## AI Localization/Translation Quality

- Benchmark leading LLMs directly against human translators for any planned multilingual content expansion.
- Select translation workflow (model vs. human vs. hybrid) per content type based on task-specific performance rather than defaulting to human-only.

## AI Overviews

- Abandon rigid position (1-10) tracking on AIO/AI Mode-exposed queries — focus on outcomes (visits/conversions), not rank.
- Re-audit commercial query AIOs regularly given AIO coverage now exceeding 80% of searches — prioritize reviews, pricing, and comparison page types.
- Monitor whether the AI Overviews citations card disappears on tracked queries and have a fallback method for measuring source attribution if it's removed.
- Adopt a structured metrics framework covering brand presence, answer accuracy, and attribution, layered with citation-to-conversion and clicks-per-citation KPIs.
- Structure content briefs around nested sub-query/query fan-out coverage to capture AI-driven long-tail traffic.

## AI Paid Media Compliance

- Audit default AI automation settings in Google/Meta/OpenAI ad accounts for compliance risk given fair housing/financial-services ad regulations relevant to rental and property management advertising.
- Review AI-generated 'review summaries' now appearing directly in Google Search ads for accuracy against actual brand reviews; flag inaccuracies via support.
- Review updated Google Ads Data Strength, Smart Bidding learning-period, Customer Lifecycle Goals, and 1-click AI Max experiment guidance before accepting account recommendations.
- Move beyond click-only PPC measurement by layering conversion tracking, impression signals, and business-record validation as buying journeys shift toward AI research.

## AI Search Attribution

- Pull 12-month GA4 LLM-referral traffic data per brand before allocating significant new budget to GEO/AEO tactics; AI assistants drive only a small, uneven share of organic decline.
- Update analytics referral rules to capture Gemini's new UTM parameters and build fallback referrer-domain detection for ChatGPT traffic since OpenAI dropped UTM parameters.
- Avoid treating Direct-traffic increases as proof of AI-driven visibility; apply bot-filtering and server-log cross-checks before attributing any Direct lift to AI assistants.
- Stop relying on single-prompt AI visibility checks; require multi-run sampling before drawing citation-presence conclusions.
- Build a prompt-based tracking framework (not just keyword-based) since matched-user panel data shows meaningfully different behavior between Google and LLM search sessions.

## AI Search Strategy Diagnostics

- Run a layered diagnostic (crawlability/access, content accuracy, structured data, citation performance) before investing in AI-visibility content rewrites.
- Fix the weakest layer first — content rewrites won't help if AI systems can't reach the site or are citing wrong information.
- Benchmark maturity against a phased foundation-to-authority framework rather than defaulting to more content volume.

## AI Shopping Agent Readiness

- Audit plan/pricing/product pages for plain-text answers to common transactional questions (cancellation, billing, trial terms, fees) rather than relying solely on structured data.
- Benchmark brand pages against agent-readiness failure patterns and current best-practice guidance for AI shopping agent visibility.
- Monitor Google's live Universal Cart, Connected Apps Platform, generative UI/booking-intermediary ambitions, and AI Mode sponsored-product blending tests for relevance to transactional rental/application flows.
- Prioritize owned-channel (direct site, app, email) booking/application paths as a hedge against Google-mediated transaction capture.

## AI Visibility Monitoring Tools

- Pilot an AI-visibility dashboard that cross-references AI citation presence against actual Google click performance.
- Scrutinize AI share-of-voice metrics' underlying methodology before adopting as a core KPI; pair with citation-to-conversion data.
- Use Bing Webmaster Tools' Topics Portfolio to find queries where competitors are cited but the brand isn't, and prioritize content fixes against that gap list.
- Earmark budget for AI-visibility/citation-gap initiatives cautiously given multiple studies showing minimal traffic/conversion impact to date; set a defined proof-of-impact checkpoint.

## AI-Era Content Validation Workflow

- Identify decision gaps competitors/AI summaries haven't addressed and fill them with original, proprietary knowledge.
- Prove claims with evidence/data before publishing, especially on YMYL legal and investment guide content.
- Test writing precise, unambiguous 'technical manual' style passages on key guide/help pages to improve LLM parsing and citation accuracy.
- Structure flagship content as modular, self-contained answer blocks that remain accurate and credible when excerpted out of context.

## Audience Data Quality for AI Agents

- Audit first-party audience/segment data quality feeding any AI-driven personalization, targeting, or agent-facing tools.
- Treat audience/data hygiene as a prerequisite for AI visibility strategy, not just an ads/marketing concern.

## Canonical Tag Hygiene

- Run periodic canonical tag audits across all brand domains, especially syndicated content, partner integrations, and shared templates.
- For any statically-generated site or section, confirm canonicals, sitemaps, redirects, and 404 handling are manually implemented since CMS plugin automation won't apply.

## Content Distribution System

- Assign a named distribution owner to every major content asset at publish time.
- Build a repeatable 90-day post-publish checklist (outreach, syndication, internal linking, PR) aimed at earning backlinks and AI citations.
- Review underperforming older content against this checklist to re-ignite distribution rather than only focusing on new launches.
- Extend outreach/monitoring to Reddit given its growing role as a PR, community, and AI-citation source; evaluate standing up a branded subreddit as part of this strategy.

## Content Strategy — Listicles & Comparisons

- Audit existing comparison/listicle content for genuine reader utility (clear criteria, honest tradeoffs, real recommendations) rather than keyword-driven structure alone.
- Prioritize trust-building elements (methodology transparency, first-hand testing notes) on comparison pages targeted at commercial/buyer-intent queries.

## Core Web Vitals — Soft Navigation

- Identify SPA/dashboard-style sections on brand sites that use client-side route changes without full page loads.
- Monitor CrUX experimental soft navigation metrics for these sections ahead of expected Search Console integration.

## Custom 404 Pages

- Audit brand 404 pages for helpful navigation, search functionality, and links to popular/related content rather than default server-generated pages.
- Treat 404 page UX as a conversion/retention lever, not an SEO ranking concern, since Google confirms 404s aren't a ranking threat.

## Enterprise SEO Process Silos

- Audit cross-team ownership gaps for technical SEO changes spanning multiple brand sites/subdomains to catch silo-driven inconsistencies.
- Standardize implementation checklists (schema, redirects, metadata) across brand properties so fixes on one site don't get missed on others.
- Build a scale-safe rollout process (templated changes, staged QA) before pushing SEO fixes across large or multi-brand site portfolios.

## Feed / Rendered Listing Data Integrity

- Audit live listing/product SERP presentation (prices, sale badges, images) against current source feed data to catch Google's cached/derived data mismatches.
- Set a recurring spot-check process for high-value listing pages comparing rendered search results to the actual feed.
- Throttle high-churn feed fields (price, availability) to avoid more-than-daily changes now that Merchant Center may disapprove products on mismatch detection.
- Deprioritize emergency fixes for low-quality listing images since poor image quality alone no longer blocks Search/Ads inclusion.

## Google Algorithm Update

- Check GSC Performance and Manual Actions reports across all brand properties when unconfirmed ranking volatility/chatter surfaces; don't assume an official core update without confirmation.
- Audit syndicated, partner, affiliate, and UGC content for compliance as Google's spam-enforcement scope expands to new UGC-adjacent platforms/tools.
- Only attribute ranking drops to a spam update or volatility event if policy-violating practices or confirmed lasting loss are present.
- When post-migration indexing stalls or old URLs reappear, evaluate underlying site quality/originality and expect migration processing to legitimately take 4+ months before escalating.

## Google Indexing API

- Re-review Google's recently updated Indexing API documentation (approval process, sitemap guidance, and quota details) before planning any dependent listing-freshness workflows.
- Do not build listing-freshness strategy dependent on timely or predictable Indexing API behavior given documentation churn and historical approval delays.

## Google Search Profile Badges

- Keep Search Profile badge widgets live on named-author pages for mobile, since the Follow button was removed from desktop results but remains on mobile.
- Delay heavier investment in desktop-specific Search Profile UX until the feature stabilizes.
- Pair with the lowered 10K-follower eligibility threshold to capture follow-based visibility as traffic patterns shift.

## GSC Reporting

- Flag anomalous indexing count drops and broken date-picker behavior as likely reporting bugs before launching technical audits.
- Don't treat the Links report as a complete inventory — it's a sampled view (including spammy links); supplement with third-party backlink tools for toxic-link audits.
- Use the multi-select country filter and Multimodal vs Text-based filter in Performance reports to build grouped regional views and baseline image-search contribution on listing-photo/infographic-heavy pages.
- Track Preferred Source subscriber-count emails as a new baseline KPI, and re-baseline desktop vs. mobile CTR trends now that the prior logging error has been resolved.
- Don't over-react to 'Couldn't fetch' sitemap errors alone; verify via URL inspection/live test since the error may not reflect Google's actual fetch ability.

## Helpful Content Guidelines — Main Content & Fake Authors

- Audit key templates against Google's clarified Main Content definition to ensure substantive, original content (not boilerplate/ads/nav) is the clear primary focus.
- Verify all published author bios/profiles are real, accurate, and not fabricated or templated placeholders.
- Tie this audit into existing E-E-A-T and author schema initiatives given increased scrutiny and expanded spam enforcement.

## Hreflang & International Pages

- Audit international/market pages for unique local value (pricing, legal terms, regional specifics) rather than relying on hreflang tagging to carry ranking signal.
- Check GSC indexing status of hreflang-alternate URLs since Google may leave referenced market pages unindexed.
- Prioritize localized differentiation on market pages likely to surface in AI Mode/AI Overviews answers.

## Image Formats / JPEG XL

- Avoid switching primary listing/blog/hero images to JPEG XL — Google reconfirmed Images and Discover previews still don't support the format.
- Audit any already-adopted JPEG XL images for broken previews in Google Images/Discover and fall back to supported formats (JPEG, WebP, AVIF) where needed.

## Large Site Indexing / Aggregator Pages

- If any brand property functions as a large listing/directory/aggregator site, audit the ratio of crawled-to-indexed pages rather than assuming crawl volume signals health.
- Consolidate, de-duplicate, or add unique value to thin aggregator-style pages to improve indexation rates.
- Segment large-site page types by revenue contribution (not just traffic) to prioritize which thin pages to fix, merge, or cut.
- Confirm homepage and key hub pages carry sufficiently unique, substantive content to avoid aggregator-style indexing suppression.

## Local SEO / GBP

- Use GBP post view counts (Search + Maps, 18-month lookback) to benchmark and optimize post content types, and increase posting cadence given Google Posts' higher placement in the local knowledge panel.
- Review all GBP post and listing content against the updated advertising/solicitation prohibited-content policy to avoid suspension risk.
- Check GBP listings for auto-added Facebook Messenger (m.me) links and verify they route to active, monitored pages.
- Review access to and quality of auto-replies in the expanding GBP AI-powered messaging feature before enabling broadly.
- Prepare EIN and privacy policy documentation in advance for any GBP listing updates, given Google's newly observed verification requests.

## Local Service Ads Lead Reporting

- Review updated LSA 'how leads work' documentation against current billing/dispute practices for any brand running Local Service Ads.
- Re-train local ops/support staff on what now qualifies as a billable phone lead and how lead-quality credits are handled.
- Update LSA creative/profile checklists now that Featured Professionals badges are being removed and headshots are optional with no serving impact.
- Audit campaign reporting for ad-unit misattribution given advertiser confusion distinguishing Local Service Ads from other local ad formats.

## Multimodal Image SEO

- Audit key listing/blog images for crawlability, descriptive alt text, structured data, and accessible file formats.
- Spot-check Google Images/multimodal visibility via GSC for image-heavy page templates and fix technical blockers limiting inclusion.

## PDF SEO / AEO

- Audit brand PDFs for text-based (not scanned-image) content to ensure crawlability and indexing.
- Verify links and images inside key PDFs are being processed/indexed correctly via URL inspection.
- Consider republishing high-value PDF guides as HTML pages to improve AI Mode/AEO citation potential and ranking flexibility.

## Platform Visibility Reporting Expansion

- Evaluate whether brand presence on social discovery platforms (including Reddit) should be tracked alongside traditional organic visibility metrics.
- Review Search Console's platform property options as they expand to include non-website properties.

## Product Page Copy for AI Agents

- Audit pricing/feature pages to ensure differentiator messaging exists in prose, not just schema/feed data, so AI shopping agents don't default to generic summaries.
- Verify policy/FAQ content (cancellation, billing, trial terms) is plainly readable in page text, since real-world agent testing shows agents fail transactional questions even on 'agent-ready' stores.

## Publisher Organic Traffic Decline

- Prioritize investment in direct channels (email, app, community) to hedge against accelerating YoY organic search/Discover referral decline.
- Benchmark visibility trend against vertical-wide SaaS/publisher decline using multi-year, multi-market data; distinguish share decline from absolute volume decline and from AI-attributable loss before messaging stakeholders.
- Track revenue-per-visit alongside traffic metrics, per case studies showing traffic collapse can coincide with revenue growth when other channels and conversion quality improve.
- Review content cadence and freshness mix against Discover's freshness-algorithm factors and prepare for further Discover volatility.

## Rank Tracking Reliability

- Cross-check any third-party rank-tracking tool output against GSC Performance data given ongoing scraper-blocking and reported result 'poisoning'/fake data aimed at rank-tracking bots.
- Request vendor documentation on how they detect and handle suspect/flagged results, what reprocessing looks like, and what's surfaced to customers during a flag.
- Build contingency/redundancy into visibility reporting workflows rather than relying on a single rank-tracking vendor.
- Shift core reporting toward brand visibility, AI citations, and revenue metrics given confirmed rank-tracking outages exposed single-metric reporting risk.

## Reddit Brand Communities

- Evaluate standing up a branded subreddit focused on useful, recurring answers (rental/property management Q&A) rather than promotional content.
- Coordinate any subreddit strategy with existing Reddit monitoring/outreach workflows under the content distribution program.

## Referral/Link Spam Audits

- Audit backlink profiles for toxic referring domains across all brand properties on a recurring basis, not just at migration/recovery time, using third-party tools since GSC's Links report is sampled and incomplete.
- Cross-check GA4 referral traffic for spam/ghost referrer domains and filter them from reporting to avoid skewed channel analysis.

## Schema — AI Visibility Mistakes

- Audit schema across key templates for completeness and content-match accuracy (not just validator pass/fail), since mismatches actively hurt AI visibility.
- Prioritize fixing missing/outdated/mismatched structured data on pages targeted for AEO/AI citation.

## Schema — Review Snippets

- Check whether any health/safety-adjacent brand content falls into categories where Google may be suppressing review rich snippets despite valid markup.
- Avoid over-investing in review schema for affected content verticals until Google clarifies scope of the change.

## Schema — Video Structured Data

- Add creator/author properties to VideoObject schema on any video content to strengthen E-E-A-T signals.
- Coordinate with Search Profile badge rollout for named authors/creators across video and article content.
- Review emerging AI-search-specific video optimization guidance for applicability to schema and on-page video content strategy.

## Static Site SEO Gaps

- Audit any static-site-generator-based brand property or microsite for manually-required canonicals, sitemaps, redirects, metadata, schema, and 404 handling that CMS plugins normally automate.
- Weigh Astro-style islands architecture for any new lightweight/microsite builds where CWV performance is a priority.

## Technical SEO Process

- Review internal technical SEO audit workflows for prioritization and follow-through gaps, not just checklist/tooling coverage.
- Assign clear ownership and remediation SLAs for recurring audit findings across brand sites, and audit for silo/scale failure patterns common in multi-brand/enterprise setups.
- Apply scientific-method discipline (clear hypothesis, control group, adequate sample size, confounder checks) when designing and interpreting SEO experiments.

## UGC Fresh Data Program

- Google is accepting applications for its UGC data pipeline (separate from crawling) for forums/social platforms — review eligibility criteria and apply if any brand forum, reviews, or community section qualifies.
- Audit UGC sections for freshness, structure, and update cadence to strengthen eligibility for this or similar data-sharing arrangements.

## URL Syntax Handling

- Standardize on one form (raw vs. percent-encoded) for bracket characters in URLs across links, canonical tags, and sitemaps, since Google crawls the two forms as separate URLs.
- Audit any brand URLs containing square brackets (e.g., faceted/filter parameters) for indexing anomalies and duplicate-URL issues stemming from mixed encoding.
- Avoid introducing square brackets into new URL structures until consistent handling is verified.

## WordPress Platform Maintenance

- Apply WordPress 7.1.4 immediately across all WordPress-based brand properties and verify the updater functions correctly post-patch.
- Audit for and remove/patch UpdraftPlus immediately given an active backdoor-attack breach affecting 3M+ installs.
- Confirm all WordPress-based brand properties and hosts have applied the PHP Core security patch and are on the latest patched core version, including Jetpack's recent accessibility/security update.
- Ensure any planned maintenance downtime serves a true 503 (configured outside PHP, e.g., at web server/CDN level) with robots.txt still reachable, to avoid Google dropping URLs after prolonged server errors.
- Immediately audit for and patch the All In One SEO (AIOSEO) plugin if in use, given unauthenticated-attacker vulnerabilities.
