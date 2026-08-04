# INPUT-SPEC — monday-morning-report (client mode)

The retainer-deliverable generator. Client mode ships **one** revenue tier
(chosen in `engagement.yml`), branded for the client, optionally populated with
the client's KPI values. Derived from `data/metrics.py` (the tier/metric data the
generator consumes), not the README.

## 1. Tier (engagement.yml — required)

```yaml
client: {name: "Meridian Farms"}
engagement: {id: "MER-2026-08"}
as_of_date: "2026-01-31"
basis:
  tier: "$10M–$15M"     # exactly one of: "$3M–$10M", "$10M–$15M", "$15M–$20M"
```

A tier that isn't one of the three produces a **Data Readiness Report** naming
the valid tiers — no workbook. Each tier defines three metrics (see
`data/metrics.py`).

## 2. KPI values (optional file)

A CSV/XLSX of the client's current values for the tier's three metrics. Optional:
with no file, the deliverable is a branded blank template for the client to fill.

| Column | Used for |
|---|---|
| `metric` | the metric name — matched case/whitespace-insensitively to the tier's metric labels |
| `value` | the client's value for that metric (kept as text — never coerced) |

A value for a metric not in the tier is disclosed and ignored; a tier metric with
no value is left blank and disclosed as **proceeded with warnings**.

## Run

```bash
pip install -e ../engagement-template/lib
python client_mode.py --config engagement.yml [--input client-data/kpis.csv] \
    --out client-output [--final]
```

## Output

To `client-output/` (gitignored): `<engagement>-monday-morning-report.xlsx` — a
branded workbook (client name in the Playfair title + `lailarallc.com` footer)
with the one tier's three metrics, their guidance (what it is / where to find it /
watch-for + gotcha), and the client's values where provided. `[DRAFT]` in the
title until `--final`. A **Provenance** sheet carries the tool + version, config
hash, `as_of_date`, input filename + SHA-256, and validation status. Or a
`data-readiness-report.html` if the tier is invalid.

The demo template (`generate.py` → `output/monday-morning-report.xlsx`) is
untouched: it keeps all three tiers behind the chooser. Client mode never edits it.
