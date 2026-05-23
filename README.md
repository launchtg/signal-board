# Signal Board

Signal Board is Launch Technology Group's visual pipeline for moving product ideas from raw opportunity to validated product.

GitHub Pages URL: <https://launchtg.github.io/signal-board/>
Repo: `launchtg/signal-board`

## Source of Truth

- **Branch:** `main`
- **GitHub Pages serves from:** `main`
- **Do not create or use `master`**
- After any board change, **commit and push to `main` immediately** so the live board matches the repo

## What the Board Means

### 1. Ideas
Raw opportunities worth researching.

A card belongs here when we have:
- a clear pain point
- evidence of demand signals
- target buyer hypothesis
- rough monetization idea

### 2. Design
The idea has been packaged.

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

## Repo Structure

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

## Workflow Rules

1. Update the board in `index.html`
2. Keep card stage and asset state aligned
3. If a card moves stages, update counts and any relevant tracking fields
4. Commit clearly
5. Push to `main`
6. Verify GitHub Pages reflects the change

## Commit Style

Use direct commit messages like:
- `Move AISearchRank to Design on Signal Board`
- `Add Validation stage and tracking fields to Signal Board`
- `Update NewFilings validation metrics`

## Agent Notes

If you are an agent opening this repo:
- assume `main` is canonical
- assume the GitHub Pages site should match the repo exactly
- prefer clarity over cleverness
- leave the board cleaner than you found it
- if you edit the board, push the change unless explicitly told not to
