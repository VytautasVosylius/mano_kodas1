import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
import matplotlib.pyplot as plot
# import os
# print(os.path.exists(r"E:\ML_beginer\Company bancropcy data\data.csv"))

df = pd.read_csv( "E:\\ML_beginer\\Company bancropcy data\\data.csv")
print (df)
print (df.info())
print ( df.dtypes )
print (df.columns)


# x_reg, y_reg = make_regression ( n_samples=100, n_features=2, noise=30, random_state=42 )

# linear_model = LinearRegression()
# kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# linear_score = cross_val_score(linear_model, x_reg, y_reg, cv=kfold, scoring="r2")

# print(linear_score)
# print(np.average(linear_score))