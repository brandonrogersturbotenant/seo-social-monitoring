# SEO Social Monitoring

Automated weekday SEO morning briefings. Crawls RSS feeds from top SEO sources, compares against a running knowledge brain, and emails actionable insights by 8 AM Mountain Time.

## How it works

```
6:00 AM MT (weekdays)  →  Fetch RSS feeds (last 24h)
                       →  Load brain, skip already-processed URLs
                       →  Claude summarizes + deduplicates against brain
                       →  Update brain repository
                       →  Email briefing via Resend
```

## Setup

### 1. Add API keys as GitHub Secrets

Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

| Secret | Value |
|--------|-------|
| `ANTHROPIC_API_KEY` | Your Claude API key (`sk-ant-...`) |
| `ANTHROPIC_WORKSPACE_ID` | Workspace ID (`wrkspc_...`) — required for non-workspace-scoped keys |
| `RESEND_API_KEY` | Your Resend API key (`re_...`) |
| `RESEND_FROM` | Sender email (see note below) |
| `EMAIL_TO` | `brandon.rogers@turbotenant.com` |

**About `ANTHROPIC_WORKSPACE_ID`:** In [Anthropic Console](https://console.anthropic.com) → Settings → Workspaces, open your workspace and copy the ID (starts with `wrkspc_`). Or create an API key that is scoped to a specific workspace so this secret is not needed.

**About `RESEND_FROM`:** For testing, use `onboarding@resend.dev` (Resend's sandbox sender). For production, verify a domain in [Resend](https://resend.com/domains) (e.g. `turbotenant.com`) and use something like `seo-brief@turbotenant.com`.

### 2. Test locally (optional)

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Copy and fill in your keys
cp .env.example .env
# Edit .env with your API keys

# Run manually
python -m src.main
```

### 3. Test via GitHub Actions

After adding secrets, go to **Actions** → **SEO Morning Brief** → **Run workflow** to trigger a manual test run.

### 4. Automatic schedule

Runs every weekday at **6:00 AM Mountain Time**. Email typically arrives within a few minutes.

## Managing sources

Edit `config/sources.yaml` to add or remove RSS feeds, creators, or brands. Commit and push — the next run picks up changes automatically.

```yaml
rss_feeds:
  - name: New Source
    url: https://example.com/feed/
```

## The brain

- `data/brain.json` — structured knowledge store (topics, bullets, processed URLs)
- `brain/LEARNINGS.md` — human-readable version, auto-generated

The brain grows over time. Each morning Claude checks new posts against existing topics before adding insights, so you don't get duplicate coverage.

## Brands in scope

turbotenant.com, tenantcloud.com, rentler.com, ziprent.com, ipropertymanagement.com, reihub.net

## Project structure

```
config/sources.yaml     ← your feed list and settings
data/brain.json         ← knowledge repository
brain/LEARNINGS.md      ← readable brain export
src/
  fetcher.py            ← RSS ingestion
  summarizer.py         ← Claude analysis
  brain.py              ← brain read/write/dedup
  emailer.py            ← Resend delivery
  main.py               ← pipeline orchestrator
.github/workflows/      ← weekday cron schedule
```
