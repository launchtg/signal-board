# LicenseWatch — Product Requirements Document

## 1. Executive Summary

LicenseWatch is a micro SaaS application that monitors state business license filings daily and alerts subscribers when new businesses register in their target categories and geographies. It gives insurance agents, B2B sales teams, accountants, and payroll companies first-mover advantage on new business leads.

## 2. Problem Statement

Insurance agents, accountants, POS companies, payroll providers, and B2B sales reps need to reach newly registered businesses before competitors. Currently they:

- Manually check state Secretary of State websites weekly (30-60 min per state)
- Navigate clunky, inconsistent government portals
- Copy filing data into spreadsheets or CRMs by hand
- Miss new filings because there's no alert system
- Lose deals to competitors who found the business first

There is no affordable, dedicated tool for this. Existing data providers (InfoUSA, D&B) charge enterprise prices and deliver stale data.

## 3. Target Users

### Primary
- Insurance agents (commercial lines — GL, WC, BOP)
- B2B sales reps targeting new businesses
- Accountants and bookkeepers seeking new clients
- Payroll companies (ADP alternatives, local providers)
- POS/merchant services sales reps

### Secondary
- Commercial real estate agents
- Business attorneys
- Marketing agencies targeting startups
- Franchise development teams

## 4. Core Value Proposition

"Know about new businesses before anyone else. Get alerted the day they file."

- First-mover lead generation
- Zero manual checking
- Enriched contact data ready for outreach
- Direct CRM integration

## 5. Core Features (MVP)

### 5.1 Watchlist Configuration
- Select target states (start with 5-10 states)
- Select business categories (LLC, Corp, DBA, Nonprofit)
- Set industry keywords (e.g., "restaurant", "construction", "tech")
- Set geography filters (county, city, zip when available)

### 5.2 Daily Filing Monitor
- Automated daily scraping of state SOS websites
- Parse: business name, type, filing date, registered agent, address
- Store in database with dedup logic
- Run against user watchlists for matches

### 5.3 Alert System
- Email digest: daily summary of matched filings
- Real-time alerts: instant notification for high-priority matches
- In-app notification center
- Configurable alert frequency (instant, daily, weekly)

### 5.4 Dashboard
- Today's new filings count
- Watchlist match count
- Alerts sent
- States monitored
- Filing table with search, sort, filter
- Match score indicator

### 5.5 Filing Detail View
- Full filing information
- Registered agent details
- Business address
- Filing date and type
- Enrichment data (when available): phone, email, website, LinkedIn

### 5.6 Contact Enrichment (Basic)
- Auto-lookup business website from name
- Extract contact email from website
- Phone number lookup
- LinkedIn company page match

### 5.7 Export & CRM
- CSV export of matched filings
- "Send to CRM" action (webhook-based)
- Copy contact info to clipboard
- Bulk export watchlist matches

## 6. Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js (App Router) |
| Styling | Tailwind CSS |
| Backend | Next.js API routes + Python scraper services |
| Database | Supabase (PostgreSQL) |
| Auth | Supabase Auth |
| Scraping | Apify actors + custom Python scrapers |
| Enrichment | Apollo API, Hunter.io, Clearbit |
| Email | Resend or Postmark |
| Hosting | Vercel |
| Cron Jobs | Vercel Cron or Supabase pg_cron |
| Payments | Stripe |

## 7. Data Architecture

### Tables
- `filings` — raw business license filing records
- `states` — supported states with scraper config
- `watchlists` — user-defined monitoring rules
- `matches` — filings that match user watchlists
- `alerts` — sent alert log
- `enrichments` — cached contact enrichment data
- `users` — auth and subscription info

### Key Indexes
- filings: (state, filed_date, business_type)
- matches: (user_id, created_at, is_read)
- watchlists: (user_id, state, active)

## 8. Scraping Strategy

### Phase 1 (MVP): 5 States
Start with states that have accessible, structured SOS websites:
1. Texas — https://www.sos.state.tx.us
2. California — https://bizfileonline.sos.ca.gov
3. Florida — https://dos.fl.gov/sunbiz
4. New York — https://www.dos.ny.gov/corps
5. Delaware — https://icis.corp.delaware.gov

### Approach
- Apify scheduled actors running daily at 6am ET
- Parse new filings from previous day
- Normalize data into standard schema
- Store in Supabase with state + date composite key
- Run watchlist matching after each scrape completes

### Rate Limiting & Ethics
- Respect robots.txt
- Rate limit requests (1 req/sec max)
- Cache aggressively
- Use public data only

## 9. UI/UX Requirements

### Design Direction
- Dark theme (LTG brand: #0a0a12 bg, #7CB800 primary, #CCFF00 accent)
- Inter font family
- JetBrains Mono for data/numbers
- Information-dense, operational feel
- Linear/Vercel aesthetic
- High data density with clean hierarchy

### Layout
- Left sidebar: navigation
- Main panel: filing table + stats
- Right panel: filing detail + enrichment (collapsible)
- Top bar: search, filters, state selector

### Key Interactions
- Click filing row → detail panel opens
- Star filing → save to favorites
- "Send to CRM" button on detail panel
- Bulk select → export CSV
- Toggle between "All Filings" and "My Matches"

## 10. Pricing

| Plan | Price | Includes |
|------|-------|----------|
| Starter | $39/mo | 1 state, 3 watchlists, daily digest |
| Pro | $79/mo | 3 states, unlimited watchlists, real-time alerts, enrichment |
| Agency | $149/mo | All states, team seats, API access, CRM integration |

Free trial: 7 days, 1 state, limited results.

## 11. Success Metrics

### MVP Success
- Scraper reliably pulls daily filings from 5 states
- Watchlist matching works accurately
- Email alerts deliver on time
- User can find and export matched filings

### Product Success
- 50 paying users within 90 days
- <5% churn monthly
- Users report time savings of 2+ hours/week
- NPS > 40

## 12. Competitive Landscape

| Competitor | Price | Weakness |
|-----------|-------|----------|
| InfoUSA/Data.com | $500+/mo | Stale data, enterprise only |
| D&B (Dun & Bradstreet) | $300+/mo | Expensive, slow updates |
| Manual SOS checking | Free | 30-60 min/state/week, error-prone |
| BizBuySell alerts | Free | Only businesses for sale, not new filings |

LicenseWatch wins on: price, freshness, specificity, and alert speed.

## 13. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| State websites change structure | Monitoring + quick scraper updates |
| Rate limiting by state sites | Respectful scraping, caching, rotating IPs |
| Data accuracy | Cross-reference multiple sources, user reporting |
| Low initial state coverage | Start with highest-value states, expand based on demand |

## 14. Roadmap

### Phase 1 (MVP) — Weeks 1-2
- 5 state scrapers
- Watchlist system
- Daily email alerts
- Dashboard with filing table
- Stripe billing

### Phase 2 — Weeks 3-4
- Contact enrichment
- CRM webhooks
- 10 more states
- Filing detail panel with enrichment

### Phase 3 — Months 2-3
- All 50 states
- Team/agency features
- API access
- Advanced analytics (trending categories, geographic heatmaps)
- Slack/Teams integration
