# AGENTS.md — Signal Board

## Purpose
Signal Board is a lightweight portfolio pipeline for LTG product ideas.

It is not just a design board.
It is the decision system for moving ideas through:
- Ideas
- Design
- Validation
- Build
- Live

## Non-Negotiables

- `main` is the only canonical branch
- GitHub Pages is expected to reflect `main`
- Do not create `master`
- `projects.json` is the source of truth
- `index.html` is the renderer/UI
- After changing the board, commit and push to `main`
- Keep the board state, repo assets, and live site consistent

## How Ideas Are Created

Do not add ideas just because they sound interesting.

Signal Board ideas should come from researched pain signals such as:
- Reddit posts asking for solutions
- forum threads describing recurring frustration
- expensive or bloated incumbents creating price gaps
- repeated manual workflows using spreadsheets, screenshots, or copy/paste
- evidence that people are already trying to solve the problem badly
- API/scraper usage patterns that reveal strong demand

A good idea usually has:
- a clear buyer
- recurring pain
- a specific workflow problem
- a monetization path
- a reason existing solutions are not good enough

## What “Clean” Means Here

Any agent should be able to open this repo and immediately understand:
- what each stage means
- how ideas are discovered
- which branch is canonical
- what file to edit
- whether the live board matches the repo

If anything is ambiguous, fix the ambiguity.

## Editing Rules

When updating Signal Board:
1. edit `projects.json` first
2. only edit `index.html` if the renderer or layout needs to change
3. keep stage, assets, and validation state aligned
4. if in Validation, update validation metrics fields
5. commit with a literal message describing the change
6. push to `main`

## Stage Intent

### Ideas
Evidence-backed opportunities worth tracking.

### Design
Packaged concepts with name, positioning, mockup, and build brief.

### Validation
Landing page and demand testing phase.

Use it to track:
- LP URL
- Signups
- Qualified signups
- Conversion
- Traffic source
- Last check
- Validation status

### Build
Build should mean **validated demand**, not just "assets are done."

### Live
Shipped and publicly accessible.

## Promotion Logic

### Ideas → Design
Move when the research is strong enough to justify packaging the opportunity.

### Design → Validation
Move when the product can be tested with a landing page or demand capture flow.

### Validation → Build
Move when there is real signal:
- qualified signups
- strong replies
- demo/pilot interest
- willingness-to-pay evidence

## Folder Expectations

Per-project folders may include:
- `PRD.md`
- `meta-prompt.md`
- `logo.png`
- `ui-mockup.png`
- later: landing page assets if needed

Keep naming straightforward.
Avoid mystery files.

## Default Agent Behavior

If asked to update Signal Board:
- make the smallest clear change that preserves readability
- prefer explicit labels over hidden logic
- push your changes unless explicitly told not to
- verify branch/repo cleanliness after structural changes
- if idea-generation logic is missing from docs, add it
