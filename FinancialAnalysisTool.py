Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> 
= RESTART: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/main.py

Financial Analysis Tool
Running file: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/main.py
This tool works best with public operating companies, like AAPL or MSFT.
ETFs, funds, and indexes, like QQQ, may not have the same financial statements.

--- SEC Identity ---
The SEC asks programs to identify who is making requests.
Enter your name and email, like: Jane Doe jane@example.com
SEC identity: daws.benj@gmail.com

--- Time Period Selection ---
This program can pull up to 3 recent annual reporting periods.
Example: enter 3 to see the 3 most recent annual reporting periods.
Note: some statements may have fewer periods available than you request.
How many recent reporting periods do you want to analyze? Max is 3: 3

Enter a ticker symbol, like AAPL or MSFT: MSFT

--- Reporting Periods ---
          Statement  Requested Periods  Available Periods                   Selected Periods                                         Note
   Income Statement                  3                  3 2025-06-30, 2024-06-30, 2023-06-30            Requested periods were available.
      Balance Sheet                  3                  2             2025-06-30, 2024-06-30 Fewer periods were available than requested.
Cash Flow Statement                  3                  3 2025-06-30, 2024-06-30, 2023-06-30            Requested periods were available.

--- Period Availability Explanation ---
The program could not show every period you requested for every statement.
That usually happens because the SEC filing only includes a limited
number of comparable periods for that statement.
For example, balance sheets often show fewer dates than income statements.
- Balance Sheet: you asked for 3, but only 2 were available.

--- Income Statement ---
                  Line Item         2025-06-30         2024-06-30         2023-06-30
                    Revenue 281,724,000,000.00 245,122,000,000.00 211,915,000,000.00
            Cost of revenue  87,831,000,000.00  74,114,000,000.00  65,863,000,000.00
               Gross margin 193,893,000,000.00 171,008,000,000.00 146,052,000,000.00
   Research and development  32,488,000,000.00  29,510,000,000.00  27,195,000,000.00
        Sales and marketing  25,654,000,000.00  24,456,000,000.00  22,759,000,000.00
 General and administrative   7,223,000,000.00   7,609,000,000.00   7,575,000,000.00
           Operating income 128,528,000,000.00 109,433,000,000.00  88,523,000,000.00
Other income (expense), net  -4,901,000,000.00  -1,646,000,000.00     788,000,000.00
 Income before income taxes 123,627,000,000.00 107,787,000,000.00  89,311,000,000.00
 Provision for income taxes  21,795,000,000.00  19,651,000,000.00  16,950,000,000.00

--- Balance Sheet ---
                                                                     Line Item         2025-06-30         2024-06-30
                                                                        Assets                                      
                                                               Current assets:                                      
                                                     Cash and cash equivalents  30,242,000,000.00  18,315,000,000.00
                                                        Short-term investments  64,323,000,000.00  57,228,000,000.00
                      Total cash, cash equivalents, and short-term investments  94,565,000,000.00  75,543,000,000.00
  Accounts receivable, net of allowance for doubtful accounts of $944 and $830  69,905,000,000.00  56,924,000,000.00
                                                                   Inventories     938,000,000.00   1,246,000,000.00
                                                          Other current assets  25,723,000,000.00  26,021,000,000.00
                                                          Total current assets 191,131,000,000.00 159,734,000,000.00
Property and equipment, net of accumulated depreciation of $93,653 and $76,421 204,966,000,000.00 135,591,000,000.00

--- Cash Flow Statement ---
                                                       Line Item         2025-06-30        2024-06-30        2023-06-30
                                                      Operations                                                       
                                                      Net income 101,832,000,000.00 88,136,000,000.00 72,361,000,000.00
Adjustments to reconcile net income to net cash from operations:                                                       
                           Depreciation, amortization, and other  34,153,000,000.00 22,287,000,000.00 13,861,000,000.00
                                Stock-based compensation expense  11,974,000,000.00 10,734,000,000.00  9,611,000,000.00
            Net recognized losses on investments and derivatives    -609,000,000.00   -305,000,000.00   -196,000,000.00
                                           Deferred income taxes  -7,056,000,000.00 -4,738,000,000.00 -6,059,000,000.00
                    Changes in operating assets and liabilities:                                                       
                                             Accounts receivable  10,581,000,000.00  7,191,000,000.00  4,087,000,000.00
                                                     Inventories    -309,000,000.00 -1,284,000,000.00 -1,242,000,000.00

--- Metrics Table ---
                             2023-06-30         2024-06-30         2025-06-30
Metric                                                                       
Revenue              211,915,000,000.00 245,122,000,000.00 281,724,000,000.00
Net Income            72,361,000,000.00  88,136,000,000.00 101,832,000,000.00
Income Tax Expense    16,950,000,000.00  19,651,000,000.00  21,795,000,000.00
Total Assets                        NaN 512,163,000,000.00 619,003,000,000.00
Total Liabilities                   NaN 243,686,000,000.00 275,524,000,000.00
Total Equity                        NaN                NaN                NaN
Cash From Operations                NaN                NaN                NaN
Capital Expenditures                NaN                NaN                NaN
Profit Margin                     34.15              35.96              36.15
Debt To Equity                      NaN                NaN                NaN
Saved CSV file to: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/outputs/MSFT/metrics.csv
Saved CSV file to: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/outputs/MSFT/periods.csv
Saved CSV file to: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/outputs/MSFT/income_statement.csv
Saved CSV file to: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/outputs/MSFT/balance_sheet.csv
Saved CSV file to: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/outputs/MSFT/cash_flow_statement.csv

Saved Excel workbook to: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/outputs/MSFT/msft_financial_analysis.xlsx
Saved chart image to: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/outputs/MSFT/charts/revenue.png
Saved chart image to: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/outputs/MSFT/charts/net_income.png
Saved chart image to: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/outputs/MSFT/charts/profit_margin.png
Skipped MSFT Cash From Operations chart because no data was found.
Saved chart image to: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/outputs/MSFT/charts/assets_vs_liabilities.png

Done.
Open this folder to find everything: /Users/dawsben/Documents/Codex/2026-04-29/i-am-building-a-beginner-python/outputs/MSFT

