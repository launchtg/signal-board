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

Ideas should come from researched pain signals:
- people asking for solutions
- repeated manual workflows
- expensive or weak incumbents
- evidence of recurring buyer pain

If you need the full research standard, read `RESEARCH_PLAYBOOK.md`.

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
4. update `meta.lastUpdated` when data changes meaningfully
5. if in Validation, update validation metrics fields
6. commit with a literal message describing the change
7. push to `main`

## Stage Intent

- **Ideas** — evidence-backed opportunities worth tracking
- **Design** — packaged concepts with name, positioning, mockup, and build brief
- **Validation** — landing page and demand-testing phase
- **Build** — validated demand exists; not just finished assets
- **Live** — shipped and publicly accessible

For the full stage logic, read `HOW_IT_WORKS.md` and `VALIDATION_PLAYBOOK.md`.

## Project Data Expectations

`projects.json` is the primary editing surface.
Start from `PROJECT_TEMPLATE.json` when creating a new record.

Each record should usually include:
- `id`
- `name`
- `domain`
- `stage`
- `pain`
- `tags`
- `score`
- `scorePercent`
- `mvpTime`
- `pricing`

Optional but common sections:
- `details` — research context for Ideas-stage cards
- `assets` — for Design+ cards with logo/mockup/PRD/meta prompt
- `validation` — for demand-tracking once a project reaches Design/Validation

Do not invent alternate ad hoc structures when the existing schema is sufficient.
Extend the schema only when there is a clear repeated need.

## Folder Expectations

Per-project folders may include:
- `PRD.md`
- `meta-prompt.md`
- `logo.png`
- `ui-mockup.png`
- later: landing page assets if needed

Folder creation rule:
- do not create folders for every Ideas-stage card by default
- create a folder once the project enters Design or real assets need to be stored

Keep naming straightforward.
Avoid mystery files.

## Reading Order for Agents

### Minimum to operate
1. `README.md`
2. `HOW_IT_WORKS.md`
3. `AGENTS.md`

### Read when needed
4. `RESEARCH_PLAYBOOK.md`
5. `VALIDATION_PLAYBOOK.md`
6. `INTAKE_CHECKLIST.md`
7. `PROJECT_TEMPLATE.json`
8. `tools/validate_projects.py`
9. `tools/new_project.py`
10. `tools/publish_board.sh`

### Reference only
11. `SCORING_RUBRIC.md`
12. `KILL_CRITERIA.md`
13. `EXAMPLES.md`
14. `SAMPLE_VALIDATION_CASE.md`

## Default Agent Behavior

If asked to update Signal Board:
- make the smallest clear change that preserves readability
- prefer explicit labels over hidden logic
- remember that browser drag/drop is visual only unless `projects.json` changes
- run `python3 tools/validate_projects.py` before publishing
- use `tools/new_project.py` instead of inventing new record structure by hand when practical
- push your changes unless explicitly told not to
- verify branch/repo cleanliness after structural changes
- if workflow logic is missing from docs, add it
- if schema changes, update docs in the same pass
