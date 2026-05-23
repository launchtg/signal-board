# Signal Board

Signal Board is Launch Technology Group's visual pipeline for moving product ideas from raw opportunity to validated product.

GitHub Pages URL: <https://launchtg.github.io/signal-board/>
Repo: `launchtg/signal-board`

## Doc Map

### Tier 1 — Read first
These are enough for a new agent to understand and operate the system:
- `README.md` — repo overview, source of truth, workflow, schema
- `HOW_IT_WORKS.md` — the operating system / stage logic
- `AGENTS.md` — agent-specific editing rules and behavior

### Tier 2 — Read when doing the work
Use these when performing specific tasks:
- `RESEARCH_PLAYBOOK.md` — how ideas are discovered and researched
- `VALIDATION_PLAYBOOK.md` — how demand is tested before build
- `INTAKE_CHECKLIST.md` — exact intake and stage-update procedure
- `PROJECT_TEMPLATE.json` — reusable template for new project records

### Tier 3 — Reference when needed
Helpful, but not required up front:
- `SCORING_RUBRIC.md` — how to score opportunities more consistently
- `KILL_CRITERIA.md` — when to kill, hold, or deprioritize ideas
- `EXAMPLES.md` — good vs bad card patterns and decision examples
- `SAMPLE_VALIDATION_CASE.md` — what a completed validation review should look like

## Source of Truth

- **Branch:** `main`
- **GitHub Pages serves from:** `main`
- **Do not create or use `master`**
- **`projects.json` is the board source of truth**
- `index.html` is the renderer/UI for GitHub Pages
- **browser drag/drop is visual only unless `projects.json` is changed and pushed**
- After any board change, **commit and push to `main` immediately** so the live board matches the repo

## Idea Creation System

Ideas do not come from vibes alone.

Add ideas only when there is repeated evidence that a real market has a painful, recurring, monetizable problem.

At minimum, an idea should have:
- a clear pain summary
- a target buyer hypothesis
- a current manual workflow
- evidence of real people describing the pain
- a rough monetization angle
- a rough MVP scope

For the full research standard, read `RESEARCH_PLAYBOOK.md`.

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

- **Ideas → Design** when the research is strong enough to justify packaging the opportunity
- **Design → Validation** when the product can be tested with a landing page or demand capture flow
- **Validation → Build** when there is real signal from the right audience
- **Build → Live** when the product is deployed and publicly accessible

For fuller stage logic, read `HOW_IT_WORKS.md` and `VALIDATION_PLAYBOOK.md`.

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

Folder rule:
- Ideas-stage records usually do **not** need a folder yet
- create a folder once the project enters Design or real assets need a home

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
- Update `meta.lastUpdated` whenever project data changes meaningfully

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
