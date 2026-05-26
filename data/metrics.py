"""
Tier definitions and starter metric defaults for the Monday Morning Report.

Each tier contains exactly three metrics. Every metric has seven fields:
  label         - short display name shown in the template
  description   - one sentence shown below the label
  unit          - "currency" | "units_per_store" | "count" | "text"
  source_system - which portal or system to open
  source_detail - exact report name or navigation path
  watch_for     - one-sentence interpretation guide
  gotcha        - one common mistake that trips founders up (the credibility signal)

DEFAULT_NOTE is appended to every metric label in the template to make clear
these are suggested starting points, not prescriptions.
"""

DEFAULT_NOTE = "Suggested default — change to match your business"

TIERS = {
    "$3M–$10M": {
        "label": "$3M–$10M",
        "range_note": "Early retail presence, lean staff, cash-constrained",
        "metrics": [
            {
                "label": "Cash Position",
                "description": "Bank balance + AR due within 30 days − AP due this week",
                "unit": "currency",
                "source_system": "Bank portal + QuickBooks / Xero AR aging",
                "source_detail": (
                    "Bank: dashboard balance. "
                    "AR: Accounts Receivable Aging Summary, filter 0–30 days. "
                    "AP: Accounts Payable Aging Summary, filter current week."
                ),
                "watch_for": (
                    "If cash position drops below 6 weeks of operating expenses, "
                    "you have a cash-flow problem forming — act before it becomes a crisis."
                ),
                "gotcha": (
                    "Shopify 'total sales' is not cash — use your bank portal's "
                    "actual balance plus the QuickBooks AR aging, not the Shopify dashboard."
                ),
            },
            {
                "label": "Confirmed POs Not Yet Shipped",
                "description": "Dollar value of purchase orders received but not yet fulfilled",
                "unit": "currency",
                "source_system": "ERP / order management system (or email folder)",
                "source_detail": (
                    "In QuickBooks: Sales Orders report, filter status = Open. "
                    "If using a manual process: count confirmed PO emails in your "
                    "inbox not yet matched to a shipment confirmation."
                ),
                "watch_for": (
                    "This is your near-term revenue visibility. "
                    "If it's shrinking week over week, your pipeline is thinning "
                    "and you'll feel it in cash in 30–60 days."
                ),
                "gotcha": (
                    "A verbal commitment or email discussion is not a confirmed PO. "
                    "Only count orders where you have a written PO number in hand."
                ),
            },
            {
                "label": "Velocity Pulse",
                "description": "Units sold per store per week — top 3 SKUs at your key retailer",
                "unit": "units_per_store",
                "source_system": "Retailer portal (Retail Link for Walmart, Partner Hub for Target, KeHE Connect, UNFI portal)",
                "source_detail": (
                    "Walmart: Retail Link → Sales & Inventory → Item-Level Sales, "
                    "filter by your item numbers, last 4 weeks, ÷ store count. "
                    "Target: Partners Online → Scorecard. "
                    "Natural/specialty: KeHE Connect or UNFI Insights, weekly scan."
                ),
                "watch_for": (
                    "A 10%+ drop in UPW week-over-week on a top SKU at a major retailer "
                    "is a shelf-health signal — investigate before the buyer does."
                ),
                "gotcha": (
                    "Retail Link and KeHE report UPW on different lag windows "
                    "(Walmart is near-real-time; KeHE lags ~2 weeks). "
                    "Never compare UPW numbers across portals directly."
                ),
            },
        ],
    },

    "$10M–$15M": {
        "label": "$10M–$15M",
        "range_note": "Multi-channel distribution, beginning to add staff, plan vs. actual matters",
        "metrics": [
            {
                "label": "Revenue vs Plan (MTD by Channel)",
                "description": "Month-to-date revenue by channel against your monthly plan",
                "unit": "currency",
                "source_system": "ERP or accounting system + channel sales reports",
                "source_detail": (
                    "QuickBooks / NetSuite: P&L by Class (class = channel), "
                    "current month, compare to your annual plan spreadsheet. "
                    "Channels: Natural/Specialty, Conventional Grocery, DTC, "
                    "Club, Export — whatever your top 3 are."
                ),
                "watch_for": (
                    "If any single channel is more than 15% behind plan MTD by week 2, "
                    "it won't catch up without intervention — flag it now, not at month close."
                ),
                "gotcha": (
                    "Distributor invoices ≠ retail sell-through. "
                    "You may be on plan with UNFI but the product is sitting in their warehouse. "
                    "Cross-check with your velocity numbers."
                ),
            },
            {
                "label": "4-Week Cash Forecast",
                "description": "Projected cash position 4 weeks from today",
                "unit": "currency",
                "source_system": "Your cash flow model (spreadsheet or QuickBooks forecast)",
                "source_detail": (
                    "QuickBooks: Cash Flow Forecaster (if set up). "
                    "Otherwise: current cash + expected AR collections − scheduled AP payments "
                    "− payroll − production runs scheduled this month."
                ),
                "watch_for": (
                    "If the 4-week forecast drops below 4 weeks of operating expenses, "
                    "you need to accelerate AR collections or delay a production run."
                ),
                "gotcha": (
                    "Retailer chargebacks and deductions are rarely in AP aging — "
                    "they appear as short-pays on your remittance advice. "
                    "Add a 'deductions buffer' line to your forecast or you'll "
                    "consistently over-estimate collections."
                ),
            },
            {
                "label": "Operational Red Flag",
                "description": "Your single biggest operational risk this week (OTIF trend, deduction spike, or chargeback cluster)",
                "unit": "text",
                "source_system": "Retailer portals + AR aging + 3PL reports",
                "source_detail": (
                    "OTIF: Retail Link (Walmart) → Supplier Performance → OTIF score. "
                    "Deductions: your AR aging for short-pays this week. "
                    "Chargebacks: retailer deduction portal (Target Vendor Portal, "
                    "Kroger vendor portal) — log in weekly and screenshot new items."
                ),
                "watch_for": (
                    "Walmart OTIF below 95% triggers automatic fines. "
                    "A deduction spike (3+ new deductions in one week) often signals "
                    "a systemic issue — wrong UPC, wrong case pack, labeling error."
                ),
                "gotcha": (
                    "Deductions from major retailers can take 60–90 days to appear "
                    "in your AR aging. By the time you see them, the shipment is ancient "
                    "history and disputing is much harder. Check the retailer portal directly "
                    "every Monday — don't wait for the remittance."
                ),
            },
        ],
    },

    "$15M–$20M": {
        "label": "$15M–$20M",
        "range_note": "Scaling distribution, growth pipeline matters as much as current performance",
        "metrics": [
            {
                "label": "Revenue vs Plan by Channel",
                "description": "MTD and prior-week revenue by channel against plan, with variance",
                "unit": "currency",
                "source_system": "ERP (NetSuite / SAP Business One / Sage) + broker reports",
                "source_detail": (
                    "NetSuite: Revenue by Customer Class report, current period. "
                    "Pull actuals by channel (Natural, Conventional, Club, DTC, Foodservice) "
                    "and compare to your annual operating plan by month."
                ),
                "watch_for": (
                    "At this stage, channel mix shift matters as much as total revenue. "
                    "DTC growing at the expense of conventional retail may look fine "
                    "in total but signal a retail relationship problem."
                ),
                "gotcha": (
                    "Broker commission accruals may not be in your P&L until month close. "
                    "If your broker-driven channels look too good MTD, check whether "
                    "commissions have been accrued."
                ),
            },
            {
                "label": "Cash Conversion Status",
                "description": "AR owed, disputed, and expected to collect this month",
                "unit": "currency",
                "source_system": "AR aging report + deduction management system",
                "source_detail": (
                    "QuickBooks / NetSuite AR aging: split into three buckets — "
                    "clean AR (expected to collect), disputed AR (deductions under review), "
                    "and aged AR (>60 days, collection risk). "
                    "Deduction management: Vividly, BottomLine, or manual deduction log."
                ),
                "watch_for": (
                    "If disputed AR is growing as a percentage of total AR, your "
                    "deduction management process isn't keeping up. "
                    "At $15M+, unmanaged deductions can cost $300K–$600K annually."
                ),
                "gotcha": (
                    "Do not net deductions against revenue in your weekly pulse — "
                    "track them separately so you see the gross deduction rate. "
                    "Netting hides whether the problem is getting worse."
                ),
            },
            {
                "label": "Growth Pipeline",
                "description": "New retailer timelines and capacity utilization against expansion plan",
                "unit": "text",
                "source_system": "Your sales pipeline tracker + 3PL / co-man capacity reports",
                "source_detail": (
                    "Sales pipeline: your CRM or sales spreadsheet — filter to "
                    "'new retailer' opportunities with expected first-ship date. "
                    "Capacity: 3PL monthly summary or co-manufacturer run schedule "
                    "for the next 8 weeks."
                ),
                "watch_for": (
                    "If a new retailer first-ship date slips more than 2 weeks, "
                    "it often signals a deeper problem — insufficient inventory, "
                    "slotting fee not yet paid, or a buyer change. Flag it early."
                ),
                "gotcha": (
                    "Co-manufacturer capacity commitments are often verbal. "
                    "Get run dates in writing 8 weeks out or you will not have "
                    "inventory for a new retailer launch."
                ),
            },
        ],
    },
}

# Ordered list of tier keys for display sequencing
TIER_ORDER = ["$3M–$10M", "$10M–$15M", "$15M–$20M"]
