FMCG Sales Intelligence & Distribution Tool
📌 Project Overview

This project is a real-world data analysis tool developed using Python to analyze FMCG (Fast-Moving Consumer Goods) sales and distribution data. The motivation behind this project comes from my 6 years of hands-on experience as a Computer Operator, where I observed that large volumes of sales data were being recorded but not meaningfully analyzed.

The goal of this project is to transform raw Excel-based sales data into actionable business insights that can support better pricing, distribution, and decision-making.

🎯 Objectives

Clean and preprocess messy FMCG sales data

Automate repetitive Excel-based reporting tasks

Analyze brand-wise sales performance

Visualize trends to support management decisions

Lay the foundation for advanced analytics such as shop-level demand prediction

📊 Dataset Description

The dataset (Month sale.xlsx) represents monthly FMCG distribution data, including:

Brand Name

Net Sales

Sold Quantity (Cartons)

The data contains missing values and unstructured entries, reflecting real operational data rather than a synthetic dataset.

🛠 Tools & Technologies Used

Python

Pandas – Data cleaning and manipulation

Matplotlib – Data visualization

Microsoft Excel – Source data

GitHub – Version control and documentation

🔍 Key Steps Performed

Imported Excel sales data using Pandas

Handled missing values to ensure accurate analysis

Aggregated brand-wise net sales

Identified top-performing brands

Generated visual bar charts for sales comparison

Exported graphs for reporting and presentation

📈 Key Insight

High sales volume does not always mean high revenue.
Pricing strategy plays a crucial role in determining overall profitability.

This insight highlights the importance of analyzing both quantity and revenue rather than relying on volume alone.

🖼 Sample Output

The project generates visual outputs such as:

Top 10 Brands by Net Sales (Bar Chart)
<img width="1143" height="348" alt="image" src="https://github.com/user-attachments/assets/32015f43-ce77-4cee-acb0-f31c64abc716" />


These visuals help non-technical stakeholders quickly understand performance trends.

▶ How to Run the Project

Clone this repository

Install required libraries:

pip install pandas matplotlib numpy

Place the Excel file in the project directory

Run the Python script:

python main.py
🚀 Future Enhancements

Shop-wise sales analysis

Fuzzy matching to group unorganized shop names

Territory-level demand prediction

Integration with dashboards (Power BI / Streamlit)

👤 Author

Zafaran Shah
Computer Operator | Aspiring Data Scientist
GitHub: https://github.com/Zafiiii

📌 Note

This project represents my self-learning journey into data analytics and my transition from manual data entry to automated, insight-driven analysis.
