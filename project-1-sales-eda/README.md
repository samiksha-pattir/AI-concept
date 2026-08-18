# Sales Data EDA

A simple exploratory data analysis (EDA) project analyzing sales data by city and by product, using Pandas for aggregation and Matplotlib for visualization.

## What it does
- Groups raw sales records by **city** and by **product**
- Calculates total sales per group with Pandas `groupby`
- Generates bar charts showing sales distribution across categories
- Identifies the top-performing city and product

## Tech used
Python, Pandas, Matplotlib, NumPy

## Files
- `Visualization.py` — main analysis script
- `sales_chart.png` — total sales by city
- `prod_chart.png` — total sales by product

## Insights
- Delhi has the highest total sales among cities (₹440), followed by Blr (₹290) and Mumbai (₹70)
- Wire and laptop are the top-selling products by total sales value

## How to run
```bash
python3 -m venv venv
source venv/bin/activate
pip install pandas matplotlib numpy
python Visualization.py
```
