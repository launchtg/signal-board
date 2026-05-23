# HOW_IT_WORKS — Signal Board Operating System

This document explains Signal Board as a system, not just a UI.

## Core Principle

Signal Board exists to help LTG choose which product ideas are worth building.

The goal is **not** to collect clever ideas.
The goal is to move from:
- observed pain
- to packaged concept
- to real market validation
- to build decision
- to live product

## The Pipeline

### 1. Ideas
This is the research queue.

A project enters Ideas only when there is evidence that:
- a specific buyer has a specific recurring pain
- the current workflow is annoying, manual, expensive, or broken
- existing solutions are too expensive, too bloated, or poorly targeted
- there is a plausible monetization path

Ideas should be evidence-backed, not vibe-backed.

### 2. Design
This is packaging.

The purpose of Design is to turn a researched problem into something testable.

That usually means:
- naming the product
- clarifying the positioning
- creating a logo
- creating a UI mockup
- writing the PRD
- writing the meta prompt / build brief

Design does **not** mean the product deserves to be built.
It means the idea is ready to be tested.

### 3. Validation
This is the market test.

The purpose of Validation is to answer:
**Do enough real people care enough to justify building this?**

This stage usually includes:
- a landing page
- a CTA
- distribution to relevant communities or channels
- signup tracking
- quality-of-interest tracking

Validation matters more than polish.

### 4. Build
This is the implementation decision.

A project should enter Build only after there is real signal such as:
- qualified signups
- strong replies from target buyers
- demo or pilot requests
- willingness-to-pay signals
- repeated positive feedback from the right audience

Build should mean:
**validated demand exists**
not:
**we have assets and are excited**

### 5. Live
This is the execution phase after launch.

A project is Live when:
- it is deployed
- it has a public URL
- it is now being measured as a real business/project

## Decision Logic

Signal Board is a filter.

Each stage should reduce uncertainty:
- Ideas reduces uncertainty about whether the problem matters
- Design reduces uncertainty about whether the concept is understandable
- Validation reduces uncertainty about whether the market wants it
- Build reduces uncertainty about whether it can be executed
- Live reduces uncertainty about whether it can sustain traction/revenue

## Source of Truth

- `projects.json` is the source of truth for project data
- `index.html` renders the board for GitHub Pages
- `README.md` explains the repo and schema
- `AGENTS.md` explains agent behavior
- supporting docs explain research, validation, and scoring

## What Counts as a Good Move

A move between stages should correspond to a real state change.

Good example:
- an idea gets enough research → move to Design
- landing page is live and traffic is being sent → move to Validation
- signups and buyer replies are strong → move to Build

Bad example:
- move to Build because the mockup looks good
- move to Validation with no CTA
- move to Live because a prototype exists privately

## Kill Logic

Signal Board should not become a graveyard of permanent maybe-projects.

Kill, archive, or deprioritize ideas when:
- the pain was weaker than expected
- the wrong audience responded
- the market already has a good-enough solution
- validation traffic did not convert meaningfully
- willingness-to-pay signals are absent
- distribution channels are too hard relative to upside

## Operating Standard

Any agent should be able to open this repo and understand:
- what the stages mean
- how ideas are created
- what file to edit
- what proof is needed to move something forward
- when an idea should be killed

If the docs stop making that obvious, improve them.
