# Day 10 - Feature Engineering & Pipelines
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression



# ==========================================
# Concept 1: OneHotEncoder
# ==========================================

# What is OneHotEncoder?
# OneHotEncoder converts text categories into numbers
# that a Machine Learning model can understand.

# Why do we use it?
# Models understand numbers, not text.
# Also, converting categories like
# Delhi=1, Mumbai=2, Bangalore=3
# creates a false order.

# OneHotEncoder creates one column
# for each category.

# Example:

# Before:
# City
# Delhi
# Mumbai
# Bangalore

# After:
# Delhi  Mumbai  Bangalore
#   1      0        0
#   0      1        0
#   0      0        1

# 1 = This category is present.
# 0 = This category is not present.
# data = pd.DataFrame({"city": ["Delhi", "Mumbai", "Blr", "Delhi","Goa"]})
# encoder=OneHotEncoder(sparse_output=False)
# encoded=encoder.fit_transform(data[["city"]])
# print(encoded)
# print(encoder.get_feature_names_out())
# # df=pd.DataFrame(data)
# # print(df)


# ==========================================
# Concept 2: StandardScaler
# ==========================================

# What is StandardScaler?
# Rescales numeric values so they are centered around 0,
# with a similar spread - instead of raw units (e.g. sq ft).

# Why do we use it?
# If one numeric column has much bigger values than another,
# models can wrongly treat it as "more important" just because
# of its size. Scaling puts every numeric feature on equal footing.

# data = [[10], [20], [30], [40], [50]]

# scaler=StandardScaler()

# scaled_data = scaler.fit_transform(data)
# print(scaled_data)





# ==========================================
# Concept 3: ColumnTransformer
# ==========================================

# What is ColumnTransformer?
# Applies different preprocessing to different columns in one step -
# e.g. OneHotEncoder on a text column and StandardScaler on a numeric
# column, combined into a single transformer.

# Why do we use it?
# Real datasets mix text and numbers. Doing this manually (slice,
# transform, merge back) is error-prone - ColumnTransformer does it
# cleanly in one object.

# data=pd.DataFrame({
#     "city":["delhi","mumbai", "bangalore", "goa", "mysor"],
#     "size":[1200, 4000, 3000, 1234, 1020]
# })
# print(data)
# #                  DATA
# #                   ↓
# #         ┌─────────────────┐
# #         │                 │
# #       city              size
# #         ↓                 ↓
# # OneHotEncoder       StandardScaler
# #         ↓                 ↓
# #    0 / 1 columns     Scaled numbers(mean/avg or StandardScaler)
# #         └───────┬─────────┘
# #                 ↓
# #          Combined Result
# #                 ↓
# #           Model-ready data

# preprocessor=ColumnTransformer([
#     ("cat", OneHotEncoder(sparse_output=False),["city"]),
#     ("num", StandardScaler(),["size"])
# ])

# print(preprocessor.fit_transform(data))


# ==========================================
# Concept 4: Pipeline
# ==========================================

# What is Pipeline?
# Chains preprocessing and the model together into ONE object -
# call fit() once instead of doing steps manually in order.

# Why do we use it?
# Manually preprocessing then fitting = easy to make mistakes
# (e.g. accidentally scaling train/test differently). Pipeline
# guarantees the same steps run in the same order, every time.

        #          Pipeline
        #             ↓
        #   ┌──────────────────┐
        #   │ ColumnTransformer│
        #   │                  │
        #   │ city → OneHot    │
        #   │ size → Scaler    │
        #   └────────┬─────────┘
        #            ↓
        #       ML Model
        #            ↓
        #        Prediction

    # pipeline: instead of separately managing preprocessing and the model, we put them into one workflow.


# Input data
x = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]

# Correct answers
y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# Split data
# 80% → Training
# 20% → Testing

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2
)


# Create Pipeline
# Here we only have one step:
# Linear Regression

pipeline = Pipeline([
    ("regression", LinearRegression())
])


# Train the model

pipeline.fit(x_train, y_train)


# Predict on unseen test data

prediction = pipeline.predict(x_test)


# Print predictions

print("Predicted:", prediction)

# Print actual answers

print("Actual:", y_test)


# Data
#  ↓
# Train/Test Split
#  ↓
# 80% Training ──→ Pipeline ──→ LinearRegression learns
#                                       ↓
# 20% Testing ─────────────────→ Prediction


# ==========================================
# Recruiter Challenge: Data Leakage
# ==========================================

# Bug: fitting a scaler on the WHOLE dataset before train_test_split
# leaks test-set information into training (the mean/std were computed
# using test rows too).
#
# scaler.fit_transform(data)                     # BAD - fit on everything first
# X_train, X_test, y_train, y_test = train_test_split(data_scaled, y)
#
# Fix: split first, then fit the scaler ONLY on training data.
# Test data only ever gets transform() (never fit) with what the
# scaler already learned from train.
#
# X_train, X_test, y_train, y_test = train_test_split(data, y)
# scaler.fit(X_train)
# X_train_scaled = scaler.transform(X_train)
# X_test_scaled = scaler.transform(X_test)