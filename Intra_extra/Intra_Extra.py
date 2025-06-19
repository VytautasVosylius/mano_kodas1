
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression #, load_iris
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import root_mean_squared_error, r2_score, classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt


df = pd.read_csv("E:\\Intra_extra\\personality_dataset.csv")


print(df.head())

target = df["Personality"]
data = df.drop(columns="Personality")

encoder_label = LabelEncoder()

encoder_label.fit(target)

# Šita naudojme tik vieną kartą, nes kitaip iškraipoma forma
targets_encoded = encoder_label.transform(target)

# Pakeičia "Yes" ir "No" į 1 ir 0.
data = data.replace({'Yes': 1, 'No': 0})
data = data.fillna(data.mean(numeric_only=True))

X_test, X_train, Y_test, Y_train = train_test_split( data, target, train_size = 0.8, random_state = 13, stratify = target)

model = KNeighborsClassifier(n_neighbors=6)

print(data.dtypes)

# print(data.isnull().sum())


model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

# print(targets_encoded)

# print(encoder_label.inverse_transform(targets_encoded))

print ( "Tikslumas: ", accuracy_score(Y_test, Y_pred))
print ( "\nKlasifikacijos ataskaita:\n", classification_report(Y_test, Y_pred, target_names=encoder_label.classes_))
print ( "\nKonfucujaus matrica:\n", confusion_matrix(Y_test, Y_pred))







# import numpy as np
# import pandas as pd
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.preprocessing import LabelEncoder
# from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
# import matplotlib.pyplot as plt

# # 1. Įkeliame duomenų rinkinį
# # df = pd.read_csv("E:\\Intra_extra\\personality_dataset.csv")

# # 2. Atskiriame duomenis (X) ir tikslus (y)
# # target = df["Personality"]
# # data = df.drop(columns="Personality")

# # 3. Užkoduojame asmenybių etiketes į skaičius
# # encoder_label = LabelEncoder()
# # targets_encoded = encoder_label.fit_transform(target)

# # 4. Padaliname į mokymo ir testavimo aibes
# # X_train, X_test, y_train, y_test = train_test_split(data, targets_encoded, test_size=0.2, random_state=42)

# # 5. Pasirenkame klasifikatorių (pvz., K Nearest Neighbors)
# model = KNeighborsClassifier(n_neighbors=5)

# # 6. Apmokome modelį
# model.fit(X_train, y_train)

# # 7. Atliekame prognozes
# y_pred = model.predict(X_test)

# # 8. Įvertiname rezultatus
# print("Tikslumas:", accuracy_score(y_test, y_pred))
# print("\nKlasifikacijos ataskaita:\n", classification_report(y_test, y_pred, target_names=encoder_label.classes_))
# print("\nSutrikimo matrica:\n", confusion_matrix(y_test, y_pred))