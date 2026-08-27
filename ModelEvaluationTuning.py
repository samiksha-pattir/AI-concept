import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
# Cross-Validation (K-Fold)
#                  DATA
#                    ↓
#              Split into 5
#                  folds
#                    ↓
#       ┌──────┬──────┬──────┬──────┬──────┐
#       │ Fold1│ Fold2│ Fold3│ Fold4│ Fold5│
#       └──────┴──────┴──────┴──────┴──────┘
#           ↓
#      Test each fold
#      one at a time
#           ↓
#       5 scores
#           ↓
#     Average score
#           ↓
#    More reliable result

x = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
y = [10,20,30,40,50,60,70,80,90,100]
model=LinearRegression()
scores=cross_val_score(model,x,y,cv=5)

# print(scores)
# print(scores.mean())
# cross_val_score() by default uses the model's .score() method. For LinearRegression, that score is R². So these are 5 R² scores, not accuracy percentages.



    #          Ridge Model
    #               ↓
    #       Hyperparameter
    #           alpha
    #               ↓
    #    ┌─────────────────────┐
    #    │ Values to try       │
    #    │                     │
    #    │ 0.1   1   10   100 │
    #    └──────────┬──────────┘
    #               ↓
    #       GridSearchCV
    #               ↓
    #    Try each value
    #               ↓
    #       5-Fold CV
    #               ↓
    #     Compare scores
    #               ↓
    #       Best setting
    #               ↓
    #    best_params_
    #               ↓
    #     Best CV score
    #               ↓
    #    best_score_


# model = Ridge()
# params = {"alpha": [0.1, 1, 10, 100]}   # 4 alag values try karni hai

# grid = GridSearchCV(model, params, cv=5)
# grid.fit(x, y)

# print(grid.best_params_)    # best value mili
# print(grid.best_score_)      # us value ka score


# sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor

models = {
    "Linear Regression": LinearRegression(),
    "Ridge": Ridge(alpha=0.1),
    "Decision Tree": DecisionTreeRegressor()
}

for name, model in models.items():
    scores = cross_val_score(model, x, y, cv=5)
    print(f"{name}: avg score = {scores.mean():.4f}")

# Result: Linear Regression ~1.0, Ridge ~0.9998, Decision Tree ~ -5.4
# The dataset is a tiny, perfectly linear line, so the simplest model
# (Linear Regression) wins. Decision Tree does badly here because with
# only 10 points split into 5 folds, each fold trains on very little
# data, and trees don't extrapolate a straight line beyond what they saw.
# Lesson: a more complex model is not automatically a better model -
# it depends on the data.


# ==========================================
# Day 11 - Interview Questions
# ==========================================

# 1. What does K-fold CV protect against (why is it better than one split)?
# A single train/test split can be lucky or unlucky - the random split
# might put easy or hard examples into the test set by chance, giving a
# misleading score. K-fold tests the model on K different slices of the
# data and averages the results, so the score reflects overall
# performance rather than one lucky/unlucky split.

# 2. Grid search vs random search - what's the difference?
# Grid search tries every combination of the given parameter values
# (exhaustive, slower, guaranteed to check everything you listed).
# Random search picks a random sample of combinations to try (faster,
# good when there are too many combinations to check them all, though
# it might miss the single best one).

# 3. Given this result (Decision Tree failing) - how do you decide which
#    model to use?
# Look at the data first: how much data is there, is the relationship
# simple (linear) or complex, and how did each model actually score
# with cross-validation - not just which model "sounds" more powerful.
# Here, the data was small and perfectly linear, so the simple model
# (Linear Regression) beat the more complex one (Decision Tree) by a
# huge margin. Model choice should follow the evidence (CV scores),
# not assumptions about which algorithm is fancier.

