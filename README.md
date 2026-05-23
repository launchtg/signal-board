# Signal Board

Signal Board is Launch Technology Group's visual pipeline for moving product ideas from raw opportunity to validated product.

GitHub Pages URL: <https://launchtg.github.io/signal-board/>
Repo: `launchtg/signal-board`

## Core Docs

Read these in order if you are new to the repo:
- `README.md` — repo overview, workflow, schema
- `HOW_IT_WORKS.md` — the operating system / stage logic
- `RESEARCH_PLAYBOOK.md` — how ideas are discovered and researched
- `VALIDATION_PLAYBOOK.md` — how demand is tested before build
- `SCORING_RUBRIC.md` — how to score opportunities more consistently
- `KILL_CRITERIA.md` — when to kill, hold, or deprioritize ideas
- `EXAMPLES.md` — good vs bad card patterns and decision examples
- `SAMPLE_VALIDATION_CASE.md` — what a completed validation review should look like
- `PROJECT_TEMPLATE.json` — reusable template for new project records
- `AGENTS.md` — agent-specific behavior and editing rules

## Source of Truth

- **Branch:** `main`
- **GitHub Pages serves from:** `main`
- **Do not create or use `master`**
- **`projects.json` is the board source of truth**
- `index.html` is the renderer/UI for GitHub Pages
- After any board change, **commit and push to `main` immediately** so the live board matches the repo

## Idea Creation System

Ideas do not come from vibes alone.

They should be created from repeated evidence that a real market has a painful, recurring, monetizable problem.

### Primary idea sources

Look for ideas in places where people describe workarounds, frustration, or missing tools:
- Reddit threads
- niche forums
- Facebook groups
- Slack / Discord communities
- Indie Hackers
- G2 / Capterra reviews
- product comparison threads
- job descriptions that reveal tedious workflows
- popular scraper/API usage patterns that signal demand

### Good signals

Strong idea signals include:
- people explicitly asking for a solution
- repeated complaints about manual workflows
- screenshots, spreadsheets, copy/paste, browser bookmark routines
- existing tools being too expensive, too bloated, or too enterprise
- people hacking together ugly partial solutions
- strong urgency or financial impact
- clear buyer identity

### Weak signals

Avoid adding ideas based only on:
- personal curiosity
- generic AI hype
- problems with no clear buyer
- one-off pain with low repeat frequency
- markets where free/native tools already solve it well

## Research Standard for Adding an Idea

Before a project is added to Signal Board, aim to have:
- a clear pain summary
- target buyer hypothesis
- current manual workflow
- workflow friction
- evidence of real people describing the pain
- existing solutions and why they fail
- rough monetization angle
- rough MVP scope

The goal is to add **evidence-backed opportunities**, not random brainstorms.

## What the Board Means

### 1. Ideas
Raw but evidence-backed opportunities worth tracking.

A card belongs here when we have:
- a clear pain point
- evidence of demand signals
- target buyer hypothesis
- rough monetization idea
- enough research to justify tracking it on the board

### 2. Design
The idea has been packaged into something testable.

A card belongs here when we have:
- name
- positioning
- logo
- UI mockup
- PRD
- meta prompt / build brief

### 3. Validation
The idea is being market-tested before build.

A card belongs here when we have:
- landing page live
- signup CTA active
- traffic being sent
- validation data being tracked on-card

Validation fields to maintain:
- LP URL
- Signups
- Qualified
- Conversion
- Traffic Source
- Last Check
- Validation Status

### 4. Build
Only validated ideas should move here.

A card belongs here when:
- demand is proven enough to justify build
- validation data is positive
- we are ready to execute the product

### 5. Live
Shipped products.

A card belongs here when:
- product is deployed
- public URL exists
- we are monitoring traction/revenue

## Stage Promotion Criteria

### Ideas → Design
Move when:
- research is strong enough to justify packaging the opportunity
- buyer and pain are clear
- the market gap is real enough to test

### Design → Validation
Move when:
- creative assets exist
- positioning is clear
- landing page is ready or live
- there is a concrete CTA to measure demand

### Validation → Build
Move when there is real signal, such as:
- qualified signups
- strong replies from target users
- repeated positive feedback
- demo/pilot requests
- willingness-to-pay signals

### Build → Live
Move when:
- the product is deployed
- there is a public/live URL
- the project is now in execution/traction mode instead of concept mode

## Repo Structure

- `projects.json` — source of truth for all project/stage data
- `index.html` — the live board UI used by GitHub Pages
- `assets/` — shared board assets
- `aisearchrank/` — product assets for AISearchRank
- `licensewatch/` — product assets for NewFilings / licensewatch assets

Each product folder should contain, when available:
- `PRD.md`
- `meta-prompt.md`
- `logo.png`
- `ui-mockup.png`
- optional landing page assets later

## Project Record Schema

When creating a new record, start from `PROJECT_TEMPLATE.json` and then adapt it to the actual project stage.

Each project in `projects.json` should follow this general shape:

```json
{
  "id": "short-stable-id",
  "name": "ProjectName",
  "domain": "projectname.com",
  "stage": "ideas|design|validation|build|live",
  "pain": "One clear sentence describing the pain/opportunity.",
  "tags": [
    { "text": "Market / Buyer", "class": "market" },
    { "text": "Category" },
    { "text": "API / Source", "class": "api" }
  ],
  "score": "8.8/10",
  "scorePercent": 88,
  "mvpTime": "~3 days MVP",
  "pricing": "$29-79/mo",
  "details": [
    { "title": "Current Manual Workflow", "text": "..." },
    { "title": "Workflow Friction", "text": "..." },
    { "title": "Evidence", "text": "..." },
    { "title": "Relevant APIs", "text": "..." },
    { "title": "Why They'd Pay", "text": "..." },
    { "title": "Existing Bad Solutions", "text": "..." }
  ],
  "assets": {
    "folder": "project-folder",
    "logo": "project-folder/logo.png",
    "uiMockup": "project-folder/ui-mockup.png",
    "prd": "project-folder/PRD.md",
    "metaPrompt": "project-folder/meta-prompt.md"
  },
  "validation": {
    "lpUrl": "not live",
    "signups": "0",
    "qualified": "0",
    "conversion": "—",
    "trafficSource": "—",
    "lastCheck": "not launched",
    "status": "NOT LIVE"
  }
}
```

### Field guidance

- `id` — short, stable, lowercase identifier used by the UI
- `name` — public-facing product name
- `domain` — preferred domain if known
- `stage` — current board column
- `pain` — the shortest useful description of the pain/opportunity
- `tags` — usually market, category, and API/source
- `score` / `scorePercent` — internal attractiveness score + display bar width
- `mvpTime` — rough time-to-first-version estimate
- `pricing` — rough pricing hypothesis
- `details` — used mainly for Ideas-stage research context
- `assets` — used when a project has entered Design or beyond
- `validation` — used for Design/Validation/Build/Live stage tracking when demand testing matters

### Practical rules

- Use `details` for research-backed idea context
- Use `assets` only when files actually exist or are about to exist
- Add `validation` when a project is in Design or later
- Keep values explicit; avoid hidden assumptions
- Prefer updating an existing record over inventing alternate structures

## Workflow Rules

1. Update `projects.json` first
2. Only update `index.html` when the renderer/UI itself needs changes
3. Keep card stage and asset state aligned
4. If a card moves stages, update any relevant validation tracking fields
5. Commit clearly
6. Push to `main`
7. Verify GitHub Pages reflects the change

## Commit Style

Use direct commit messages like:
- `Move AISearchRank to Design on Signal Board`
- `Add Validation stage and tracking fields to Signal Board`
- `Update NewFilings validation metrics`
- `Document Signal Board idea creation workflow`

## Agent Notes

If you are an agent opening this repo:
- assume `main` is canonical
- assume the GitHub Pages site should match the repo exactly
- assume `projects.json` is the primary editing surface
- prefer clarity over cleverness
- leave the board cleaner than you found it
- if you edit the board, push the change unless explicitly told not to
- ideas should be evidence-backed, not just clever-sounding
