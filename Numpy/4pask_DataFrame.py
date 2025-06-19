import pandas as pd

zv = 30

def duomenys ():
    stulpelis1 = "Laikas"
    stulpelis2 = "Temperatūra"
    laikai = ["8:00", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30" ]
    # temperaturoOLD = [15, 17, 16, 18, 18, 19, 21, 20]
    temperaturos = [15, 17, -2, 18, -1, 19, 21, 20]
    duomenys = { stulpelis1 :  laikai, stulpelis2 : temperaturos}
    return pd.DataFrame(duomenys)

df = duomenys ()

# •Sukurkite DataFrame su bent 5 eilutėmis ir 3 stulpeliais, kur vienas iš stulpelių būtų temperatūra
def lentele_ir_dregme ( df ):
    df["Drėgmė"] = [60, 55, 70, 65, 68, 63, 61, 66]
    print ( df )
    return df


# •Atspausdinkite antrą ir ketvirtą eilutę iš DataFrame
def issitraukiam_is_df (nr1, nr2):
    print ( df.iloc[nr1], df.iloc[nr2] )

# •Atspausdinkitevisas eilutes,kuriosetemperatūra yra neigiama
def neigiamos_temp ( df ):
    print ( df[df["Temperatūra"] < 0] )

# •Apskaičiuokite ir atspausdinkite bendrą temperatūrų sumą
def temp_suma ( df ):
    print ( "Temperatūrų suma:", df["Temperatūra"].sum() )

# •Pridėkite naują stulpelį "Vėjas" su atsitiktinėmis reikšmėmis
def pridedam_veja ( df ):
    df["Vėjas"] = [8, 12, 6, 18, 13, 15, 25, 28]
    print ( df )
    return df

# •Pridėkite stulpelį "Peršalimo Rizika" su reikšme "Taip" visoms eilutėms, kuriose temperatūra mažesnė nei 0.
def rizika_persalt ( df ):
    df["Peršalimo Rizika"] = df["Temperatūra"].apply(lambda x: "Taip" if x < 0 else "Ne")
    print ( df )
    return df

# •Pakeiskite "Vėjas" stulpelio reikšmes į didžiosiomis raidėmis parašytą "Silpnas", "Vidutinis" arba "Stiprus", priklausomai nuo reikšmės (mažiau nei 10, nuo 10 iki 20, daugiau nei 20) (hintuseapply).
# def klasifikuok ( x ):
#     if x < 10:
#         return "Silpnas"
#     elif 10 <= x <= 20:
#         return "Vidutinis"
#     else:
#         return "Stiprus"


# •Sugrupuokiteduomenispagal"PeršalimoRizika" ir apskaičiuokitevidutinętemperatūrąkiekvienaigrupei

# •SurikiuokiteDataFramepagal "Temperatūra" stulpelį mažėjančia tvarka

# •Sujunkite du DataFrameobjektus (vieną su datomis ir temperatūromis, kitą su datomis ir vėjo stiprumu) pagal bendrą raktą ("Data") (gali būti indeksas, tuomet naudokite, joinmetodą, joinyra, kaip merge tik su indeksu).



# 1 užduotis
print ( "\n", "*" * zv, "1 užduotis", "*" * zv )
lentele_ir_dregme(df)
# 2 užduotis
print ( "\n", "*" * zv, "2 užduotis", "*" * zv )
issitraukiam_is_df (1, 3)
# 3 užduotis
print ( "\n", "*" * zv, "3 užduotis", "*" * zv )
neigiamos_temp (df)

# 4 užduotis
print ( "\n", "*" * zv, "4 užduotis", "*" * zv )
temp_suma (df)

# 5 užduotis
print ( "\n", "*" * zv, "5 užduotis", "*" * zv )
df = pridedam_veja(df)

# 6 užduotis
print ( "\n", "*" * zv, "6 užduotis", "*" * zv )
df = rizika_persalt(df)

# 7 užduotis
# print ( "\n", "*" * zv, "6 užduotis", "*" * zv )
# df = klasifikuok(df)
# df["Vėjas"] = df["Vėjas"].apply(klasifikuok)
# print ( df )

