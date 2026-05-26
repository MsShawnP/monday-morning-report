---
title: "feat: Build Monday Morning Report Excel template and Cinderhaven case study"
date: 2026-05-26
status: active
plan_depth: standard
---

# feat: Build Monday Morning Report Excel template and Cinderhaven case study

**Created:** 2026-05-26
**Depth:** Standard

---

## Problem Frame

Specialty food founders at $3M–$15M have no trusted weekly pulse. They cobble together
data from four browser tabs on Sunday night, spend 45 minutes assembling a picture they
don't trust, and forget it by Tuesday. The Monday Morning Report is a downloadable
spreadsheet that gives them three numbers — chosen for their revenue tier — in 30 seconds
flat. The founder fills in three cells, sees whether things are better or worse than last
week, writes one sentence on what to do about it, and closes the file.

**Scope:** This repo produces the template file and Cinderhaven case study only.
Landing page, email capture, and article content are out of scope (see Scope Boundaries).

---

## Requirements

- **R1** Three-tier metric structure: $3M–$10M, $10M–$15M, $15M–$20M
- **R2** Tier selector on Setup tab auto-configures metric labels across the workbook
- **R3** This Week tab: three input cells, prior-week values for comparison, trend
  arrows (↑ ↓ →), one-line action note per metric
- **R4** History tab: 52 pre-created rows (one year); row 1 formula-links to This
  Week; rows 2–52 are blank input rows for manual weekly copy-down
- **R5** Where to Find These Numbers tab: per-metric guide — which system, which
  report, what to watch for, one common gotcha
- **R6** Starter defaults clearly labeled as suggested starting points, not
  prescriptions
- **R7** No macros — formulas and data validation only (Excel + Sheets portability)
- **R8** Lailara design system applied throughout (Canvas background, Chicago navy
  headers, Source Sans 3, Economist aesthetic, print-ready)
- **R9** Google Sheets: import guide documenting how to upload the .xlsx and what
  formatting gaps to reapply manually
- **R10** Cinderhaven case study: 12-week Markdown narrative showing the template in
  action, including the Week 6 velocity-drop story

---

## Key Technical Decisions

### 1. Python / openpyxl for template generation
Generate the .xlsx programmatically. Rationale: version-controllable, reproducible
when defaults change after v1 founder validation, readable diff when the metric set
evolves. Trade-off: openpyxl doesn't support native Excel icon sets or sparklines —
trend arrows are Unicode characters (↑ ↓ →) in formula-driven cells; sparklines are
omitted.

### 2. Metrics defined as Python data structure
Tier and metric definitions live in `data/metrics.py` as a typed dict. A dedicated
config format (JSON, YAML) adds overhead without benefit at this scale.

### 3. No macros
All interactivity via data validation (tier dropdown) and formulas (dynamic labels,
trend arrows, last-week reference). Ensures the file opens cleanly on any platform
and survives import to Google Sheets.

### 4. Trend arrow formula
`=IF(B5>C5,"↑",IF(B5<C5,"↓","→"))` where B5 = This Week, C5 = Last Week.
Colored via conditional formatting rules (↑ teal #158f75, ↓ red #cc100a, → grey
#666666). openpyxl CF font-color support has version quirks — fall back to background
color if font color proves unreliable.

### 5. Google Sheets: import, not API
Provide the .xlsx plus a one-page import guide (`docs/google-sheets-import.md`).
No gspread dependency. Eliminates OAuth complexity for a Tier 4 asset. Known gap:
conditional formatting may not transfer — document reapplication steps.

### 6. Three tiers retained
Keep $3M–$10M / $10M–$15M / $15M–$20M as specified in the brief. Consolidating to
two saves complexity but loses tier-awareness across the full target band, which is
a stated differentiator.

### 7. Defaults labeled as working hypotheses
Every metric label carries a note: *"Suggested default — change to match your
business."* The brief's starter set is defensible but not yet validated with real
founders; this framing is honest and reduces the risk of overclaiming.

---

## Output Structure

```
monday-morning-report/
├── generate.py                        # Entry point — produces output/monday-morning-report.xlsx
├── requirements.txt                   # openpyxl only
├── data/
│   └── metrics.py                     # Tier definitions and starter metric defaults
├── output/
│   └── monday-morning-report.xlsx     # Generated deliverable (committed to repo)
├── docs/
│   ├── google-sheets-import.md        # One-page import guide
│   └── cinderhaven-case-study.md      # 12-week narrative
└── docs/plans/
    └── 2026-05-26-001-feat-...-plan.md
```

---

## Implementation Units

### U1. Project scaffolding and metrics data model

**Goal:** Python environment, directory structure, and the tier/metric data that
drives every tab in the workbook.

**Requirements:** R1, R6, R7

**Dependencies:** None

**Files:**
- `generate.py` (scaffold — imports + calls to tab-builder functions defined in U2–U5)
- `data/__init__.py`
- `data/metrics.py`
- `requirements.txt`
- `output/.gitkeep`

**Approach:**
Define a `TIERS` ordered dict in `data/metrics.py`. Each entry keyed by tier label
("$3M–$10M" etc.) contains: revenue range string, and a list of three metric dicts.

Each metric dict has:
- `label` — short display name (e.g., "Cash Position")
- `description` — one sentence shown in the template
- `unit` — "currency" / "units" / "count" / "text"
- `source_system` — which portal/system (e.g., "Bank portal + QuickBooks AR aging")
- `source_detail` — exact report name or navigation path
- `watch_for` — one-sentence interpretation guide
- `gotcha` — one-sentence common mistake (the credibility marker)
- `default_note` — "Suggested default — change to match your business"

Starter defaults (working hypothesis per office hours):

| Tier | Metric 1 | Metric 2 | Metric 3 |
|---|---|---|---|
| $3M–$10M | Cash position (bank + AR – AP due) | Confirmed POs not yet shipped | Velocity pulse (units/store/week, top 3 SKUs, key retailer) |
| $10M–$15M | Revenue vs plan MTD by channel | 4-week cash forecast | Operational red flag (OTIF trend / deduction spike) |
| $15M–$20M | Revenue vs plan by channel | Cash conversion status (owed/disputed/expected) | Growth pipeline (new retailer timelines, capacity utilization) |

`generate.py` scaffold: load metrics, call tab builders, save workbook to
`output/monday-morning-report.xlsx`.

**Test scenarios:**
- Import `data/metrics.py` — three tiers present, each with exactly three metrics
- Each metric dict contains all seven required fields (no KeyError)
- `python generate.py` runs without error and creates `output/monday-morning-report.xlsx`
- Generated file opens in openpyxl (not corrupted)

**Verification:** `python generate.py` succeeds; file exists at `output/monday-morning-report.xlsx`.

---

### U2. Setup tab and This Week tab

**Goal:** The two tabs a founder touches every Monday. Setup selects the tier;
This Week captures the three numbers.

**Requirements:** R1, R2, R3, R6, R7, R8

**Dependencies:** U1

**Files:**
- `generate.py` (add `build_setup_tab(wb, metrics)` and `build_this_week_tab(wb, metrics)`)

**Approach:**

**Setup tab layout:**
- Row 1: brand header — "Monday Morning Report" (Playfair Display / serif, 22px,
  navy #1f2e7a fill, white text)
- Row 3: label "Select your revenue tier:" (Source Sans 3, text-secondary #595959)
- Row 4: tier dropdown cell (data validation — dropdown list of three tier keys);
  cell highlighted with light border to signal it's the one thing to fill in
- Rows 6–8: three metric label cells, each formula-driven:
  `=INDEX(tier_label_range, MATCH($B$4, tier_key_range, 0), metric_col)`
  Since openpyxl can't write dynamic cross-sheet INDEX/MATCH easily at generation
  time, the simpler approach: bake all three tier label sets into a hidden "Config"
  sheet, and the Setup tab's metric display cells use IF formulas referencing the
  dropdown value
- Row 10: italic note — "These are suggested defaults. Change any metric label to
  match your business."
- Canvas background (#f5f3ee) for the sheet tab area

**This Week tab layout:**
- Row 1: header "Week of: [date input cell]"
- Rows 3–5, 7–9, 11–13: one block per metric (three blocks total). Each block:
  - Row A: metric label (formula referencing Setup tab dropdown selection)
  - Row B: | "This Week" input cell (yellow-ish fill) | "Last Week" (formula from
    History row 1, read-only grey fill) | Trend arrow (formula) |
  - Row C: "What I'm doing about it:" + free-text input cell (full width)
  - Thin separator below each block
- Below all three blocks: italic note per metric label — "Suggested default"
- Trend arrow conditional formatting: ↑ font color teal, ↓ red, → grey

**Patterns to follow:** Lailara color tokens in `~/projects/active/CLAUDE.md`.

**Test scenarios:**
- Setup tab has a working dropdown with exactly three tier options
- Selecting "$3M–$10M" on Setup tab causes This Week tab to display the correct
  three metric labels for that tier
- Switching tier updates all three labels (not just the first)
- This Week tab has exactly three metric input cells, three Last Week cells, and
  three trend arrow cells
- Trend arrow cell with This Week=100, Last Week=90 → "↑"
- Trend arrow cell with This Week=80, Last Week=90 → "↓"
- Trend arrow cell with This Week=90, Last Week=90 → "→"
- Last Week cell references History tab row 1 (formula visible in formula bar)

**Verification:** Open .xlsx, select each tier, confirm label changes; enter test
values on This Week tab, confirm trend arrows update correctly.

---

### U3. History tab

**Goal:** 52 pre-created rows (one year of weekly entries). Row 1 auto-shows
this week's values via formula; rows 2–52 are blank for manual copy-down each week.

**Requirements:** R4, R7

**Dependencies:** U2

**Files:**
- `generate.py` (add `build_history_tab(wb)`)

**Approach:**
Column layout: Date | Metric 1 value | Metric 1 note | Metric 2 value | Metric 2
note | Metric 3 value | Metric 3 note.

Row 1: formula-linked to This Week tab (Date cell, three value cells, three note
cells). Read-only styling (grey fill) to signal these auto-populate.

Rows 2–52: blank but pre-formatted — same column widths, borders, and alternating
row tint for readability.

Instruction block at top (above the column headers):
> "Each Monday: after completing the 'This Week' tab, copy row 1 values and
> paste as values into the next blank row. This builds your trend history."

Why no auto-append: macros are excluded (R7). The copy-paste instruction is the
manual alternative — one extra step, but transparent and portable.

**Test scenarios:**
- History tab present with correct seven column headers
- Row 1 value cells contain formulas referencing This Week tab (not hardcoded)
- Rows 2–52 exist and are blank (no stale data)
- Instruction text is visible above the column headers
- If This Week tab date cell = "2026-05-26", History row 1 date cell shows same

**Verification:** Enter a date and three values on This Week tab; confirm History
row 1 reflects those values without manual action.

---

### U4. Where to Find These Numbers reference tab

**Goal:** For each default metric in each tier, tell the founder exactly which
system to open, which report to pull, and what one thing to watch for.

**Requirements:** R5

**Dependencies:** U1

**Files:**
- `generate.py` (add `build_reference_tab(wb, metrics)`)
- `data/metrics.py` (ensure `source_system`, `source_detail`, `watch_for`, `gotcha`
  fields are fully populated for all nine metrics)

**Approach:**
One tab ("Where to Find These"). Three sections — one per tier — each with three
metric entries. Each entry:

```
[Metric label — bold, navy]
Where to find it: [source_system] → [source_detail]
What to watch for: [watch_for]
Common mistake: [gotcha]
```

The "common gotchas" are the credibility signal. Examples:
- Cash position: "Shopify 'total sales' includes unfulfilled orders — use net
  payouts from the Shopify Payouts report, not the dashboard total"
- Velocity: "Retail Link (Walmart) and Partner Portal (Target) report UPW on
  different lag windows — compare within the same portal, not across"
- Confirmed POs: "A PO from a distributor is not confirmed until you receive the
  EDI 850 — verbal commitments don't count"

Styling: wide columns (readable paragraphs, not truncated cells), generous row
height, Source Sans 3 14px, section headers in navy, dividers between tiers.

**Test scenarios:**
- Tab present with three tier sections
- All nine metrics (3 tiers × 3) have a complete entry (no blank `source_detail`
  or `gotcha`)
- No placeholder text ("[TBD]", "TODO") in any cell
- Tab is readable without horizontal scrolling at 100% zoom

**Verification:** Read through the tab in Excel — every metric has a usable,
specific data source entry and a non-generic gotcha.

---

### U5. Styling pass, Google Sheets guide, and Cinderhaven case study

**Goal:** Apply Lailara design system globally; write the import guide and the
12-week case study.

**Requirements:** R8, R9, R10

**Dependencies:** U2, U3, U4

**Files:**
- `generate.py` (add `apply_global_styles(wb)` called after all tabs are built)
- `docs/google-sheets-import.md`
- `docs/cinderhaven-case-study.md`

**Approach:**

**Global styling (`apply_global_styles`):**
Apply after all tabs exist. For each sheet:
- Default font: Source Sans 3, 12px, color #333333 (Note: custom fonts don't embed
  in .xlsx — openpyxl writes the name; Excel uses it if installed, falls back to
  Calibri otherwise. Document this in a comment in the file.)
- Tab headers (row 1): fill #1f2e7a, font white, bold, 14px
- Section headers within tabs: fill #1f2e7a, font white, 12px
- Body rows: alternating fill — Canvas (#f5f3ee) and white
- Gridlines: set `sheet.sheet_view.showGridLines = False`; apply explicit bottom
  borders in #d9d9d9 on data rows
- Input cells: fill with a very light distinguishing tint (#fffde7 or similar) and
  a visible border so founders know what to type in
- Column widths: set explicitly per tab (don't rely on auto-fit)
- Print setup: `PageSetup` — letter, 0.6in margins; footer with "Monday Morning
  Report — lailara.com" left, page number right

**Google Sheets import guide (`docs/google-sheets-import.md`):**
Under 200 words. Steps:
1. Go to sheets.google.com → Blank spreadsheet
2. File → Import → Upload → select `monday-morning-report.xlsx`
3. Import settings: Insert new sheet(s), Convert text to numbers/dates/formulas
4. Known gaps: conditional formatting (trend arrow colors) does not transfer —
   reapply manually via Format → Conditional formatting in Sheets
5. Fonts: Source Sans 3 is available in Sheets — set via Format → Font

**Cinderhaven case study (`docs/cinderhaven-case-study.md`):**
- Title: "What Cinderhaven's Founder Sees Every Monday Morning"
- Subtitle: "12 weeks of Monday reports, with commentary"
- Opening: one paragraph framing Cinderhaven at ~$25M and why the Monday discipline matters at this stage
- Weekly table (12 rows): Week # | Date | Cash | POs | Velocity (UPW) | Action taken
- Narrative callouts — the three significant weeks:
  - Week 1: establish baseline
  - Week 6: velocity on top SKU at Walmart drops 15% week-over-week. Founder flags it.
    Action: "Called Walmart category manager — asked for a planogram scan."
  - Week 8: root cause identified — planogram shift moved product from eye level to
    bottom shelf. Action: "Submitted reset request; scheduled store-check visit."
  - Week 9: partial recovery after reset
- Closing paragraph: "Without the Monday pulse, this wouldn't have surfaced until
  the quarterly category review — 10 weeks too late. The reset cost $0. A lost
  shelf position at Walmart would have cost $80K–$150K in annual velocity."
- Tone: Economist voice — declarative, specific numbers, no marketing language
- Numbers should be internally consistent (velocity figures align with Cinderhaven's
  established profile from other pieces if those exist; otherwise fabricate plausibly)

**Test scenarios:**
- `python generate.py` produces a styled .xlsx with no Python errors
- All four tabs (Setup, This Week, History, Reference) present and styled
- Row 1 of each tab has navy fill and white text
- Input cells are visually distinct from read-only cells
- Print setup is set (PageSetup object exists on each sheet)
- `docs/google-sheets-import.md` exists and is under 250 words
- `docs/cinderhaven-case-study.md` has all 12 weekly entries and the Week 6 narrative
- No "[PLACEHOLDER]" or "TODO" text in any deliverable

**Verification:** Open .xlsx and scan all four tabs; confirm styling is consistent
and the file looks like a Lailara deliverable, not a default Excel workbook.

---

## Scope Boundaries

### In scope
- `generate.py` + openpyxl to produce `output/monday-morning-report.xlsx`
- Four tabs: Setup, This Week, History, Where to Find These Numbers
- `docs/google-sheets-import.md`
- `docs/cinderhaven-case-study.md`

### Deferred for later
- Starter metric validation with real founders (v2 — expected before wide distribution)
- Automated data connection (Shopify API, bank API, ERP integration) — separate
  productized engagement ("Monday Morning Report Setup" at $3K–$8K)

### Outside this product's identity
- Landing page, email capture, ConvertKit/Mailchimp integration (portfolio site)
- LinkedIn article / written content (handled separately by the user)
- Dashboard, BI tool, or web app version

### Deferred to follow-up work
- Native Google Sheets version built with gspread (only if import quality is
  unacceptable after testing the .xlsx → Sheets import path)
- Sparkline trend charts in History tab (not supported by openpyxl; could be added
  manually after generation)

---

## Deferred Implementation Notes

- Exact openpyxl conditional formatting syntax for trend arrow font coloring —
  confirm at implementation time; CF font-color support has version-specific quirks.
  If unreliable, fall back to background color or accept plain arrows.
- Whether to commit `output/monday-morning-report.xlsx` to the repo — decide at
  implementation time based on whether binary diffs are acceptable in this repo.
  Alternative: `.gitignore output/` and regenerate on demand.
- Cinderhaven velocity and cash numbers — cross-check against existing Cinderhaven
  pieces for internal consistency before finalizing the case study. If no prior
  numbers exist, fabricate plausibly ($25M revenue, top Walmart SKU at ~4–5
  UPW, dropping to ~3.5 in week 6).

---

## Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| openpyxl CF doesn't reliably set font color | Medium | Low | Fall back to background color fill for trend arrows |
| Custom fonts don't embed in .xlsx | High (known) | Low | Document in template comments and import guide; Source Sans 3 is widely available |
| Excel → Sheets import loses conditional formatting | High (known) | Low | Documented in import guide; instruct founder to reapply manually |
| Starter defaults prove wrong post-validation | Medium | Medium | Defaults labeled as working hypotheses; update is a one-file change in `data/metrics.py` |
| openpyxl version incompatibility | Low | Medium | Pin version in `requirements.txt`; test on Python 3.10+ |
