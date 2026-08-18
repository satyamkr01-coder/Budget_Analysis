

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Budget data (2022-23 to 2026-27)

years = ["2022-23", "2023-24", "2024-25", "2025-26 (RE)", "2026-27 (BE)"]
tax_revenue = [18.7, 20.7, 22.3, 23.4, 26.2]          # in lakh crore
total_receipts = [22.84, 27.83, 31.47, 31.47, 36.52]   # in lakh crore
total_expenditure = [39.45, 44.43, 47.16, 50.65, 53.47] # in lakh crore
fiscal_deficit = [6.4, 5.6, 4.8, 4.4, 4.3]             # % of GDP

budget_df = pd.DataFrame({
    "Year": years,
    "Tax_Revenue": tax_revenue,
    "Total_Receipts": total_receipts,
    "Total_Expenditure": total_expenditure,
    "Fiscal_Deficit_%": fiscal_deficit
})

print("Budget Data:")
print(budget_df)


# Sector-wise expenditure for 2026-27 (in crore)    

sectors = ["Transport", "Defence", "Rural Development", "Home Affairs",
           "Agriculture", "Education", "Energy", "Health"]
allocation_crore = [598520, 594585, 273108, 255234, 162671, 139289, 109029, 104599]

sector_df = pd.DataFrame({
    "Sector": sectors,
    "Allocation_Crore": allocation_crore
})

# convert to lakh crore for easier reading
sector_df["Allocation_Lakh_Crore"] = sector_df["Allocation_Crore"] / 100000

# sort sectors from highest to lowest spending
sector_df = sector_df.sort_values("Allocation_Crore", ascending=False)

print("\nSector-wise Expenditure (2026-27):")
print(sector_df)


#Basic analysis using NumPy

# growth rate of expenditure year by year
expenditure_growth = []
for i in range(1, len(total_expenditure)):
    growth = ((total_expenditure[i] - total_expenditure[i-1]) / total_expenditure[i-1]) * 100
    expenditure_growth.append(round(growth, 2))

avg_growth = np.mean(expenditure_growth)
avg_deficit = np.mean(fiscal_deficit)

# which sector gets the highest funding
top_sector = sector_df.iloc[0]["Sector"]
top_sector_value = sector_df.iloc[0]["Allocation_Crore"]
total_sector_spend = sum(allocation_crore)
top_sector_share = (top_sector_value / total_sector_spend) * 100

print("\n--- Key Insights ---")
print("Year-wise expenditure growth %:", expenditure_growth)
print("Average expenditure growth rate: {:.2f}%".format(avg_growth))
print("Average fiscal deficit (% of GDP): {:.2f}%".format(avg_deficit))
print("Top funded sector in 2026-27:", top_sector, "with {:.1f}% of total sector spending".format(top_sector_share))


#Visualization using Matplotlib

plt.figure(figsize=(12, 8))

# Chart 1: Receipts vs Expenditure
plt.subplot(2, 2, 1)
plt.plot(years, total_receipts, marker='o', label="Total Receipts")
plt.plot(years, total_expenditure, marker='o', label="Total Expenditure")
plt.title("Receipts vs Expenditure (Lakh Crore)")
plt.xticks(rotation=30)
plt.legend()
plt.grid(True)

# Chart 2: Fiscal Deficit trend
plt.subplot(2, 2, 2)
plt.bar(years, fiscal_deficit, color="red")
plt.title("Fiscal Deficit (% of GDP)")
plt.xticks(rotation=30)
plt.grid(True)

# Chart 3: Sector-wise expenditure
plt.subplot(2, 2, 3)
plt.barh(sector_df["Sector"], sector_df["Allocation_Lakh_Crore"], color="green")
plt.title("Sector-wise Expenditure 2026-27 (Lakh Crore)")
plt.gca().invert_yaxis()

# Chart 4: Tax revenue growth
plt.subplot(2, 2, 4)
plt.plot(years, tax_revenue, marker='s', color="orange")
plt.title("Tax Revenue Growth")
plt.xticks(rotation=30)
plt.grid(True)

plt.tight_layout()
plt.savefig("budget_analysis_charts.png")
print("\nCharts saved as budget_analysis_charts.png")

plt.show()