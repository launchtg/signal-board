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
- After changing the board, commit and push to `main`
- Keep the board state, repo assets, and live site consistent

## What “Clean” Means Here

Any agent should be able to open this repo and immediately understand:
- what each stage means
- which branch is canonical
- what changed
- whether the live board matches the repo

If anything is ambiguous, fix the ambiguity.

## Editing Rules

When moving a card:
1. move the card in `index.html`
2. update the column counts
3. keep empty states accurate
4. if in Validation, update validation metrics fields
5. commit with a literal message describing the change
6. push to `main`

## Validation Stage

Validation is between Design and Build.

Use it to track:
- LP URL
- Signups
- Qualified signups
- Conversion
- Traffic source
- Last check
- Validation status

Build should mean **validated demand**, not just "assets are done."

## Folder Expectations

Per-project folders may include:
- `PRD.md`
- `meta-prompt.md`
- `logo.png`
- `ui-mockup.png`

Keep naming straightforward.
Avoid mystery files.

## Default Agent Behavior

If asked to update Signal Board:
- make the smallest clear change that preserves readability
- prefer explicit labels over hidden logic
- push your changes unless explicitly told not to
- verify branch/repo cleanliness after structural changes
