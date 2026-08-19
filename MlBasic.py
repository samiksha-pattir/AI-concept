from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ===========================
# Day 8 — ML Basics: Regression Pipeline
# ===========================

# # ===========================
# # Machine Learning (ML) Basics
# # ===========================

# # What is Machine Learning?
# # Machine Learning (ML) is a way of teaching a computer using data
# # instead of writing fixed rules.
# #
# # Example:
# # Normal Programming: If age > 18 -> Adult
# # Machine Learning: Give the computer many examples, and it learns
# # the pattern by itself to make predictions.


# # ===========================
# # Concept 1: Train/Test Split
# # ===========================

# # What is Train/Test Split?
# # We divide the dataset into two parts:
# #
# # 1. Training Data - The model learns from this data.
# # 2. Test Data - The model has never seen this data before.
# #    We use it to check how well the model learned.

# # Why do we use it?
# # If we train and test on the same data, the model may only
# # memorize the answers instead of learning the pattern.
# #
# # A separate test set shows how well the model performs on
# # new, unseen data, which is the real-world use case.

# # Example:
# # Training Data = Practice questions
# # Test Data = Real exam
# #
# # A good model should perform well on both practice and new questions.
# x = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
# y = [10,20,30,40,50,60,70,80,90,100]
# # X = model ko diya gaya input
# # y = us input ka correct answer


# x_train,x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
# # → 8 data = Training 🧠
# # → 2 data = Testing 📝

# print(x_train)
# print(x_test)


# print(y_train)
# print(y_test)



# # ==========================================
# # Concept 2: Linear Regression
# # ==========================================

# # What is Linear Regression?
# #
# # Linear Regression is a Machine Learning model
# # that finds a relationship/pattern between input (X)
# # and output (y).
# #
# # It tries to find the best straight line through
# # the given data points.
# #
# # Then it uses this pattern to predict the output
# # for new data.
# #
# #
# # Simple Example:
# #
# # Suppose we have:
# #
# # X = Hours studied
# # y = Exam marks
# #
# # Hours studied     Marks
# #      1              10
# #      2              20
# #      3              30
# #      4              40
# #
# # The model can learn the pattern:
# #
# # More study hours → More marks
# #
# # Then if we give:
# #
# # Hours studied = 5
# #
# # The model may predict:
# #
# # Marks = 50
# #
# #
# # Real-Life Example:
# #
# # Imagine a shop owner wants to predict
# # the price of a house based on its size.
# #
# # X = House size
# # y = House price
# #
# # The model looks at old house data,
# # learns the relationship between size and price,
# # and then predicts the price of a new house.
# #
# #
# # ==========================================
# # Step 1: Import Linear Regression
# # ==========================================

# from sklearn.linear_model import LinearRegression


# # ==========================================
# # Step 2: Create the Model
# # ==========================================

# model = LinearRegression()

# # We have created an empty Linear Regression model.
# # It has not learned anything yet.


# # ==========================================
# # Step 3: Train the Model
# # ==========================================

# model.fit(X_train, y_train)

# # fit() means TRAIN / LEARN.
# #
# # The model looks at X_train and y_train
# # and learns the relationship between them.
# #
# # Example:
# # X_train = [1, 2, 4, 5]
# # y_train = [10, 20, 40, 50]
# #
# # The model learns:
# # X × 10 = y
# #
# # After fit(), the model has learned this pattern.


# # ==========================================
# # Step 4: Make Predictions
# # ==========================================

# predictions = model.predict(X_test)

# # predict() means:
# # "Use what you learned and make a prediction
# # for new/unseen data."
# #
# # X_test contains data that the model
# # did NOT use during training.
# #
# # Example:
# # X_test = [3, 8]
# #
# # The model may predict:
# # 3 → 30
# # 8 → 80


# # ==========================================
# # Step 5: Compare Prediction with Actual Answer
# # ==========================================

# print(predictions)
# print(y_test)

# # predictions = What the model predicted
# # y_test     = The actual/correct answers
# #
# # We compare both to see how well the model performed.
# #
# # Example:
# #
# # predictions = [30, 80]
# # y_test      = [30, 80]
# #
# # Prediction = Actual Answer ✅
# #
# # This means the model predicted correctly.


# # ==========================================
# # Remember
# # ==========================================

# # fit()     → Model learns from training data
# #
# # predict() → Model predicts answers for new data
# #
# # X_train + y_train → Used for learning
# #
# # X_test → Used for making predictions
# #
# # y_test → Used to check the predictions


# x = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
# y = [10,20,30,40,50,60,70,80,90,100]
# # # X = model ko diya gaya input
# # # y = us input ka correct answer

# x_train,x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)


# model=LinearRegression()
# model.fit(x_train,y_train)
# predictions=model.predict(x_test)

# print(predictions)
# print(y_test)

# print(mean_squared_error(y_test, predictions))
# print(r2_score(y_test, predictions))



# noisy data

input_data= [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
op_data = [12, 18, 33, 37, 52, 58, 75, 79, 88, 95]   # ~10x not exact , noise data

ind_train, ind_test, op_train, op_test=train_test_split(input_data, op_data, test_size=0.2)
# print(ind_train)
# print(ind_test)
# print(op_train)
# print(op_test)


# model=LinearRegression()
# model.fit(ind_train, op_train)
# model_prediction= model.predict(ind_test)
# actual_data=op_test
# print(f"actuall data = {actual_data}")
# print(f"model predictin data = {model_prediction}")


# print(f"diffrence between actual data and model prediction = {mean_squared_error(actual_data,model_prediction)}")
# print(f"model learning feedback = {r2_score(actual_data,model_prediction)}")



# small problem for house rent prediction
size = [[500],[750],[1000],[1250],[1500],[1750],[2000],[2250],[2500],[2750]]
price = [25,35,48,55,68,80,90,105,115,130]  #in lakhs, bit noise

size_train, size_test, price_train, price_test=train_test_split(size, price,test_size=0.2)

# print(size_train,"\n",price)
model=LinearRegression()
model.fit(size_train,price_train)
prediction=model.predict(size_test)
print(prediction)
real_ans=price_test
print(real_ans)

print(mean_squared_error(real_ans, prediction))
print(r2_score(real_ans, prediction))

# Overfitting

# What: The model performs very well on training data, but poorly on test/new data. It memorized the training examples (including noise/randomness) instead of learning the actual general pattern.

# How to spot it: Training accuracy is very high (like 99%), but test accuracy is much lower (like 60%) — a big gap between the two.

# Example: Imagine your house-price model learned "size 1000 = exactly 48 lakhs" by memorizing that exact training row, instead of learning "roughly size × constant." It nails every training example but fails on new sizes it hasn't seen.

# Underfitting

# What: The model performs poorly on BOTH training and test data. It's too simple to even capture the pattern in the training data itself.

# How to spot it: Training accuracy itself is low (like 40%) — it never learned properly even on data it saw.

# Example: Trying to fit a straight line to data that's actually curved — the line will be wrong everywhere, training and test both.

# Quick comparison

# ┌──────────────┬───────────────────┬──────────────────────────┐
# │              │ Training accuracy │      Test accuracy       │
# ├──────────────┼───────────────────┼──────────────────────────┤
# │ Overfitting  │ High              │ Low                      │
# ├──────────────┼───────────────────┼──────────────────────────┤
# │ Underfitting │ Low               │ Low                      │
# ├──────────────┼───────────────────┼──────────────────────────┤
# │ Good fit     │ High              │ High (close to training) │
# └──────────────┴───────────────────┴──────────────────────────┘


# ===========================
# Feature Scaling
# ===========================

# What: Transforming numeric columns so they're on a similar range/scale
# (e.g. StandardScaler makes mean=0, std=1).

# Why: When features have very different ranges (e.g. size in thousands vs
# rooms 1-5), some algorithms end up biased toward the larger-magnitude
# feature, or take longer to train. Scaling puts every feature on equal footing.

# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# Needed for: Linear/Logistic Regression, KNN, SVM
# Not needed for: Decision Trees / Random Forest (they split on thresholds,
# not affected by magnitude)
