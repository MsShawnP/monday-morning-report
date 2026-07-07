# Monday Morning Report

A downloadable Excel template that gives specialty food founders at $3M–$20M revenue three numbers to track every Monday — and nothing else. Built around the discipline that the brands that scale are the ones that see the same three signals every week, not the ones that have a different dashboard crisis each month.

## What it does

Run `python generate.py` once to produce a ready-to-use `.xlsx` file. Open it Monday morning, enter three numbers, close it.

The template is tiered — the right three metrics depend on where your brand sits:

| Revenue tier | Three metrics |
|---|---|
| $3M–$10M | Cash Position · Confirmed POs Not Yet Shipped · Velocity Pulse (top 3 SKUs) |
| $10M–$15M | Revenue vs Plan (MTD by Channel) · 4-Week Cash Forecast · Operational Red Flag |
| $15M–$20M | Revenue vs Plan by Channel · Cash Conversion Status · Growth Pipeline |

Select your tier on the Setup tab. The template adapts. Every default is labelled *"Suggested — change to match your business."*

**Four tabs:**

| Tab | Purpose |
|---|---|
| Setup | Tier selector with visible affordance. Change your defaults here. |
| This Week | Three input cells. Trend arrows auto-populate (↑ teal, ↓ red, → grey). |
| History | 52 pre-created rows. Row 3 links to This Week. One year of signal. |
| Where to Find These | Per-metric data source guide with gotchas. |

Includes a Cinderhaven case study (12-week live example showing how tracking three metrics caught a shelf-position risk before it became a deauthorization) and a Google Sheets import guide.

## Run locally

```bash
pip install -r requirements.txt
python generate.py
```

Output lands at `output/monday-morning-report.xlsx`.

To update the starter defaults — adjust `data/metrics.py`, then regenerate.

## Stack

- Python 3.13
- openpyxl 3.1.5

## Project structure

```
generate.py              Template generator — run this
data/
  metrics.py             Tier definitions and metric defaults (edit here)
docs/
  cinderhaven-case-study.md   12-week example walkthrough
  google-sheets-import.md     Google Sheets compatibility guide
output/
  monday-morning-report.xlsx  Generated template (gitignored, rebuild with generate.py)
```

## Data contract

Canonical Cinderhaven conformance — 50 SKUs across 5 product lines and 6 contracted retailers.

## License

MIT — see [LICENSE](LICENSE).

---

Built by [Lailara LLC](https://lailarallc.com) — data hygiene and analytics consulting for specialty food brands scaling into national retail.
