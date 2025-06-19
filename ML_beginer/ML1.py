from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
# X, y = iris.data, iris.target

import matplotlib.pyplot as plt
import seaborn as sns
 
# df = sns.load_dataset("titanic")
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
 
# labai svarbu susipažinti su duomenimis
print(df.head())
print(df.describe())
print(df.info())
 
# df1 = sns.load_dataset("titanic") 



# print(sns.load_dataset("titanic"))
 
sns.pairplot(df, hue='target') #, markers=["o", "s", "D"])
plt.show()
 
# DUomenys sutvarkyti # ir paruošti mokymui
from sklearn.model_selection import train_test_split
 
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_test, y_train, y_test  = train_test_split(df, df['target'], test_size=0.20, random_state=42, stratify=df['target'])
# strify=df['target'] - tai svarbu, kad duomenys būtų subalansuoti
print(X_train.shape)
print(X_test.shape)
 
from sklearn.linear_model import LogisticRegression
 
model = LogisticRegression()
model.fit(X_train, y_train) # Treniravimas (training)
# Model evaluation
from sklearn.metrics import accuracy_score, confusion_matrix
y_pred = model.predict(X_test) # Predicting(Inference) Spejimas
 
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

"""
Sutvarkykite duomenis, kad tiktų logistinei regresijai. Svarbu nepalikti pasikartojančio target stulpekio,
pvz yra IsAlive (kurio reikšmės yra identiškos Survived, šitą privaloma išmesti).
Atlikite ant jo treniravimą ir pamėginkite gauti kuo aukštesnius accuracy rezultatus su testavimo duomenimis.
Nepamirškite visų žingsnių, tokių, kaip duomenų sutvarkymas, logistinė regresija negali dirbti su tekstiniais duomenimis,
dėl to reikės arba išmesti arba paversti į skaičius (pvz Male/Female -> 0/1. 
Nerekomenduojama versti į skaičius, jeigu yra daugiau nei dvi reikšmės pvz uostas S/Q/C neturėtų virsti į 0/1/2,
šiandienai juos geriau tiesiog išmesti, o kitą dieną išmoksite, kaip susitvarkyti).

"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_regression, load_iris
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import root_mean_squared_error, r2_score, classification_report
import matplotlib.pyplot as plt


df = pd.read_csv("personality_dataset.csv")


print(df.head())

target = df["Personality"]
data = df.drop(columns="Personality")

encoder_label = LabelEncoder()

encoder_label.fit(target)

targets_encoded = encoder_label.transform(target)

print(targets_encoded)

print(encoder_label.inverse_transform(targets_encoded))














# data = load_iris()


# x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)

# # print(x_train)
# # print(y_train)

# # print(x_test)
# # print(y_test)






# model_clasification_k = KNeighborsClassifier(n_neighbors=3)

# model_clasification_k.fit(x_train, y_train)

# y_pred = model_clasification_k.predict(x_test)

# report = classification_report(y_test, y_pred)

# print(report)








# x_reg, y_reg = make_regression(n_samples=100, n_features=2, noise=30, random_state=42)

# linear_model = LinearRegression()
# kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# linear_score = cross_val_score(linear_model, x_reg, y_reg, cv=kfold, scoring="r2")

# print(linear_score)
# print(np.average(linear_score))



# x_train, x_test, y_train, y_test = train_test_split(x_reg, y_reg, test_size=0.3, random_state=42)
# model = LinearRegression()


# model.fit(x_train,y_train)

# Y_pred = model.predict(x_test)

# rmse = root_mean_squared_error(y_test, Y_pred)
# r2 = r2_score(y_test, Y_pred)

# print(rmse) # 0 perfect more means more error
# print(r2) # 0-1 - 1 means perfrect





# plt.scatter(y_test, Y_pred)
# plt.xlabel("Tiesa")
# plt.ylabel("Spėjimas")
# plt.show()

