import pandas as pd
import seaborn as gr
import matplotlib.pyplot as plot

x = [1, 2, 3, 4, 5, 6]
y = [2, 3, 5, 4, 6, 2]

def drop_objects ( df ):
    for column in df.columns:
        if df[column].dtype == "object":
            df = df.drop(column, axis=1)
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


# gr.pairplot(df, hue="survived", vars=["age", "fare", "class"], kind="scatter")




# gr.barplot ( x = df["passanger_id"], y = df["age"], color = "green" )
# plot.title ("grafikas1")
# plot.xlabel("passenger_id")
# plot.ylabel("age")
# plot.show()



# padropint šituos:


# pasidaryti funkciją, kuri dropins visus kurie yra object tipo!

    