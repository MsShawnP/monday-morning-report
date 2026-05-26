# Using the Monday Morning Report in Google Sheets

The template is built as an Excel file (`.xlsx`). Most features transfer cleanly when you import it into Google Sheets. Follow these steps.

---

## Import Steps

1. Go to [sheets.google.com](https://sheets.google.com) and open a blank spreadsheet.
2. **File → Import → Upload** — select `monday-morning-report.xlsx`.
3. In the import dialog, choose:
   - **Import location:** Insert new sheet(s)
   - **Convert text, numbers, and formulas:** Yes
4. Click **Import data**.

---

## After Importing

**Set the font.** Source Sans 3 is available in Google Sheets. Select all cells (Ctrl+A), then Format → Font → type "Source Sans 3".

**Reapply trend arrow colors.** Conditional formatting for the trend arrows (↑ teal, ↓ red, → grey) may not transfer. To reapply in Sheets:
- Select cell D5 (first trend arrow)
- Format → Conditional formatting
- Add a rule: "Text is exactly ↑" → Custom color `#158F75`
- Add a rule: "Text is exactly ↓" → Custom color `#CC100A`
- Add a rule: "Text is exactly →" → Custom color `#666666`
- Repeat for D8 and D11

**Tier selector.** The dropdown on the Setup tab should work as-is. If it doesn't, re-create it: Data → Data validation → Dropdown (from list) → enter `$3M–$10M,$10M–$15M,$15M–$20M`.

---

## Known Gaps

- The `_Config` hidden sheet that drives the dynamic metric labels may not translate perfectly in all Sheets versions. If labels show as errors on the This Week tab, manually type your three metric labels directly into cells A5, A8, and A11 on the This Week tab.
- Print headers/footers don't transfer — set them via File → Print → Headers & footers if needed.
