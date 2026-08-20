from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, recall_score, f1_score, precision_score
# ==========================================
# Machine Learning (ML) Overview
# ==========================================

# Data
# X = Input (Features)
# y = Correct Answer (Target)

# Train/Test Split
# Split the data into Training (80%) and Testing (20%).
# The model learns from training data.
# Test data is used later to check the model on unseen data.

# Feature Scaling
# Convert numerical features to a similar scale
# so that large values do not dominate smaller values.
# Useful for Linear Regression, Logistic Regression, KNN, and SVM.
# Not required for Decision Tree and Random Forest.

# Regression
# Regression predicts a numeric value.
# Example: House Price, Salary, Marks.

# Linear Regression
# A simple regression model that learns the relationship
# between X and y using the best-fit straight line.

# Classification
# Classification predicts a category or label.
# Example: Pass/Fail, Spam/Not Spam, Yes/No.

# Logistic Regression
# A classification model that first predicts a probability
# (0 to 1) and then converts it into a label
# using a threshold (usually 0.5 or 50%).

# fit()
# Train the model using X_train and y_train.

# predict()
# Predict answers for new/unseen test data.

# predictions
# The answers predicted by the model.

# y_test
# The actual correct answers used to compare predictions.

# Mean Squared Error (MSE)
# Measures the average squared error between actual
# and predicted values.
# Lower MSE is better. (0 = Perfect)

# R² Score
# Shows how well the model explains the data pattern.
# Closer to 1 is better.

# Overfitting
# The model memorizes training data.
# Training accuracy is high, but test accuracy is low.

# Underfitting
# The model is too simple to learn the pattern.
# Both training and test accuracy are low.

# Good Fit
# The model performs well on both training
# and test data, with similar accuracy.


# hours studied -> pass(1) or fail(0)
# hours = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
# result = [0,0,0,0,1,1,1,1,1,1]   # 0=fail, 1=pass

# hrs_train, hrs_test,res_train, res_test, =train_test_split(hours, result, test_size=0.2)
# print(hrs_train)
# print(res_train)


# model=LogisticRegression()
# model.fit(hrs_train,res_train)
# prediction=model.predict(hrs_test)
# print(f"this for testing - {hrs_test}")
# print(f"this is model predicting - {prediction}")
# print(f"this is actuall answer {res_test}")



# ==========================================
# Concept 2: Confusion Matrix
# ==========================================

# What is a Confusion Matrix?
# A Confusion Matrix is a table that shows
# how many predictions were correct and
# what types of mistakes the model made.
#
# It is mainly used for Classification problems.
#
# Example:
# Suppose we are predicting:
#
# Pass = Positive
# Fail = Negative
#
# There are 4 possible results:
#
# 1. True Positive (TP)
#    Actual = Pass
#    Predicted = Pass
#    Correct prediction
#
# 2. True Negative (TN)
#    Actual = Fail
#    Predicted = Fail
#    Correct prediction
#
# 3. False Positive (FP)
#    Actual = Fail
#    Predicted = Pass
#    Wrong prediction
#
# 4. False Negative (FN)
#    Actual = Pass
#    Predicted = Fail
#    Wrong prediction
#
#
# True  = Model prediction was correct
# False = Model prediction was wrong
#
# Positive = Pass
# Negative = Fail
#
#
# Why do we use Confusion Matrix?
# Accuracy only tells us how many predictions
# were correct.
#
# Confusion Matrix tells us exactly:
# - How many positives were correctly predicted
# - How many negatives were correctly predicted
# - How many false positives occurred
# - How many false negatives occurred
#
# This is especially useful when the data is imbalanced.

# hours = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
# result = [0,0,0,0,1,1,1,1,1,1]   # 0=fail, 1=pass

# hrs_train, hrs_test,res_train, res_test, =train_test_split(hours, result, test_size=0.2)
# print(hrs_train)
# print(res_train)


# model=LogisticRegression()
# model.fit(hrs_train,res_train)
# prediction=model.predict(hrs_test)
# acctual_ans=res_test
# print(f"this for testing - {hrs_test}")
# print(f"this is model predicting - {prediction}")
# print(f"this is actuall answer {acctual_ans}")
# # print(confusion_matrix(acctual_ans, prediction))
# print(confusion_matrix(acctual_ans, prediction))
# # total predicted positive
# # Precision = Out of all Positive predictions,
# # how many were actually Positive?
# # Precision = TP / (TP + FP)
# print(precision_score(acctual_ans, prediction))# 
# print
# # Actual Fail → Predicted Fail = TN ✅
# # Actual Pass → Predicted Fail = FN ❌
# # Actual Fail → Predicted Pass = FP ❌

# print(precision_score(acctual_ans, prediction))
# print(recall_score(acctual_ans, prediction))
# print(f1_score(acctual_ans, prediction))


# ==========================================
# Day 9 Mini Project: Class Imbalance
# ==========================================

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score


# ------------------------------------------
# Step 1: Create the data
# ------------------------------------------

# Study hours of 100 students
hours = [[i] for i in range(1, 101)]

# 0 = Fail
# 1 = Pass
#
# 90 students are Fail
# 10 students are Pass
#
# This is called Class Imbalance.

result = [0] * 90 + [1] * 10


# ------------------------------------------
# Step 2: Split the data
# ------------------------------------------

# 80% data → Training
# 20% data → Testing

X_train, X_test, y_train, y_test = train_test_split(
    hours,
    result,
    test_size=0.2
)


# ------------------------------------------
# Step 3: Create Logistic Regression model
# ------------------------------------------

# Logistic Regression is a classification model.
# It learns the pattern and predicts a class
# such as Fail (0) or Pass (1).

model = LogisticRegression()


# ------------------------------------------
# Step 4: Train the model
# ------------------------------------------

# Model learns from training data.

model.fit(X_train, y_train)


# ------------------------------------------
# Step 5: Make predictions
# ------------------------------------------

# Model predicts the result for unseen test data.

predictions = model.predict(X_test)


# ------------------------------------------
# Step 6: Confusion Matrix
# ------------------------------------------

# Shows:
# TP = True Positive
# TN = True Negative
# FP = False Positive
# FN = False Negative

print(confusion_matrix(y_test, predictions, labels=[0, 1]))


# ------------------------------------------
# Step 7: Accuracy
# ------------------------------------------

# Shows how many predictions were correct overall.

print("Accuracy:", model.score(X_test, y_test))


# ------------------------------------------
# Step 8: Precision
# ------------------------------------------

# Out of all students predicted as Pass,
# how many were actually Pass?

print("Precision:", precision_score(y_test, predictions))


# ------------------------------------------
# Step 9: Recall
# ------------------------------------------

# Out of all students who were actually Pass,
# how many did the model correctly identify as Pass?

print("Recall:", recall_score(y_test, predictions))