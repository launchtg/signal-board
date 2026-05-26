# LicenseWatch — Build Meta Prompt
## For Loveable or Claude Code

---

## PROMPT

Build a full-stack web application called **LicenseWatch** — a B2B micro SaaS dashboard that monitors new state business license filings and alerts users when new businesses register in their target categories and geographies.

---

## TECH STACK (Required)

- **Framework:** Next.js 14+ (App Router)
- **Styling:** Tailwind CSS
- **Database:** Supabase (PostgreSQL)
- **Auth:** Supabase Auth (email + password, magic link)
- **Payments:** Stripe (subscription billing)
- **Email:** Resend (transactional alerts)
- **Hosting:** Vercel
- **Font:** Inter (sans), JetBrains Mono (monospace/data)

---

## DESIGN SYSTEM (Required — follow exactly)

### Colors
```
--bg: #0a0a12
--bg-surface: #12121c
--bg-card: #1a1a28
--bg-card-hover: #222234
--border: #2a2a3c
--text: #e8e8f0
--text-muted: #6b6b80
--text-dim: #4a4a5c
--primary: #7CB800
--primary-bright: #CCFF00
--destructive: #ef4444
--warning: #f59e0b
--success: #22c55e
--info: #3b82f6
```

### Typography
- Headings: Inter, font-weight 600-700, letter-spacing -0.02em
- Body: Inter, font-weight 400
- Data/numbers/badges: JetBrains Mono, font-weight 400-500
- Font sizes: 0.7rem (badges) → 1.125rem (page titles)

### Border Radius
- Small: 0.25rem
- Medium: 0.5rem
- Large: 0.75rem
- XL: 1rem

### Design Aesthetic
- Dark theme ONLY (no light mode)
- Linear/Vercel/Raycast aesthetic
- High information density
- Subtle borders, no heavy shadows
- Cards with 1px borders (#2a2a3c)
- Lime green (#7CB800) for primary actions, active states, and accents
- Electric lime (#CCFF00) sparingly for highlights and badges
- Glassmorphism: none. Clean flat surfaces only.

---

## DATABASE SCHEMA

Create these Supabase tables:

### `profiles`
- id (uuid, FK to auth.users)
- full_name (text)
- company (text)
- plan (text: 'trial', 'starter', 'pro', 'agency')
- stripe_customer_id (text, nullable)
- created_at (timestamptz)

### `watchlists`
- id (uuid, PK)
- user_id (uuid, FK to profiles)
- name (text)
- states (text[]) — array of 2-letter state codes
- business_types (text[]) — ['LLC', 'CORP', 'DBA', 'NONPROFIT']
- keywords (text[]) — industry keywords
- alert_frequency (text: 'instant', 'daily', 'weekly')
- active (boolean, default true)
- created_at (timestamptz)

### `filings`
- id (uuid, PK)
- state (text, 2-letter code)
- business_name (text)
- business_type (text)
- filing_date (date)
- registered_agent (text, nullable)
- address (text, nullable)
- city (text, nullable)
- county (text, nullable)
- zip (text, nullable)
- category (text, nullable)
- raw_data (jsonb)
- source_url (text)
- created_at (timestamptz)

### `matches`
- id (uuid, PK)
- user_id (uuid, FK to profiles)
- watchlist_id (uuid, FK to watchlists)
- filing_id (uuid, FK to filings)
- match_score (integer, 0-100)
- is_read (boolean, default false)
- is_starred (boolean, default false)
- created_at (timestamptz)

### `enrichments`
- id (uuid, PK)
- filing_id (uuid, FK to filings)
- website (text, nullable)
- email (text, nullable)
- phone (text, nullable)
- linkedin_url (text, nullable)
- enriched_at (timestamptz)

### `alerts`
- id (uuid, PK)
- user_id (uuid, FK to profiles)
- match_id (uuid, FK to matches)
- channel (text: 'email', 'in_app')
- sent_at (timestamptz)

### Row Level Security
- Enable RLS on all tables
- Users can only read/write their own watchlists, matches, alerts
- Filings and enrichments are readable by all authenticated users

---

## PAGE STRUCTURE

### `/login`
- Email + password login
- Magic link option
- "Start free trial" link
- Dark themed, centered card

### `/signup`
- Email, password, full name, company
- Auto-start 7-day trial
- Redirect to onboarding

### `/onboarding`
- Step 1: Select your states (checkboxes for available states)
- Step 2: Select business types (LLC, Corp, DBA, Nonprofit)
- Step 3: Add industry keywords
- Step 4: Set alert frequency
- Creates first watchlist automatically

### `/dashboard` (main page, requires auth)

**Layout:**
- Left sidebar (240px, collapsible):
  - LicenseWatch logo + name at top
  - Nav: Dashboard, Alerts, Watchlists, States, Settings
  - Active item has lime green left border + subtle bg highlight
  - User avatar + plan badge at bottom

- Top bar:
  - Search input (search filings by business name)
  - State dropdown filter
  - Date range picker
  - Business type filter
  - Toggle: "All Filings" / "My Matches"

- Main content:
  - Stats row (4 cards):
    - New Filings Today (number)
    - Your Watchlist Matches (number, lime green)
    - Alerts Sent (number)
    - States Monitored (number)
  - Filings table:
    - Columns: Star, Business Name, Type, State, Filed Date, Category, Match Score
    - Sortable columns
    - Lime green dot on matched rows
    - Click row to open detail panel
    - Pagination (50 per page)

- Right detail panel (slides in on row click, 380px):
  - Business name (large)
  - Filing type badge
  - State + date
  - Registered agent
  - Address
  - Enrichment section:
    - Website (link)
    - Email (mailto link)
    - Phone
    - LinkedIn (link)
  - Actions:
    - "Send to CRM" button (lime green, primary)
    - "Export Contact" button (secondary)
    - Star/unstar toggle
    - "Mark as Read"

### `/alerts`
- List of sent alerts with timestamp
- Filter by watchlist
- Click to see matched filing

### `/watchlists`
- List of user's watchlists
- Create new watchlist
- Edit existing (states, types, keywords, frequency)
- Toggle active/inactive
- Delete with confirmation

### `/settings`
- Profile info
- Email preferences
- CRM webhook URL configuration
- Plan & billing (link to Stripe portal)
- Export all data (CSV download)

---

## API ROUTES

### `/api/filings`
- GET: List filings with pagination, filters (state, date, type, search)
- Query params: state, from_date, to_date, type, search, page, limit

### `/api/matches`
- GET: List user's matches with pagination
- PATCH: Update match (is_read, is_starred)

### `/api/watchlists`
- GET: List user's watchlists
- POST: Create watchlist
- PATCH: Update watchlist
- DELETE: Delete watchlist

### `/api/alerts`
- GET: List user's alert history

### `/api/enrich`
- POST: Trigger enrichment for a filing (rate-limited)

### `/api/export`
- GET: Export matches as CSV

### `/api/webhooks/stripe`
- POST: Handle Stripe subscription events

### `/api/cron/scrape`
- POST: Triggered by Vercel Cron, runs daily scraping (secured with CRON_SECRET)

### `/api/cron/match`
- POST: Run watchlist matching against new filings

### `/api/cron/alerts`
- POST: Send daily digest emails

---

## SEED DATA

Generate realistic seed data for demo purposes:
- 200 sample filings across TX, CA, FL, NY, DE
- Mix of LLC, Corp, DBA types
- Realistic business names (e.g., "Summit Innovations LLC", "BrightNest Homes Corp")
- Dates within last 30 days
- Categories: Technology, Real Estate, Food Service, Construction, Healthcare, Retail, Professional Services

---

## COMPONENTS TO BUILD

1. `Sidebar` — navigation with active state
2. `StatsCard` — metric display card
3. `FilingTable` — sortable, filterable data table
4. `FilingDetailPanel` — slide-in detail view
5. `WatchlistForm` — create/edit watchlist
6. `AlertList` — alert history list
7. `SearchBar` — global search with filters
8. `Badge` — status/type badges (JetBrains Mono)
9. `MatchScoreBar` — visual score indicator
10. `EmptyState` — for empty tables/lists
11. `OnboardingWizard` — multi-step setup flow

---

## IMPORTANT IMPLEMENTATION NOTES

1. Use Supabase client-side SDK for real-time subscriptions on matches table
2. Implement optimistic UI updates for starring/reading
3. Use React Server Components where possible
4. Implement proper loading skeletons (not spinners)
5. All tables must be keyboard-navigable
6. Search should debounce (300ms)
7. Filing table must handle 10,000+ rows efficiently (virtual scrolling or server-side pagination)
8. Mobile responsive: sidebar collapses to hamburger menu, detail panel goes full-screen
9. Use Supabase Row Level Security — never trust client-side auth alone
10. Stripe integration: use Stripe Checkout for subscription, Customer Portal for management

---

## DO NOT

- Add a light mode
- Use any UI component library (build all components from scratch with Tailwind)
- Use any ORM (use Supabase client directly)
- Add social auth (email only for MVP)
- Over-engineer the scraping layer (placeholder/mock for MVP, real scrapers added later)
- Add team/collaboration features (single-user MVP)
