# monday-morning-report — Failure Log

What was attempted that didn't work, why it didn't work, and what was
tried next.

Lower bar than DECISIONS.md — capture failures even when they didn't
produce a durable rule. The whole point: future-you (or future-Claude)
shouldn't re-attempt dead ends because the lesson got lost.

---

## Format

### YYYY-MM-DD — [One-line failure description]

**Attempted:** [What was tried]

**Why it didn't work:** [Concrete reason, not "it broke." If the
failure mode was technical, name the specific issue. If the failure
mode was scope or approach, name that.]

**What we tried instead:** [The next attempt, which may also have
failed and may have its own entry below]

**Status:** Resolved / open / abandoned

**Tags:** [keywords for future text-search — e.g., "rendering, pandoc,
quarto" or "scope, scrollytelling, decoration"]

---

## Entries

### 2026-05-26 — Generic food industry KPI content unusable as starter defaults

**Attempted:** Used LinkedIn content ("gross margin, operating cash flow, prime cost/CAC") and an Aptean food manufacturing blog as sources for the three starter metrics per tier.

**Why it didn't work:** Both sources were wrong for this specific use case. LinkedIn content mixed restaurant and CPG metrics and used monthly/quarterly cadence numbers that can't be pulled on a Monday morning. Aptean content was plant-floor operations (yield per production line, BOM consumption) — not CEO-level at all. Neither source mentioned velocity (units/store/week), which is the most important retail CPG signal.

**What we tried instead:** Fell back to the brief's original working hypothesis, which was written with this specific audience in mind. Labeled all defaults as "Suggested default — change to match your business" to avoid overclaiming. Plan: validate with 3–5 real founders before v2.

**Status:** Resolved (working hypothesis in place; validation deferred to next arc)

**Tags:** research, metrics, defaults, starter-set, velocity, CPG, retail, validation

---

### 2026-05-26 — Unicode characters in print() crash on Windows cp1252 console

**Attempted:** Used `✓` in a `print()` statement in `generate.py`.

**Why it didn't work:** Windows default console encoding is cp1252, which can't encode characters outside the Latin-1 range. Python raises `UnicodeEncodeError: 'charmap' codec can't encode character` at runtime even though the character is valid UTF-8.

**What we tried instead:** Replaced `✓` with plain ASCII text. Works immediately. Alternative fix: add `# -*- coding: utf-8 -*-` and set `PYTHONIOENCODING=utf-8` in the environment, but ASCII replacement is simpler and more portable.

**Status:** Resolved

**Tags:** windows, encoding, cp1252, unicode, print, generate.py
