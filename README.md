# SEC Financial Analysis Tool

A beginner-friendly Python project that pulls public company financial
statements from the SEC, organizes the data into Excel-style tables, and
creates charts.

This project is designed for people who are learning finance, Python, data
analysis, or all three.

## What This Program Does

The program asks for a stock ticker, such as `AAPL` or `MSFT`, then:

- pulls SEC financial statement data with EdgarTools
- organizes the data with pandas
- creates an Excel workbook with clean sheets
- creates Excel-native charts with openpyxl
- creates chart images with matplotlib
- saves each company in its own folder
- explains what periods were available and selected
- includes beginner explanations of common financial terms

After one company finishes, the program asks if you want to analyze another
company.

## Important Limitation

This tool works best with public operating companies, such as:

```text
AAPL
MSFT
TSLA
AMZN
NVDA
```

Some tickers may not work, especially ETFs, funds, indexes, or trusts. For
example, `QQQ` is an ETF, not a normal operating company, so it may not have the
same income statement, balance sheet, and cash flow statement structure that
this project expects.

If a ticker does not work, the program will explain the most likely reasons and
let you try another ticker.

## What The Program Creates

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

The Excel workbook includes:

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

## Requirements

You need Python installed on your computer.

The project uses these Python libraries:

- EdgarTools
- pandas
- matplotlib
- Beautiful Soup
- openpyxl

## Install

Run this command in Terminal from inside the project folder:

```bash
python3 -m pip install -r requirements.txt
```

This installs the Python libraries listed in `requirements.txt`.

## Run From Terminal

```bash
python3 main.py
```

## Run From IDLE

1. Open IDLE.
2. Click `File > Open`.
3. Open `main.py`.
4. Press `F5`.

Do not type `python3 main.py` inside IDLE. That command is for Terminal.

## What The Program Asks For

The program asks:

1. Your SEC identity, usually your name and email.
2. How many recent reporting periods to analyze. The maximum is `3`.
3. A ticker symbol, such as `AAPL`.
4. Whether you want to analyze another company.

## SEC Identity

The SEC asks automated tools to identify who is making requests.

You can set your identity in Terminal:

```bash
export EDGAR_IDENTITY="Your Name your.email@example.com"
```

If you do not set this first, the program will ask you to type your name and
email when it runs.

## How To Share This Project

If sharing on GitHub, upload:

```text
main.py
requirements.txt
README.md
.gitignore
```

Do not upload generated data folders unless you intentionally want to share
your outputs:

```text
outputs/
.edgar_data/
.edgar_cache/
.matplotlib_cache/
__pycache__/
```

The `.gitignore` file is included to help Git ignore those local/generated
files.

## Good GitHub Description

```text
A beginner-friendly Python financial analysis tool that pulls SEC data with EdgarTools, organizes statements with pandas, exports Excel workbooks, and creates charts with matplotlib and openpyxl.
```

## LinkedIn Project Summary

I built a Python financial analysis tool that pulls public company financial
statements from the SEC using EdgarTools, organizes the data with pandas,
exports Excel workbooks, and creates charts with matplotlib and openpyxl. The
project helped me practice financial statement analysis, data cleaning, Excel
automation, and data visualization.

## Library Roles

- EdgarTools pulls SEC financial statement data.
- pandas organizes the data into tables.
- Beautiful Soup is available for future SEC filing HTML text extraction.
- matplotlib saves chart images.
- openpyxl formats the Excel workbook and adds Excel-native charts.
