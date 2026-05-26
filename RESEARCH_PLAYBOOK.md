# RESEARCH_PLAYBOOK.md

This document explains how to research ideas for Signal Board.

## Goal

The goal of research is to determine whether a problem is:
- real
- recurring
- monetizable
- painful enough to deserve a board slot

## Where to Look

Search places where people describe real workflows and real frustration:
- Reddit
- niche forums
- Indie Hackers
- Facebook groups
- Slack/Discord communities
- G2 / Capterra reviews
- app comparison threads
- API marketplaces / scraper popularity
- job descriptions that reveal repeated manual operations

## What to Look For

### Strong evidence

Strong evidence includes:
- explicit requests for a tool or solution
- multiple people describing the same manual workflow
- complaints about cost, complexity, or missing features in incumbents
- obvious spreadsheet/screenshot/copy-paste behavior
- urgency tied to money, leads, reputation, or operational pain
- evidence that people are already paying for a bad version of the solution

### Weak evidence

Weak evidence includes:
- generic trend discussion
- aspirational or theoretical interest
- curiosity without urgency
- one-time problems
- no clear buyer
- no evidence of repeated behavior

## Research Questions

For every candidate idea, answer these questions:

1. **Who is the buyer?**
2. **What exact workflow is painful?**
3. **How often does this pain happen?**
4. **What is the current workaround?**
5. **Why is the workaround bad?**
6. **What tools already exist?**
7. **Why are those tools insufficient?**
8. **How crowded is the market, really?**
9. **Is competition low enough, or do we have a truly sharp wedge?**
10. **Why would someone pay for a better version?**
11. **How simple could an MVP be?**
12. **Can we realistically reach this audience for validation?**
13. **What would the validation page actually promise?**
14. **What CTA would we test first?**
15. **How would we capture signups or replies on a live page?**
16. **What live URL / deployment path would we use if we validated this tomorrow?**
17. **What traffic source would we realistically send first?**

## Minimum Standard Before Adding an Idea

Before adding an idea to `projects.json`, try to have:
- 3+ real examples of pain evidence
- a clear target buyer
- a current manual workflow summary
- a friction summary
- a rough pricing hypothesis
- an MVP framing
- a rough validation angle (what the landing page would say)
- a rough CTA hypothesis
- an initial thought on how we would get a live page and capture demand
- a basic competition read: who already exists, how strong they are, and whether the opportunity is actually low-competition

If the evidence is weak, do not force it onto the board.
If competition is high, do not force it onto the board unless there is a clear and credible wedge.

## How to Write a Good Idea Card

A strong Ideas-stage record usually includes:
- short pain summary
- meaningful tags
- score + rough time-to-MVP
- pricing hypothesis
- `details` entries for:
  - Current Manual Workflow
  - Workflow Friction
  - Evidence
  - Relevant APIs / actors
  - Why They'd Pay
  - Existing Bad Solutions

## Scoring Guidance

Use the score as an internal judgment call, not fake precision.

High scores usually mean:
- buyer is obvious
- pain is recurring
- workaround is ugly
- existing tools are weak/expensive
- competition is low or the wedge is unusually strong
- MVP is small enough
- distribution is accessible

Low scores usually mean:
- buyer is fuzzy
- pain is infrequent
- market gap is weak
- competition is crowded with no sharp wedge
- MVP is too big
- go-to-market is unclear

See `SCORING_RUBRIC.md` for a more formal rubric.

## Practical Research Standard

Prefer depth over volume.

A well-researched idea with:
- clear buyer
- strong pain evidence
- obvious monetization

is more valuable than ten vague brainstorms.

## Research Output Standard

When finished, the result should make it easy for another agent to answer:
- why this idea exists
- who it is for
- why it matters
- why existing options are not good enough
- why it deserves to move to Design
