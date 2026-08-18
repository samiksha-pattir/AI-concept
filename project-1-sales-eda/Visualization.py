
import matplotlib.pyplot as plt
import pandas as pd
# Day 07 — Visualization + Ship Project 1

# Concept 1: matplotlib basics
# What: Python library to draw charts/graphs - bar chart, line chart, histogram, etc.
# Why: A table of numbers is hard to read for patterns - a chart shows trend,
# comparison, and outliers instantly. Also easier to present to non-technical stakeholders.

# Chart types:
# Bar chart - compare categories (e.g. sales by city)
# Line chart - see trend over time (e.g. sales by month)
# Histogram - see distribution of one column (e.g. how marks are spread)


# Chart 1: sales by city
data = {
    "city": ["Delhi", "Delhi", "Mumbai", "Blr", "Delhi", "Blr"],
    "sales": [80, 60, 70, 90, 300, 200]
}
df = pd.DataFrame(data)
city_sales = df.groupby("city")["sales"].sum()
print(city_sales)

plt.figure()   # new blank canvas so this chart doesn't mix with the next one
plt.bar(city_sales.index, city_sales.values)
plt.xlabel("city")
plt.ylabel("sales")
plt.title("sales by city")
plt.savefig("sales_chart.png")
print("saved city chart")


# Chart 2: sales by product
prd_data = {
    "product": ["laptop","phone","phone","mosuse","laptop","wire"],
    "sales": [100,200,300,400,600,700]
}
pdf = pd.DataFrame(prd_data)
print(pdf)

clc = pdf.groupby("product")["sales"].sum()
print(clc)

plt.figure()   # new blank canvas again, separate from the city chart
plt.bar(clc.index, clc.values)
plt.xlabel("product")
plt.ylabel("sales")
plt.title("sales by product")
plt.savefig("prod_chart.png")
print("done product chart")
