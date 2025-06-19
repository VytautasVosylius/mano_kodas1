
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression, load_iris
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import root_mean_squared_error, r2_score, classification_report
import matplotlib.pyplot as plt


df = pd.read_csv("E:\\Video_games\\vgsales.csv")


print(df.head())

target = df["Personality"]
data = df.drop(columns="Personality")

encoder_label = LabelEncoder()

encoder_label.fit(target)

targets_encoded = encoder_label.transform(target)



print(targets_encoded)

print(encoder_label.inverse_transform(targets_encoded))
