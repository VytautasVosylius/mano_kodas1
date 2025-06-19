# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split, KFold, cross_val_score
# from sklearn.metrics import mean_squared_error, r2_score
# import matplotlib.pyplot as plt
# import seaborn as sns

# # 🔽 Duomenų nuskaitymas
# df = pd.read_csv(r"E:\ML_beginer\Company bancropcy data\data.csv")

# # 🔽 Tikrinam duomenis
# print(df.head())
# print(df.info())
# print(df.dtypes)

# # 🔽 Pašalinam ne-skaitinius stulpelius (nebent nori kitaip)
# for col in df.columns:
#     if df[col].dtype == "object":
#         df = df.drop(columns=[col])

# # 🔽 Užpildom NaN su vidurkiu
# df = df.fillna(df.mean(numeric_only=True))

# # 🔽 Target ir features
# target = 'Bankrupt?'
# X = df.drop(columns=[target])
# y = df[target]

# # 🔽 Duomenų padalijimas
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # 🔽 Modelio treniravimas
# model = LinearRegression()
# model.fit(X_train, y_train)

# # 🔽 Prognozės
# y_pred = model.predict(X_test)

# # 🔽 Apvalinam tik jei nori klasifikuoti: np.round(y_pred)
# print("\n--- Modelio metrikos ---")
# print("R²:", r2_score(y_test, y_pred))
# print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# # 🔽 Tikimybės (nuo 0 iki 1)
# print("\n--- Tikimybės (pirmi 10) ---")
# print(np.round(y_pred[:10], 3))

# # 🔽 K-fold įvertinimas
# kfold = KFold(n_splits=5, shuffle=True, random_state=42)
# cv_scores = cross_val_score(model, X, y, cv=kfold, scoring="r2")

# print("\n--- K-Fold R² rezultatai ---")
# print(cv_scores)
# print("Vidutinis R²:", np.mean(cv_scores))

# # 🔽 Grafinė analizė
# plt.figure(figsize=(6, 6))
# sns.scatterplot(x=y_test, y=y_pred)
# plt.xlabel("Tikros reikšmės")
# plt.ylabel("Prognozuotos tikimybės")
# plt.title("Tikros vs. Prognozuotos tikimybės")
# plt.grid(True)
# plt.show()



import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# 🔽 Nuskaitymas
df = pd.read_csv(r"E:\ML_beginer\Company bancropcy data\data.csv")

# 🔽 Valymas
for col in df.columns:
    if df[col].dtype == "object":
        df = df.drop(columns=[col])
df = df.fillna(df.mean(numeric_only=True))

# 🔽 Target ir features
target = 'Bankrupt?'
X = df.drop(columns=[target])
y = df[target]

# 🔽 Padalijimas
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔽 Logistic Regression (tinka 0/1 atvejams)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 🔽 Prognozės (0/1)
y_pred = model.predict(X_test)

# 🔽 Tikimybės (nuo 0 iki 1)
y_prob = model.predict_proba(X_test)[:, 1]

# 🔽 Metrikos
print("\n--- Tikslumas (Accuracy) ---")
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\n--- Confusion Matrix ---")
print(confusion_matrix(y_test, y_pred))

print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred))

# 🔽 Tikimybių palyginimas su realiais duomenimis (scatter)
plt.figure(figsize=(6, 6))
sns.scatterplot(x=y_test, y=y_prob)
plt.xlabel("Tikra reikšmė")
plt.ylabel("Prognozuota tikimybė")
plt.title("Tikros vs. prognozuotos tikimybės")
plt.grid(True)
plt.show()
