import numpy as np

zv = 30

# 1 užduotis
print ( "\n", "*" * zv, "1 užduotis", "*" * zv )

eulute = [1, 2, 3, 4, 5]
masyvas = np.array(eulute)  # Sukuriamas masyvas iš sąrašo
print ( "Masyvas:", masyvas )

# 2 užduotis
print ( "\n", "*" * zv, "2 užduotis", "*" * zv )

nulinis_masyvas = np.zeros((3, 3))  # Sukuriamas 3x3 masyvas su nulinėmis reikšmėmis
print ( "Nulinis masyvas:\n", nulinis_masyvas )

# 3 užduotis
print ( "\n", "*" * zv, "3 užduotis", "*" * zv )

eilute2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("Eilutė 2:", eilute2)
masyvas2 = np.array(eilute2)  # Sukuriamas masyvas iš sąrašo
masyvas3 = masyvas2.reshape(3, 3)  # Perkuriamas masyvas į 3x3 formą
print ( "Masyvas 3x3:\n", masyvas3 )

# 3.1 užduotis
print ( "\n", "*" * zv, "3.1 užduotis", "*" * zv )

simbolis = masyvas3[0, 1]  # Pasiekiama reikšmė masyve
print ( "Reikšmė masyvo pirmos eilutės antro stulpelio (0, 1):", simbolis )

# 3.2 užduotis
print( "\n", "*" * zv, "3.2 užduotis", "*" * zv )

ispjova = masyvas3  [ 0:2, 1:3] # Išpjoviamas masyvas nuo 1 iki 2 eilutės ir nuo 2 iki 3 stulpelio, imtinai
print ( "Išpjautas masyvas:\n", ispjova )

# 4 užduotis
print ( "\n", "*" * zv, "4 užduotis", "*" * zv )

masyvas5 = np.array([1, 2, 3])
masyvas6 = np.array([4, 5, 6])

# 4.1 užduotis
print ( "\n", "*" * zv, "4.1 užduotis", "*" * zv )

suma = masyvas5 + masyvas6  # Atliekama sudėtis
print ( "Masyvų suma:", suma )

skirtimas = masyvas5 - masyvas6  # Atliekamas atimtis
print ( "Masyvų skirtumas:", skirtimas )

daugyba = masyvas5 * masyvas6  # Atliekama daugyba
print ( "Masyvų daugyba:", daugyba )

dalyba = masyvas5 / masyvas6  # Atliekama dalyba
print ( "Masyvų dalyba:", dalyba )

# 4.2 užduotis
print ( "\n", "*" * zv, "4.2 užduotis", "*" * zv )

demenu_suma1 = np.sum(masyvas5)  # Apskaičiuojama masyvo suma
demenu_suma2 = np.sum(masyvas6)  # Apskaičiuojama masyvo suma
print ( "Masyvo 5 suma:", demenu_suma1 )
print ( "Masyvo 6 suma:", demenu_suma2 )

vidurkis1 = np.mean(masyvas5)  # Apskaičiuojamas masyvo vidurkis
vidurkis2 = np.mean(masyvas6)  # Apskaičiuojamas masyvo vidurkis
print ( "Masyvo 5 vidurkis:", vidurkis1 )
print ( "Masyvo 6 vidurkis:", vidurkis2 )

maks1 = np.max(masyvas5)  # Apskaičiuojama masyvo maksimali reikšmė
maks2 = np.max(masyvas6)  # Apskaičiuojama masyvo maksimali reikšmė
print ( "Masyvo 5 maksimali reikšmė:", maks1 )
print ( "Masyvo 6 maksimali reikšmė:", maks2 )

min1 = np.min(masyvas5)  # Apskaičiuojama masyvo minimali reikšmė
min2 = np.min(masyvas6)  # Apskaičiuojama masyvo minimali reikšmė
print ( "Masyvo 5 minimali reikšmė:", min1 )
print ( "Masyvo 6 minimali reikšmė:", min2 )

# 5 užduotis
print ( "\n", "*" * zv, "5 užduotis", "*" * zv )

masyvas7 = np.array([0, np.pi/2, np.pi])  # Sukuriamas masyvas su kampais radianais
print ( "Masyvas su kampais radianais:", masyvas7 )

# 5.1 užduotis
print ( "\n", "*" * zv, "5.1 užduotis", "*" * zv )

sinusai = np.sin(masyvas7)  # Apskaičiuojami sinusai
kosinusai = np.cos(masyvas7)  # Apskaičiuojami kosinusai
tangentai = np.tan(masyvas7)  # Apskaičiuojami tangentai
print ( "Sinusai:", sinusai )
print ( "Kosinusai:", kosinusai )
print ( "Tangentai:", tangentai )

# 5.2 užduotis
print ( "\n", "*" * zv, "5.2 užduotis", "*" * zv )

eksponente = np.exp(masyvas7)  # Apskaičiuojamas eksponentas
# logaritmas = np.log(masyvas7)  # Apskaičiuojamas natūralusis logaritmas
print ( "Eksponentes:", eksponente )
# print("Logaritmai:", logaritmas)


# 6 užduotis
print ( "\n", "*" * zv, "6 užduotis", "*" * zv )

atsitiktines_masyvas = np.random.rand(3, 3)  # Sukuriamas 3x3 dydžio atsitiktinių skaičių masyvas
print("Atsitiktinių skaičių masyvas:\n", atsitiktines_masyvas)

# 6.1 užduotis
print ( "\n", "*" * zv, "6.1 užduotis", "*" * zv )

padidintas_masyvas = atsitiktines_masyvas * 2  # Padauginamas masyvas iš 2
print ( "Padidintas atsitiktinių skaičių masyvas:\n", padidintas_masyvas )

# 7 užduotis
# •Užduotis yra sukurti atsitiktinius orų duomenis naudojant numpyir apskaičiuoti įvairias metrikas:
np.random.seed(0)

# 7.1 užduotis
# •Sugeneruokite miesto orų temperatūras vieniems metams (pvz2024-01-01: -15, 2024-01-02: -17 ir t.t) Rekomenduojama generuoti kiekvieną mėnesį atskirai
print ( "*" * zv, "7.1 užduotis", "*" * zv )

sausio_orai = np.random.randint( -15, 10, size = (31) )  # Sukuriamas sausio mėnesio masyvas su oro temperatūromis
vasario_orai = np.random.randint( -17, 5, size = (28) )  # Sukuriamas vasario mėnesio masyvas su oro temperatūromis
kovo_orai = np.random.randint( -5, 15, size = (31) )  # Sukuriamas kovo mėnesio masyvas su oro temperatūromis
balandzio_orai = np.random.randint( 0, 20, size = (30) )  # Sukuriamas balandžio mėnesio masyvas su oro temperatūromis
gegužės_orai = np.random.randint( 5, 25, size = (31) )  # Sukuriamas gegužės mėnesio masyvas su oro temperatūromis
birželio_orai = np.random.randint( 15, 30, size = (30) )  # Sukuriamas birželio mėnesio masyvas su oro temperatūromis
liepos_orai = np.random.randint( 15, 35, size = (31) )  # Sukuriamas liepos mėnesio masyvas su oro temperatūromis
rugpjucio_orai = np.random.randint( 10, 30, size = (31) )  # Sukuriamas rugpjūčio mėnesio masyvas su oro temperatūromis
rugsėjo_orai = np.random.randint( 5, 25, size = (30) )  # Sukuriamas rugsėjo mėnesio masyvas su oro temperatūromis
spalio_orai = np.random.randint( 0, 20, size = (31) )  # Sukuriamas spalio mėnesio masyvas su oro temperatūromis 
lapkričio_orai = np.random.randint( -5, 15, size = (30) )  # Sukuriamas lapkričio mėnesio masyvas su oro temperatūromis
gruodžio_orai = np.random.randint( -10, 10, size = (31) )  # Sukuriamas gruodžio mėnesio masyvas su oro temperatūromis


# sausio_orų_masyvas = np.array(sausio_orai)
# vasario_orų_masyvas = np.array(vasario_orai)
# kovo_orų_masyvas = np.array(kovo_orai)
# balandzio_orų_masyvas = np.array(balandzio_orai)
# gegužės_orų_masyvas = np.array(gegužės_orai)
# birželio_orų_masyvas = np.array(birželio_orai)
# liepos_orų_masyvas = np.array(liepos_orai)
# rugpjucio_orų_masyvas = np.array(rugpjucio_orai)
# rugsėjo_orų_masyvas = np.array(rugsėjo_orai)
# spalio_orų_masyvas = np.array(spalio_orai)
# lapkričio_orų_masyvas = np.array(lapkričio_orai)
# gruodžio_orų_masyvas = np.array(gruodžio_orai)

# print ( "metų temperatūros: ", sausio_oru_masyvas, vasario_oru_masyvas, kovo_oru_masyvas, balandzio_oru_masyvas, gegužės_oru_masyvas, birželio_oru_masyvas, liepos_oru_masyvas, rugpjucio_oru_masyvas, rugsėjo_oru_masyvas, spalio_oru_masyvas, lapkričio_oru_masyvas, gruodžio_oru_masyvas )
#metų_temperatūros = np.concatenate((sausio_oru_masyvas, vasario_oru_masyvas, kovo_oru_masyvas, balandzio_oru_masyvas, gegužės_oru_masyvas, birželio_oru_masyvas, liepos_oru_masyvas, rugpjucio_oru_masyvas, rugsėjo_oru_masyvas, spalio_oru_masyvas, lapkričio_oru_masyvas, gruodžio_oru_masyvas))  # Sujungiami visi mėnesių masyvai į vieną
metų_temperatūros = np.concatenate (( sausio_orai,
    vasario_orai,
    kovo_orai,
    balandzio_orai,
    gegužės_orai,
    birželio_orai,
    liepos_orai,
    rugpjucio_orai,
    rugsėjo_orai,
    spalio_orai,
    lapkričio_orai,
    gruodžio_orai
))

# metų_temperatūros = np.array(sausio_orų_masyvas.tolist() + vasario_orų_masyvas.tolist() + kovo_orų_masyvas.tolist() + balandzio_orų_masyvas.tolist() + gegužės_orų_masyvas.tolist() + birželio_orų_masyvas.tolist() + liepos_orų_masyvas.tolist() + rugpjucio_orų_masyvas.tolist() + rugsėjo_orų_masyvas.tolist() + spalio_orų_masyvas.tolist() + lapkričio_orų_masyvas.tolist() + gruodžio_orų_masyvas.tolist())
# print ( "Metų temperatūros masyvas:\n", metų_temperatūros )

# 7.2 užduotis
# •Įterpkite anomalijų pvzsausį temperatūra pasiekia +10 laipsnių arba staiga pakinta nuo -15 iki -35)
print ( "\n", "*" * zv, "7.2 užduotis", "*" * zv )

anomalija1 = -30
anomalija2 = 3
anomalija3 = 1.7345
anomalija4 = 0.0001
anomalija5 = 1000
#anomalija6 = "A"
gudrianomalija = 10

atsitiktinis = np.random.randint(0, 365, size=(8))  # Sukuriamas atsitiktinių skaičių masyvas

metų_temperatūros[atsitiktinis[0]] = anomalija1  # Pakeičiama atsitiktinė reikšmė su anomalija1
metų_temperatūros[atsitiktinis[1]] = anomalija2  # Pakeičiama atsitiktinė reikšmė su anomalija2
metų_temperatūros[atsitiktinis[2]] = anomalija3  # Pakeičiama atsitiktinė reikšmė su anomalija3
metų_temperatūros[atsitiktinis[3]] = anomalija4  # Pakeičiama atsitiktinė reikšmė su anomalija4
metų_temperatūros[atsitiktinis[4]] = anomalija5  # Pakeičiama atsitiktinė reikšmė su anomalija5
# metų_temperatūros[atsitiktinis[5]] = anomalija6  # Pakeičiama atsitiktinė reikšmė su anomalija6
metų_temperatūros[atsitiktinis[6]] = metų_temperatūros[atsitiktinis[6]] + gudrianomalija  # Pakeičiama atsitiktinė reikšmė su gudrianomalija (initially 10 laipsnių)
metų_temperatūros[atsitiktinis[7]] = metų_temperatūros[atsitiktinis[7]] - gudrianomalija  # Pakeičiama atsitiktinė reikšmė su gudrianomalija (initially -10 laipsnių)

print ( "Metų temperatūros masyvas su anomalijomis:\n", metų_temperatūros )

# 7.3 užduotis
# •Suskaičiuokite mėnesio vidutines temperatūras
print ( "\n", "*" * zv, "7.3 užduotis", "*" * zv )

sausio_orų_masyvas = metų_temperatūros[0:31]  # Ištraukiamas sausio mėnesio masyvas
vasario_orų_masyvas = metų_temperatūros[31:59]  # Ištraukiamas vasario mėnesio masyvas
kovo_orų_masyvas = metų_temperatūros[59:90]  # Ištraukiamas kovo mėnesio masyvas
balandzio_orų_masyvas = metų_temperatūros[90:120]  # Ištraukiamas balandžio mėnesio masyvas
gegužės_orų_masyvas = metų_temperatūros[120:151]  # Ištraukiamas gegužės mėnesio masyvas
birželio_orų_masyvas = metų_temperatūros[151:181]  # Ištraukiamas birželio mėnesio masyvas
liepos_orų_masyvas = metų_temperatūros[181:212]  # Ištraukiamas liepos mėnesio masyvas
rugpjucio_orų_masyvas = metų_temperatūros[212:243]  # Ištraukiamas rugpjūčio mėnesio masyvas
rugsėjo_orų_masyvas = metų_temperatūros[243:273]  # Ištraukiamas rugsėjo mėnesio masyvas
spalio_orų_masyvas = metų_temperatūros[273:304]  # Ištraukiamas spalio mėnesio masyvas
lapkričio_orų_masyvas = metų_temperatūros[304:334]  # Ištraukiamas lapkričio mėnesio masyvas
gruodžio_orų_masyvas = metų_temperatūros[334:365]  # Ištraukiamas gruodžio mėnesio masyvas

vidutines_temperaturos = np.array([
    np.mean(sausio_orų_masyvas),
    np.mean(vasario_orų_masyvas),
    np.mean(kovo_orų_masyvas),
    np.mean(balandzio_orų_masyvas),
    np.mean(gegužės_orų_masyvas),
    np.mean(birželio_orų_masyvas),
    np.mean(liepos_orų_masyvas),
    np.mean(rugpjucio_orų_masyvas),
    np.mean(rugsėjo_orų_masyvas),
    np.mean(spalio_orų_masyvas),
    np.mean(lapkričio_orų_masyvas),
    np.mean(gruodžio_orų_masyvas)
])  # Apskaičiuojamos vidutinės temperatūros kiekvienam mėnesiui
print ( "Vidutinės temperatūros kiekvienam mėnesiui:\n", vidutines_temperaturos )

# 7.4 užduotis
# •Naudodami NumPy suraskite šias anomalijas, galite naudoti įvairias technikas (rekomendacija naudoti standartinį nuokrypį)
print ( "\n", "*" * zv, "7.4 užduotis", "*" * zv )

vidurkiai = np.array([
    np.mean(sausio_orų_masyvas),
    np.mean(vasario_orų_masyvas),
    np.mean(kovo_orų_masyvas),
    np.mean(balandzio_orų_masyvas),
    np.mean(gegužės_orų_masyvas),
    np.mean(birželio_orų_masyvas),
    np.mean(liepos_orų_masyvas),
    np.mean(rugpjucio_orų_masyvas),
    np.mean(rugsėjo_orų_masyvas),
    np.mean(spalio_orų_masyvas),
    np.mean(lapkričio_orų_masyvas),
    np.mean(gruodžio_orų_masyvas)    
])
print ( "Vidurkiai kiekvienam mėnesiui:\n", vidurkiai )

medianos = np.array([
    np.median(sausio_orų_masyvas),
    np.median(vasario_orų_masyvas),
    np.median(kovo_orų_masyvas),
    np.median(balandzio_orų_masyvas),
    np.median(gegužės_orų_masyvas),
    np.median(birželio_orų_masyvas),
    np.median(liepos_orų_masyvas),
    np.median(rugpjucio_orų_masyvas),
    np.median(rugsėjo_orų_masyvas),
    np.median(spalio_orų_masyvas),
    np.median(lapkričio_orų_masyvas),
    np.median(gruodžio_orų_masyvas)
])
print ( "Medianos kiekvienam mėnesiui:\n", medianos )

standartiniai_nuokrypiai = np.array([
    np.std(sausio_orų_masyvas),
    np.std(vasario_orų_masyvas),
    np.std(kovo_orų_masyvas),
    np.std(balandzio_orų_masyvas),
    np.std(gegužės_orų_masyvas),
    np.std(birželio_orų_masyvas),
    np.std(liepos_orų_masyvas),
    np.std(rugpjucio_orų_masyvas),
    np.std(rugsėjo_orų_masyvas),
    np.std(spalio_orų_masyvas),
    np.std(lapkričio_orų_masyvas),
    np.std(gruodžio_orų_masyvas)
])
print ( "Standartiniai nuokrypiai kiekvienam mėnesiui:\n", standartiniai_nuokrypiai )

# Neveikia taip:
# rasta_anomalija1 = metų_temperatūros < -25  # Rasta anomalija, kai temperatūra mažesnė nei -25
# rasta_anomalija2 = metų_temperatūros > 35  # Rasta anomalija, kai temperatūra didesnė nei 35
# print ( "Rasta anomalija 1 (temperatūra < -25):", rasta_anomalija1 )
# print ( "Rasta anomalija 2 (temperatūra > 35):", rasta_anomalija2 )

# print ( "*" * zv, "Anomalijų temperatūros reikšmės", "*" * zv )


# print ( "Anomalijos temperatūros reikšmės: " )
# for temp in metų_temperatūros:
#     if temp > 30 or temp < -20:
#         print ( "\033[0;30;41m", temp, "\033[0m", end = " " )
#     else:
#         print(temp, end = " ")

print( "\n", "*" * zv, " Temperatūrų anomalijos (raudonam fone) ir temperatūrų šuoliai (geltoni)", "*" * zv )
print ( "Dideli temperatūrų šuoliai: " )

viršutinė_riba = 32
apatinė_riba = -16
anomalijų_indeksai = np.array([])
for i in range(len(metų_temperatūros)):
    anomalijų_indeksai = np.arange(0, len(metų_temperatūros))
    temp_šiandien = metų_temperatūros[i]
    temp_vakar = metų_temperatūros[i-1] #kai 1 = 0 pasiims paskutinę reikšmę, tai yra kąunam pilną ciklą, kas šiuo atveju gal ne visai logiška :D 
    temp_skirtumas = temp_vakar - temp_šiandien
    if temp_šiandien > viršutinė_riba or temp_šiandien < apatinė_riba:
        print ( "\033[0;31;41m", temp_šiandien, "\033[0m", end = " " )
    elif  temp_skirtumas > 15 or temp_skirtumas < -15:
        print ( "\033[0;33m", temp_šiandien, "\033[0m", end = " " )
    else:
        print ( temp_šiandien, end = " " )
print ( "\n", "*" * zv, "Anomalijų indeksai", "*" * zv )



# anomalijų_indeksai = np.where( metų_temperatūros > 30 )[0]
# print("Anomalijų indeksai:", anomalijų_indeksai)

visos_anomalijos = np.array([]) 
for i in anomalijų_indeksai:
    np.append(visos_anomalijos, metų_temperatūros [i]) 

print ("Visos anomalijos: ", visos_anomalijos)


# Advanced(neturintiems ką veikti)
# •Pamėginkite atvaizduoti visų metų temperatūra naudodami matplotlib, anomalijas paryškinkite kita spalva.

"""
•Užduotis yra sukurti atsitiktinius orų duomenis naudojant numpyir apskaičiuoti įvairias metrikas:
•Sugeneruokite miesto orų temperatūras vieniems metams (pvz2024-01-01: -15, 2024-01-02: -17 ir t.t) Rekomenduojama generuoti kiekvieną mėnesį atskirai
•Įterpkite anomalijų pvzsausį temperatūra pasiekia +10 laipsnių arba staiga pakinta nuo -15 iki -35)
•Suskaičiuokite mėnesio vidutines temperatūras
•Naudodami NumPy suraskite šias anomalijas, galite naudoti įvairias technikas (rekomendacija naudoti standartinį nuokrypį)
•
•Advanced(neturintiems ką veikti)
•Pamėginkite atvaizduoti visų metų temperatūra naudodami matplotlib, anomalijas paryškinkite kita spalva.
 
Sukurkite NumPymasyvą, kuriame saugomi komandos žaidėjų rezultatai (pvz., surinktų taškų kiekis kiekviename rungtynių etape).
•
•Naudokite operacijas, kad suskaičiuotumėte bendrą komandos rezultatą, vidurkį bei surastumėte geriausią žaidėją.
•
•Galite išplėsti užduotį – vizualizuokite rezultatus su „matplotlib“.
•
•Patarimai:
•
•Naudokite np.array() duomenų struktūros sukūrimui.
•
•Apskaičiuokite vidurkį su np.mean(), sumą su np.sum(), o geriausią rezultatą su np.max() arba np.argmax().
 
Naudodami np.arange(), sukurkite masyvą, kuriame būtų skaičiai nuo 0 iki 9.
 
Iš šio masyvo išrinkite pirmuosius 5 skaičius ir paskutinius 3 skaičius naudodami slicing.
 
Patarimai:
 
np.arange(10) sukurs masyvą nuo 0 iki 9.
 
Slicingsintaksė: array[:5] pirmiesiems 5 elementams, array[-3:] paskutiniams 3.
 
Sukurkite vienmačio masyvą, kuriame saugomos skirtingų prekių kainos (pvz., [3.50, 7.99, 2.99, 12.50, 5.00]).
 
Apskaičiuokite bendrą kainų sumą ir vidutinę prekių kainą.
 
Papildomai, apskaičiuokite, kiek kiekvienos prekės kaina padidės, jei prie jos pridėsime 10% mokesčio.
 
Patarimai:
 
Bendram sumos apskaičiavimui – np.sum().
 
Vidurkiui – np.mean().
 
Elementų padidinimui: naudokite aritmetines operacijas (pvz., prices* 1.10).
 
"""















