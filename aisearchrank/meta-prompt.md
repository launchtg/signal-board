# AISearchRank — Build Meta Prompt
## For Loveable or Claude Code

---

## PROMPT

Build a full-stack web application called **AISearchRank** — a B2B micro SaaS dashboard that tracks brand visibility across AI search engines (ChatGPT, Perplexity, Claude, Gemini). Users monitor how often their brand appears when people ask AI chatbots questions relevant to their industry.

---

## TECH STACK (Required)

- **Framework:** Next.js 14+ (App Router)
- **Styling:** Tailwind CSS
- **Database:** Supabase (PostgreSQL)
- **Auth:** Supabase Auth (email + password, magic link)
- **Payments:** Stripe (subscription billing)
- **Email:** Resend (transactional alerts)
- **Charts:** Recharts
- **Hosting:** Vercel
- **Font:** Inter (sans), Playfair Display (display), JetBrains Mono (mono)

---

## DESIGN SYSTEM (Required — follow exactly)

### Colors
```
--bg: #0B3D2E
--bg-surface: #0D4A36
--bg-card: #10573F
--bg-card-hover: #146B4D
--border: #1A7A58
--text: #F5F0E8
--text-muted: #A8C4B8
--text-dim: #6B9E88
--primary: #E8862A
--primary-bright: #F0A050
--deep-green: #0B3D2E
--pine-green: #1A5C45
--warm-ivory: #F5F0E8
--navy: #1B2A4A
--slate: #64748B
--destructive: #ef4444
--warning: #f59e0b
--success: #22c55e
--info: #5BA4D9
```

### Card Style
- Cards use **Warm Ivory (#F5F0E8)** background with **Deep Green (#0B3D2E)** text
- Card borders: #E0D9CE
- Card hover: #EDE8DF with orange border
- This creates contrast against the dark green page background

### Typography
- Headings: Playfair Display, font-weight 600-700
- Body: Inter, font-weight 400-600
- Data/numbers/badges: JetBrains Mono, font-weight 400-500

### Design Aesthetic
- Dark green background, cream cards
- LTG brand (Launch Technology Group)
- Information-dense, operational
- Linear/Vercel aesthetic
- Green checkmarks for "mentioned", red X for "not mentioned"
- Orange (#E8862A) for primary actions and accents

---

## DATABASE SCHEMA

### `profiles`
- id (uuid, FK to auth.users)
- full_name (text)
- company (text)
- plan (text: 'trial', 'starter', 'pro', 'agency')
- stripe_customer_id (text, nullable)
- created_at (timestamptz)

### `brands`
- id (uuid, PK)
- user_id (uuid, FK to profiles)
- name (text) — e.g. "HubSpot"
- domain (text, nullable) — e.g. "hubspot.com"
- is_competitor (boolean, default false)
- created_at (timestamptz)

### `queries`
- id (uuid, PK)
- user_id (uuid, FK to profiles)
- text (text) — e.g. "best CRM for small businesses"
- category (text, nullable) — e.g. "CRM", "Marketing"
- active (boolean, default true)
- created_at (timestamptz)

### `scans`
- id (uuid, PK)
- query_id (uuid, FK to queries)
- platform (text: 'chatgpt', 'perplexity', 'claude', 'gemini')
- brand_id (uuid, FK to brands)
- mentioned (boolean)
- position (integer, nullable) — position in response (1=first mention)
- context_snippet (text, nullable) — surrounding text of mention
- full_response (text) — complete AI response
- scanned_at (timestamptz)

### `scores`
- id (uuid, PK)
- user_id (uuid, FK to profiles)
- platform (text, nullable) — null = overall
- score (integer, 0-100)
- date (date)
- created_at (timestamptz)

### `alerts`
- id (uuid, PK)
- user_id (uuid, FK to profiles)
- type (text: 'score_drop', 'competitor_overtake', 'new_mention', 'weekly_digest')
- message (text)
- is_read (boolean, default false)
- sent_at (timestamptz)

### Row Level Security
- Enable RLS on all tables
- Users can only read/write their own data
- Scans readable by the query owner

---

## PAGE STRUCTURE

### `/login`
- Email + password login, magic link option
- Dark themed, centered card
- "Start free trial" link

### `/signup`
- Email, password, full name, company
- Auto-start 7-day trial

### `/onboarding`
- Step 1: Enter your brand name + domain
- Step 2: Add 2-3 competitor brand names
- Step 3: Add 10-20 search queries (with suggestions based on industry)
- Step 4: Select alert preferences
- Auto-triggers first scan on completion

### `/dashboard` (main page, requires auth)

**Layout:**
- Left sidebar (240px, collapsible):
  - AISearchRank logo + name at top
  - Nav: Dashboard, Queries, Competitors, Alerts, Settings
  - Active item: orange left border + subtle bg
  - Brand selector dropdown at bottom

- Main content:
  - Stats row (4 cream cards):
    - AI Visibility Score (large number, 0-100, with trend arrow up/down)
    - Mentions This Week (count)
    - Competitor Gap (+/- vs top competitor)
    - Platforms Tracked (count with platform icons)

  - Trend Chart (Recharts):
    - 30-day line chart
    - One line per platform (ChatGPT=blue, Perplexity=purple, Claude=orange, Gemini=green)
    - Overall score as dashed line
    - Cream card background
    - Y-axis: 0-100, X-axis: dates

  - Query Table (cream card):
    - Columns: Query, ChatGPT, Perplexity, Claude, Gemini, Score
    - Each platform column shows green checkmark or red X
    - Score column shows percentage (mentions/platforms)
    - Sortable by score
    - Click row to open Query Detail panel
    - Search/filter bar at top

- Right detail panel (slides in on row click, 400px):
  - Query text at top
  - Platform tabs (ChatGPT | Perplexity | Claude | Gemini)
  - Full AI response rendered as text
  - Brand mentions highlighted in orange
  - Competitor mentions highlighted in blue
  - "Last scanned: 2h ago" timestamp
  - "Rescan Now" button

### `/queries`
- List of all monitored queries
- Add new query (text input + category dropdown)
- Bulk add (paste multiple queries)
- Toggle active/inactive
- Delete with confirmation
- Category filter

### `/competitors`
- List of tracked competitor brands
- Add/remove competitors
- Side-by-side visibility score comparison
- Per-query comparison table

### `/alerts`
- Alert history list
- Filter by type
- Mark as read
- Alert preferences toggle

### `/settings`
- Profile info
- Email preferences (alert frequency)
- Scan schedule preference
- Plan & billing (Stripe portal link)
- API keys (for Pro/Agency)
- Export data (CSV)

---

## API ROUTES

### `/api/scans/run`
- POST: Trigger a scan for a specific query across all platforms
- Secured with CRON_SECRET or user auth
- Calls each AI platform API, parses for brand mentions, stores results

### `/api/scans`
- GET: List scan results with filters (query_id, platform, date range)

### `/api/scores`
- GET: Get visibility scores over time (user_id, date range, platform)

### `/api/queries`
- GET/POST/PATCH/DELETE: CRUD for monitored queries

### `/api/brands`
- GET/POST/DELETE: CRUD for brands and competitors

### `/api/alerts`
- GET: List alerts
- PATCH: Mark as read

### `/api/cron/daily-scan`
- POST: Triggered by Vercel Cron at 6am ET
- Runs all active queries for all users
- Calculates daily scores
- Checks alert conditions
- Sends alerts via Resend

### `/api/webhooks/stripe`
- POST: Handle Stripe subscription events

---

## AI PLATFORM SCANNING LOGIC

For each query + platform combination:

```typescript
// Pseudocode for scanning
async function scanQuery(query: string, brandName: string, platform: string) {
  // 1. Submit query to AI platform
  const response = await callAIPlatform(platform, query);

  // 2. Check if brand is mentioned
  const mentioned = response.toLowerCase().includes(brandName.toLowerCase());

  // 3. Find position (which mention number)
  const position = findMentionPosition(response, brandName);

  // 4. Extract context snippet (50 chars before and after)
  const context = extractContext(response, brandName, 50);

  // 5. Store result
  await supabase.from('scans').insert({
    query_id, platform, brand_id, mentioned, position, context_snippet: context, full_response: response
  });
}
```

Platform API calls:
- **ChatGPT:** OpenAI Chat Completions API with gpt-4o-mini, system prompt: "Answer the following question naturally"
- **Perplexity:** Perplexity API with sonar model
- **Claude:** Anthropic Messages API with claude-3-haiku
- **Gemini:** Google Generative AI API with gemini-1.5-flash

---

## SEED DATA

Generate realistic demo data:
- Brand: "Acme CRM" with competitors "HubSpot", "Salesforce", "Pipedrive"
- 20 queries about CRM, sales tools, marketing automation
- 30 days of scan history with realistic mention patterns
- Visibility score trending upward from 45 to 68

---

## COMPONENTS TO BUILD

1. `Sidebar` — navigation with brand selector
2. `StatsCard` — metric card (cream bg, dark text)
3. `VisibilityChart` — Recharts line chart with platform lines
4. `QueryTable` — sortable table with checkmark/X columns
5. `QueryDetailPanel` — slide-in panel with tabbed AI responses
6. `MentionHighlighter` — highlights brand mentions in AI response text
7. `PlatformBadge` — colored badge for each AI platform
8. `ScoreBadge` — colored score indicator (green >70, yellow 40-70, red <40)
9. `AlertList` — alert history component
10. `OnboardingWizard` — multi-step setup flow
11. `CompetitorComparison` — side-by-side score bars

---

## IMPORTANT IMPLEMENTATION NOTES

1. Use cheapest AI models for scanning (gpt-4o-mini, haiku, sonar-small, flash)
2. Cache full AI responses — don't re-scan same query within 24h
3. Implement proper loading skeletons
4. Recharts should use cream card background with dark green grid lines
5. Green checkmark: #22c55e, Red X: #ef4444
6. Mobile responsive: sidebar collapses, detail panel goes full-screen
7. Use Supabase Row Level Security
8. Stripe Checkout for subscriptions
9. Debounce search (300ms)
10. Platform icons: use simple colored dots (blue=ChatGPT, purple=Perplexity, orange=Claude, green=Gemini)

---

## DO NOT

- Add a light mode
- Use any UI component library (build with Tailwind from scratch)
- Use any ORM
- Add social auth
- Over-engineer — scanning logic can be simple string matching for MVP
- Add real-time scanning in MVP (daily batch is fine)
