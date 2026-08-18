import pandas as pd
import numpy as np
# # Concept 1: Series & DataFrame
Series = a single column of data (1D)
DataFrame = a full table with rows and columns, like an Excel sheet
s=pd.Series([10,20,30])
# print(s)

data={
    "name":["anu", "rohan", "meena"],
    "marks":[70,41,30],
    "subject":["hindi", "Eng", "Kanada"]
}
df=pd.DataFrame(data)
# print(df)
print(df["marks"])
print(df.describe())      # stats (mean, min, max, etc) for numeric columns only


# Concept 2: loc vs iloc
# What: Two ways to select rows/columns from a DataFrame — loc selects by label
# (index name or column name), iloc selects by integer position (0, 1, 2...).

# Why: Real datasets often have custom index labels (dates, IDs, names)
# instead of plain 0,1,2 — loc lets you fetch by that meaningful label, while iloc always works by pure position regardless of what the index looks like. Interviewers test this because mixing them up is a common bug.

data={
    "name":["anu", "rohan", "meena"],
    "marks":[70,41,30],
    "subject":["hindi", "Eng", "Kanada"]
}
df=pd.DataFrame(data)
print(len(df))
# print(df.loc[0])
print(df[df["marks"]>40])   # filtering: same idea as NumPy boolean indexing

#   name       marks   subject
# 0   anu      70      hindi
# 1  rohan     41      Eng
# 2  meena     30      Kanada


# Concept 3: Missing values (NaN)
# What: Pandas represents missing data as NaN (Not a Number)
# Why: Leaving NaN in place breaks calculations (math with NaN gives NaN back),
# so it must be cleaned before analysis/modeling

students={
    "name":["anu", "rohan", "meena"],
    "marks":[70,np.nan,30],
    # "subject":["hindi", "Eng", "Kanada"]
}

df=pd.DataFrame(students)
print(df)


print(df.isna())                 # True/False, shows where NaN is
print(df.dropna())                # removes rows that have NaN
print(df["marks"].fillna(df["marks"].mean()))   # fills NaN with the column average


# Concept 4: groupby
# What: Groups rows by the value in one column, then applies an aggregate (sum/mean/count) to each group.
# Why: Answers questions like "what is the average marks per subject" — same idea as an Excel Pivot Table.
data = {
    "subject": ["Math", "Math", "Eng", "Eng"],
    "marks": [80, 60, 70, 90]
}
df = pd.DataFrame(data)

print(df.groupby("subject")["marks"].mean())


# sales data analyzer
# find total sales per product, then the top-selling product

sd = {
    "city": ["Delhi", "Delhi", "Mumbai", "Blr", "Delhi", "Blr"],
    "sales": [80, 60, 70, 90,300,200],
    "product":["laptop","mouse","laptop","wire","laptop","laptop"]
}

d=pd.DataFrame(sd)
# print(d)
print(d.groupby("city")["sales"].sum())
pv=d.groupby("product")["sales"].sum().max()      # highest total sales value
pn=d.groupby("product")["sales"].sum().idxmax()   # name of the product with highest sales
print(f"{pn} has maximum sales = {pv}")
