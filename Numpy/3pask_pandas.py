import pandas as pd

zv = 30

indeksai = [1, 2, 3, 4, 5, 6]

# duomenys = [1, 10, 5, "Apelsinas", "Obuolys", 3.14]
duomenys = [1, 10, 5, 15, 50, 3]
# duomenys = ["Bananas", "Melionas", "Ananasas", "Apelsinas", "Obuolys", "Kriaušė"]
# duomenys = [0.157, 0.10, .005, 3.14, 1.81, .1]

stulpelis = pd.Series(duomenys)
print (stulpelis)

# su_indeksais = pd.Series( duomenys, indeksai )
# print (su_indeksais)


# 1 užduotis Atspausdinti serijos dydį ir tipą
print ( "\n", "*" * zv, "1 užduotis", "*" * zv )
print ( "Stulpelio elementų skaičius: ", stulpelis.size, "suomenų tipas: ", stulpelis.dtype )

# 2 užduotis Atspasudinti penktą elementą
print ( "\n", "*" * zv, "2 užduotis", "*" * zv )
print ( "Penktas elementas: ", stulpelis.values[4] )
# print ( "Penktas elementas: ", stulpelis.iloc[4] )

# 3 užduotis Atspausdinti visus išskyrus pirmą ir paskutinį
print ( "\n", "*" * zv, "3 užduotis", "*" * zv )
# trumpesnis = stulpelis.head( stulpelis.size - 1 )
# apkirptas = trumpesnis.tail( trumpesnis.size - 1 )
# print ( apkirptas )
print ( stulpelis.iloc[1:-1] )

# 4 užduotis Atspausdinti skaičius didesnius negu X
print ( "\n", "*" * zv, "4 užduotis", "*" * zv )
print ( stulpelis.values [stulpelis > 20] )

# 5 užduotis Atspausdinti serijos sumą
print ( "\n", "*" * zv, "5 užduotis", "*" * zv )
print ( pd.Series.sum( stulpelis ))

# 6 užduotis
print ( "\n", "*" * zv, "6 užduotis", "*" * zv )
print ( "Vidurkis: ", pd.Series.mean( stulpelis ))

# 7 užduotis
print ( "\n", "*" * zv, "7 užduotis", "*" * zv )
print ( "Vidurkis: ", pd.Series.mean( stulpelis ))

# 8 užduotis


applyed = 

