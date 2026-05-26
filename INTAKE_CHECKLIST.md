# INTAKE_CHECKLIST.md

Use this file when adding or updating a project in Signal Board.

## New Idea Intake Checklist

1. Research the problem using `RESEARCH_PLAYBOOK.md`
2. Gather at least 3 real pain signals if possible
3. Identify:
   - buyer
   - painful workflow
   - workaround
   - why existing solutions are weak
   - competition level and main competitors
   - whether competition is low enough or the wedge is strong enough
   - why someone would pay
   - rough validation promise / landing page angle
   - likely CTA
   - likely first traffic source
   - likely live deployment path + capture method
4. Score the opportunity using `SCORING_RUBRIC.md`
5. Start from `PROJECT_TEMPLATE.json`
6. Add the project to `projects.json`
7. Set `stage` to `ideas` unless the project has already been packaged further
8. Update `meta.lastUpdated` in `projects.json`
9. Commit and push to `main`
10. Verify GitHub Pages still loads correctly

## When to Create a Project Folder

### Do create a project folder when:
- a project enters **Design**, or
- assets already exist, or
- you are actively creating PRD/mockup/meta-prompt files

### Do not create a project folder yet when:
- the project is only an Ideas-stage research record
- no assets exist yet
- no packaging/build materials exist yet

## Stage Update Checklist

When moving a project between stages:
1. Update the `stage` field in `projects.json`
2. Update any relevant `assets` or `validation` fields
3. Update `meta.lastUpdated`
4. Commit clearly
5. Push to `main`
6. Verify the live board reflects the change

## Validation Update Checklist

When a project is in Validation, keep these fields current:
- `lpUrl`
- `signups`
- `qualified`
- `conversion`
- `trafficSource`
- `lastCheck`
- `status`

## Important UI Rule

The board UI may allow drag/drop for visual organization in the browser.

**That does not change the real source of truth unless `projects.json` is updated and pushed.**

Persistent state lives in:
- `projects.json`
- pushed commits on `main`

## `meta.lastUpdated` Rule

Update `meta.lastUpdated` in `projects.json` whenever:
- a project is added
- a project changes stage
- validation metrics are materially updated
- board structure/data changes meaningfully

Use the date of the current change in `YYYY-MM-DD` format.
