import pandas as pd

# Pandas Advanced
# Concept 1: pivot_table

# What: Builds a table where
# rows = unique values of one column,
# columns = unique values of another column, and the cells hold an aggregate value (sum/mean/count).


# data = {
#     "city": ["Delhi","Delhi","Mumbai","Mumbai"],
#     "product": ["Phone","Laptop","Phone","Laptop"],
#     "sales": [100, 200, 150, 250]
# }
# df = pd.DataFrame(data)

# print(df.pivot_table(values="sales", index="city", columns="product", aggfunc="sum"))


# sd = {
#     "city": ["Delhi", "Delhi", "Mumbai", "Blr", "Delhi", "Blr"],
#     "sales": [80, 60, 70, 90, 300, 200],
#     "product": ["laptop","mouse","laptop","wire","laptop","laptop"]
# }
# d = pd.DataFrame(sd)

# print(d.pivot_table(values="sales", index="city", columns="product", aggfunc="sum"))


# Concept 2: Datetime handling
# What: Pandas converts date/time text into a special datetime type,
# which makes date-based operations (filter by month, sort by date, date differences) easy.


# # data = {
# #     "date": ["2024-01-15", "2024-02-20", "2024-01-25"],
# #     "sales": [100, 200, 150]
# # }
# # df = pd.DataFrame(data)
# # print(pd.DataFrame(df))
# # df["date"]=pd.to_datetime(df["date"])
# # print(df["date"].dt.month)
# # print(df[df["date"].dt.month==1])



sd={
    "date": ["2024-01-15", "2024-02-20", "2024-01-25", "2024-10-20"],
    "sales": [100, 200, 150,300]
}

df=pd.DataFrame(sd)
# df["date"]=pd.to_datetime(df["date"])
# print(df[df["date"].dt.month==1])


# Recruiter challenge: apply() vs vectorized operation
# apply() runs the function row by row - slow, loop-like under the hood
df["sales_with_tax_slow"] = df["sales"].apply(lambda x: x * 1.18)
print(df["sales_with_tax_slow"])

# direct multiply is vectorized - runs on the whole column at once, same result but faster
df["sales_with_tax_fast"] = df["sales"] * 1.18
print(df["sales_with_tax_fast"])
