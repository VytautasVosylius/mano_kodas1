import pandas as pd
import seaborn as gr
import matplotlib.pyplot as plot

# from sklearn.datasets import load_iris
# iris = load_iris()

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# X, y = iris.data, iris.target

# x = [1, 2, 3, 4, 5, 6]
# y = [2, 3, 5, 4, 6, 2]

def drop_objects ( df ):
    for column in df.columns:
        if df[column].dtype == "object":
            df = df.drop (column, axis=1)
    return df

def fill_average (df, column_name):
    if column_name in df.columns:
        average = df[column_name].mean()
        df[column_name] = df[column_name].fillna(average)
    return df


# gr.set_theme ( style = "darkgrid" )

# df = pd.read_csv( "E:\\Titanic\\test.csv")
# pasitobulinu programą, įsikeliant duomenis iš duomenų rinkinio
df = gr.load_dataset("titanic")

df = df.reset_index().rename(columns={"index": "passanger_id"}) # pridedam stulpelį si indeksais, kad būtų patogiau operuoti

#Info pradžioje
# print( "Tipai pradžioje: ",df.dtypes )
# print ( "Info pradžioje: " )
# df.info()
# print ( " INFO END " )

# Išvalom duomenis (Išmetame visus objektus)

df = drop_objects ( df ) 
df = df.drop ( columns = ["deck"] ) # išmetam šitą, nes jis yra nereikalingas

df = fill_average ( df, "age" ) # užpildom amžių su vidurkiu

print ( df.dtypes )
print ( df["age"].mean() )

print ( "Info " )
df.info()
# print ( "df", df)
# print (df["PassengerId"])


 
# df = sns.load_dataset("titanic")
# df = pd.DataFrame(iris.data, columns=iris.feature_names)
# df['target'] = iris.target
 
# labai svarbu susipažinti su duomenimis
print(df.head())
print(df.describe())
print(df.info())
 
# df1 = sns.load_dataset("titanic") 



# print(sns.load_dataset("titanic"))
 
gr.pairplot(df, hue='survived') #, markers=["o", "s", "D"])
plot.show()
 
# DUomenys sutvarkyti # ir paruošti mokymui
 
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_test, y_train, y_test  = train_test_split( df, df['survived'], test_size=0.20, random_state=42, stratify=df['survived'] )
# strify=df['target'] - tai svarbu, kad duomenys būtų subalansuoti
print(X_train.shape)
print(X_test.shape)
 
 
model = LogisticRegression()
model.fit(X_train, y_train) # Treniravimas (training)
# Model evaluation
y_pred = model.predict(X_test) # Predicting(Inference) Spejimas
 
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)


# padropint šituos:


# pasidaryti funkciją, kuri dropins visus kurie yra object tipo!

    