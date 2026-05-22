# AISearchRank — Product Requirements Document

## 1. Executive Summary

AISearchRank is a micro SaaS dashboard that tracks how often your brand appears in AI-generated search results across ChatGPT, Perplexity, Claude, Gemini, and Google AI Overviews. It gives marketers, SEO teams, and agencies visibility into a channel that's rapidly replacing traditional search — with no affordable tool available today.

## 2. Problem Statement

Gartner predicts 25% of search will shift to AI chatbots by end of 2026. When someone asks ChatGPT "what's the best CRM for small businesses?" — does your brand appear? Most companies have zero visibility into this.

Currently:
- Marketers manually type queries into ChatGPT/Perplexity to check if their brand appears
- No systematic tracking, no historical data, no alerts
- Otterly.ai exists but charges $100+/mo — too expensive for SMBs
- No way to compare AI visibility vs competitors
- No way to track which queries mention you vs which don't

## 3. Target Users

### Primary
- Marketing managers at SaaS companies (50-500 employees)
- SEO agencies managing client visibility
- Founders tracking brand awareness
- Content marketers optimizing for AI discovery

### Secondary
- PR teams monitoring brand mentions in AI
- Product marketers tracking competitor positioning
- Affiliate marketers checking recommendation rankings

## 4. Core Value Proposition

"Know exactly where your brand appears — and doesn't — in AI search."

- Daily monitoring across 4+ AI platforms
- Competitor comparison
- Query-level visibility tracking
- Trend alerts when visibility changes

## 5. Core Features (MVP)

### 5.1 Brand Setup
- Enter your brand name and up to 3 competitor brands
- Add 20-50 search queries relevant to your industry
- Example queries: "best project management tool", "top CRM for agencies", "what email marketing platform should I use"
- System auto-suggests queries based on your industry

### 5.2 AI Platform Monitoring
Platforms monitored:
- **ChatGPT** (via OpenAI API — submit query, parse response)
- **Perplexity** (via Perplexity API)
- **Claude** (via Anthropic API)
- **Gemini** (via Google Gemini API)

For each query on each platform:
- Submit the query
- Parse the response for brand mentions
- Record: mentioned (yes/no), position in response, context snippet, competitor mentions
- Store with timestamp for trend tracking

### 5.3 Visibility Score
- Calculate an overall "AI Visibility Score" (0-100)
- Score = (queries where brand is mentioned / total queries) × 100
- Weighted by platform (ChatGPT weighted higher due to market share)
- Track score daily for trend line

### 5.4 Dashboard
- **Visibility Score** — large number with trend arrow
- **Mentions This Week** — count across all platforms
- **Competitor Gap** — your score vs top competitor
- **Platforms Tracked** — count
- **Trend Chart** — 30-day visibility score line chart, one line per platform
- **Query Table** — all monitored queries with per-platform mention status (checkmark/X)
- **Competitor Comparison** — side-by-side scores

### 5.5 Alerts
- Email alert when visibility score drops by >10%
- Alert when a competitor overtakes you on a key query
- Weekly digest with summary of changes
- Alert when a new query starts mentioning your brand

### 5.6 Query Explorer
- View the full AI-generated response for any query
- See exactly what was said about your brand
- See what was said about competitors
- Highlight brand mentions in context

## 6. Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 14 (App Router) |
| Styling | Tailwind CSS |
| Backend | Next.js API routes |
| Database | Supabase (PostgreSQL) |
| Auth | Supabase Auth |
| AI APIs | OpenAI, Anthropic, Perplexity, Google Gemini |
| Email | Resend |
| Cron | Vercel Cron |
| Payments | Stripe |
| Hosting | Vercel |
| Charts | Recharts |

## 7. Data Architecture

### Tables
- `brands` — user's brand and competitors (name, domain, user_id)
- `queries` — monitored search queries (text, category, user_id)
- `scans` — individual scan results (query_id, platform, mentioned, position, context_snippet, competitor_mentions, scanned_at)
- `scores` — daily aggregated visibility scores (user_id, platform, score, date)
- `alerts` — sent alert log (user_id, type, message, sent_at)
- `profiles` — user info, plan, stripe_customer_id

### Key Indexes
- scans: (query_id, platform, scanned_at)
- scores: (user_id, date)

## 8. Scanning Strategy

### Daily Scan Cycle
1. Vercel Cron triggers at 6am ET
2. For each user's queries (up to 50):
   - Submit to each platform API
   - Parse response for brand + competitor mentions
   - Store scan result
3. Calculate daily visibility score
4. Check alert conditions
5. Send alerts if triggered

### API Cost Management
- OpenAI: ~$0.01 per query (gpt-4o-mini for parsing)
- Anthropic: ~$0.01 per query (haiku for parsing)
- Perplexity: ~$0.005 per query
- Gemini: ~$0.005 per query
- 50 queries × 4 platforms = 200 API calls/day = ~$2-4/day per user
- At $29/mo pricing, margins are tight — use cheapest models for scanning

### Rate Limiting
- Stagger scans across the day to avoid API rate limits
- Cache responses for 24 hours
- Retry failed scans up to 3 times

## 9. UI/UX Requirements

### Design Direction
- LTG brand: Deep Green #0B3D2E, Launch Orange #E8862A, Warm Ivory #F5F0E8
- Cards on cream background for contrast
- Playfair Display for headings, Inter for body, JetBrains Mono for data
- Clean, information-dense dashboard
- Checkmarks (green) and X marks (red) for mention status

### Layout
- Left sidebar: Brand selector, navigation
- Main panel: Score, chart, query table
- Right panel: Query detail view (collapsible)

## 10. Pricing

| Plan | Price | Includes |
|------|-------|----------|
| Starter | $29/mo | 1 brand, 2 competitors, 20 queries, daily scans, email alerts |
| Pro | $59/mo | 3 brands, 5 competitors, 50 queries, hourly scans, Slack alerts |
| Agency | $149/mo | 10 brands, unlimited competitors, 200 queries, API access |

Free trial: 7 days, 1 brand, 10 queries.

## 11. Competitive Landscape

| Competitor | Price | Weakness |
|-----------|-------|----------|
| Otterly.ai | $100+/mo | Too expensive for SMBs |
| Semrush AI features | $130+/mo | Bundled into larger platform, not focused |
| Manual checking | Free | No tracking, no trends, no alerts |
| Google Alerts | Free | Doesn't cover AI chatbots at all |

AISearchRank wins on: price ($29 vs $100+), focus (AI search only), and simplicity.

## 12. Success Metrics

### MVP Success
- Scans run reliably across 4 platforms daily
- Visibility score tracks accurately
- Dashboard loads fast with 30 days of data
- Alerts fire correctly

### Product Success
- 100 paying users within 90 days
- <5% monthly churn
- Users check dashboard 3+ times/week
- NPS > 50

## 13. Roadmap

### Phase 1 (MVP) — Week 1-2
- 4 platform scanning (ChatGPT, Perplexity, Claude, Gemini)
- Visibility score + trend chart
- Query table with mention status
- Daily email alerts
- Stripe billing

### Phase 2 — Week 3-4
- Query Explorer (see full AI responses)
- Competitor comparison view
- Query auto-suggestions
- Slack integration

### Phase 3 — Month 2-3
- Google AI Overviews monitoring
- Bing Copilot monitoring
- Historical trend analysis
- API access for agencies
- White-label reports
