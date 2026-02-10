"""
Project Title: Automated Sales Intelligence & Distribution Analytics Tool
Developer: Zafaran shah
Goal: Analyzing Sales Data from Month.xlsx
"""

import pandas as pd
import matplotlib.pyplot as plt

# --- STEP 1: LOAD DATA ---
# Changed to header=0 because your data starts from the very first row
file_name = 'Month sale.xlsx' 
try:
    df = pd.read_excel(file_name, header=0)
    # Cleaning column names (removing any hidden spaces)
    df.columns = df.columns.str.strip()
    print("✅ Data Loaded and Column Names Cleaned!")
except Exception as e:
    print(f"❌ Error loading file: {e}")

# --- STEP 2: DATA CLEANING ---
# Filling empty cells with 0 and filtering out the 'Total' row
df['Net Sales'] = df['Net Sales'].fillna(0)
df['Sold QTY (Cartons)'] = df['Sold QTY (Cartons)'].fillna(0)

# Removing the 'Total' row so it doesn't mess up our graphs
df_cleaned = df[df['Brand Name'] != 'Total']

# --- STEP 3: ANALYSIS ---
brand_sales = df_cleaned.groupby('Brand Name')['Net Sales'].sum().sort_values(ascending=False)
brand_qty = df_cleaned.groupby('Brand Name')['Sold QTY (Cartons)'].sum().sort_values(ascending=False)

# --- STEP 4: DISPLAY RESULTS ---
print("\n--- TOP BRANDS BY REVENUE ---")
print(brand_sales.head(10))

print("\n--- STRATEGIC INSIGHT ---")
print("High sales revenue does not always mean high quantity sold; pricing plays a key role.")

# --- STEP 5: VISUALIZATION ---
plt.figure(figsize=(12, 6))
brand_sales.head(10).plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Top 10 Brands by Net Sales (from Month.xlsx)', fontsize=14)
plt.xlabel('Brand Name', fontsize=12)
plt.ylabel('Net Sales', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Saving and showing the graph
plt.savefig('Final_Sales_Report.png')
plt.show()

print("\n✅ Project Successful! Graph saved as 'Final_Sales_Report.png'")