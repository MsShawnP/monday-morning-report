# monday-morning-report — Decisions Log

Permanent record of choices that should survive session turnover.
If a decision is reversed, strike it through and add the replacement
below — don't delete.

---

## Format

Each entry:
- **Date** — when decided
- **Decision** — one sentence, imperative voice
- **Why** — the reasoning, including what was tried and rejected
- **Scope** — what this applies to (file, chunk, deliverable, or "global")
- **Do not** — explicit anti-instructions, if any

---

## Scope

### 2026-05-26 — Article and LinkedIn content handled outside this repo, not with Claude Code
- **Why:** Owner is writing the content piece separately through a different workflow.
- **Scope:** Global — this repo does not contain the article, LinkedIn post, or any written marketing content.
- **Do not:** Draft, scaffold, or suggest article content in this repo.

---

## Architecture & Pipeline

### 2026-05-26 — Email-gate the template download; landing page and capture built on owner's site, not in this repo
- **Why:** Maximum distribution requires a trust signal (email opt-in), but the lead-capture infrastructure (landing page, ConvertKit/Mailchimp form, confirmation flow) lives on the portfolio site — outside this project's scope.
- **Scope:** Global — this repo delivers the template files and content only. No HTML landing page, no form handling, no email integration.
- **Do not:** Build a landing page, email capture form, or any web infrastructure in this repo. The deliverable stops at the downloadable file(s) and written content.

---

## Data & Schema

### 2026-05-26 — Label starter defaults as working hypotheses; validate with founders before v2
- **Why:** No specific research validates the tier-specific metric choices. Domain confidence is based on general CPG knowledge, not observed founder behavior. Overclaiming undermines credibility with the exact audience this template is meant to reach.
- **Scope:** `data/metrics.py`, all template copy referencing the defaults, any marketing language about the three numbers
- **Do not:** Present the three defaults per tier as authoritative or research-backed until at least 3–5 founder interviews confirm them. The "Suggested default — change to match your business" label must stay in the template.

---

## Visualization

[Chart conventions, palette decisions, interactivity choices]

---

## Output Formats

[Decisions about deliverable formats, structure, organization]

---

## Writing & Voice

[Voice, style, terminology decisions specific to this project]

---

## Reversed / Superseded

When a decision is overturned:
1. Strike through the original entry above (don't delete)
2. Add a new entry below with the replacement decision
3. Note the link in both directions

This preserves the history of why something is the way it is.
