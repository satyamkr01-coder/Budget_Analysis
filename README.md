# Indian Budget - Comprehensive Data Analysis

A Python project that analyzes India's Union Budget data from 2022-23 to
2026-27, including government receipts, expenditure, fiscal deficit, and
sector-wise spending.

## What this project does

- Stores budget data (receipts, expenditure, tax revenue, fiscal deficit) for the last 5 budgets
- Stores sector-wise spending data for 2026-27 (Transport, Defence, Education, Health, etc.)
- Calculates year-on-year growth in government expenditure
- Calculates average fiscal deficit and the top funded sector
- Plots 4 charts to visualize all of the above

## Tech used

- Python 3
- pandas
- NumPy
- Matplotlib

## How to run it

1. Install the required libraries:
```
pip install pandas numpy matplotlib
```

2. Run the script:
```
python budget_analysis.py
```

3. It will print the data tables and insights in the terminal, and save a
chart image called `budget_analysis_charts.png` in the same folder.

## Data source

The budget figures used in this project are real numbers taken from:
- Union Budget documents (indiabudget.gov.in)
- PRS Legislative Research budget analyses (prsindia.org)

## Author

Satyam Kumar
B.Tech CSE (AI & ML), Guru Nanak Institute of Technology
