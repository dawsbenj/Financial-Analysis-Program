# Financial Analysis Tool

This beginner Python project pulls SEC financial statement data with
EdgarTools, organizes it with pandas, exports Excel-friendly files, and creates
charts with both matplotlib and openpyxl.

## What The Program Shows

The program helps you see:

- What company ticker you pulled.
- What reporting periods are available.
- What reporting periods were selected.
- Income statement data.
- Balance sheet data.
- Cash flow statement data.
- Key metrics over time.
- Beginner explanations of common financial terms.

## What It Creates

Each company gets its own output folder:

```text
outputs/AAPL/
  aapl_financial_analysis.xlsx
  metrics.csv
  periods.csv
  income_statement.csv
  balance_sheet.csv
  cash_flow_statement.csv
  charts/
    revenue.png
    net_income.png
    profit_margin.png
    cash_from_operations.png
    assets_vs_liabilities.png
```

The Excel workbook includes these sheets:

```text
metrics
periods
explanations
where_files_are_saved
income_statement
balance_sheet
cash_flow_statement
raw_income_statement
raw_balance_sheet
raw_cash_flow_statement
excel_charts
```

## Install

Run this in Terminal, not inside IDLE:

```bash
python3 -m pip install -r requirements.txt
```

## Run From Terminal

```bash
python3 main.py
```

## Run From IDLE

Open `main.py`, then press `F5`.

The program will ask for:

1. How many recent reporting periods to analyze. The maximum is `3`.
2. A ticker symbol, such as `AAPL`.
3. Your SEC identity if you did not already set `EDGAR_IDENTITY`.

## SEC Identity

The SEC expects automated tools to identify who is making requests. You can set
your identity in Terminal like this:

```bash
export EDGAR_IDENTITY="Your Name your.email@example.com"
```

If you use IDLE and did not set `EDGAR_IDENTITY`, the program will ask you to
type your name and email when it runs.

## Sharing

You can share this project by putting these files in a GitHub repository or a
ZIP file:

```text
main.py
requirements.txt
README.md
.gitignore
```

The generated `outputs/` folder is ignored so company files do not clutter the
repository.

Recommended share checklist:

- Share `main.py`, `requirements.txt`, `README.md`, and `.gitignore`.
- Do not share your generated `outputs/` folder unless you want people to see
  the company files you created.
- Do not hardcode your personal SEC identity in the code.
- Tell users to install the requirements before running the program.

## Library Roles

- EdgarTools pulls the SEC financial statements.
- pandas organizes the data into tables.
- Beautiful Soup is available for future SEC filing HTML text extraction.
- matplotlib saves chart images.
- openpyxl formats the Excel workbook and adds Excel-native charts.
