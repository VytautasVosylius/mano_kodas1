import time
import numpy as np
import math

# dienos = 30
# centai = 1 * 2 ** dienos
# print("Centų skaičius po 30 dienų:", centai)  # Išvedamas centų skaičius po 30 dienų




#  # Skaičius pakeltas laipsniu
# # Sukuriamas dvimatis masyvas
# masyvas1 = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 3, 3]])
# masyvas2 = np.array([6, 7, 8, 9, 10])


# print("Masyvas 1:", masyvas1)


# # zeros_arr = np.zeros((3, 4))  # Sukuriamas 3x4 masyvas su nulinėmis reikšmėmis
# # print("Nulinis masyvas:\n", zeros_arr)

# # zeros_arr = np.zeros((5))  # Sukuriamas 3x4 masyvas su nulinėmis reikšmėmis
# # print("Nulinis masyvas:\n", zeros_arr)

# # zeros_arr = np.zeros((3, 3, 3, 3))  # Sukuriamas 3x4 masyvas su nulinėmis reikšmėmis
# # print("Nulinis masyvas:\n", zeros_arr)

# # for i in masyvas1:
# #     for j in i:
# #         print(j)

# for i in masyvas1:
#     print(i[1])

# print( "-" * 50)


# transposed_arr = masyvas1.T  # Transponuojamas masyvas
# # transposed_arr = masyvas1.transpose  # Transponuojamas masyvas
# print("Pasuktas masyvas:\n", transposed_arr)


# masyvas3 = np.arange(1, 10, 2)  # Sukuriamas masyvas su reikšmėmis nuo 1 iki 10 su žingsniu 2
# print("Masyvas su žingsniu 2:", masyvas3)

# masyvas4  = np.random.randint(1, 10, size=(3, 3))  # Skaičų reikšmės nuo 1 iki 10,  kuriamas atsitiktinių sveikųjų skaičių masyvas

# start = time.time()


# didelis_masyva1 = np.random.randint(1, 1000000, size=(1000, 1000))  # Sukuriamas didelis atsitiktinių sveikųjų skaičių masyvas
# print ("Didelis masyvas:\n", didelis_masyva1)


# eiliskumas = np.arange(1, 1080)  # Sukuriamas eilės tvarka didelis masyvas
# max = np.max(eiliskumas)  # Maksimali reikšmė 

# vienetine = np.eye(4)
# print("Vienetinis masyvas:\n", vienetine)

# vienetine [0,1] = 5  # Pakeičiama reikšmė vienetiniame masyve
# print("Pakeistas vienetinis masyvas:\n", vienetine)
# vienetine [2,0] = 10  # Pakeičiama reikšmė vienetiniame masyve
# print("Pakeistas vienetinis masyvas:\n", vienetine)

# test_masyvas = ()
# print (masyvas1.dtype)  # Išvedama masyvo tipas


# for i in range(len(vienetine)):
#     vienetine [0,i] = 5  # Pakeičiama reikšmos visos reikšmės pirmoje eilutėje
#     vienetine [i,0] = 5  # Pakeičiama reikšmos visos reikšmės pirmoje stulpelyje
#     vienetine [i,i] = 5  # Pakeičiama reikšmos visos reikšmės įstrižainėje!
# print("Pakeistas vienetinis masyvas:\n", vienetine)

# gabalas = vienetine[0: 2, 0:3]  # Išgaunamas gabalas iš „vienetinės“ matricos
# print("Išgautas gabalas iš vienetinio masyvo:\n", gabalas)

# Studentai = np.array(["Tomas", "Petras", "Ona", "Jonas", "Marytė", "Antanas", "Raimondas"])
# lankomumas = np.array([1, 0, 1, 1, 0, 1, 0])

# for i in range(len(Studentai)):
#     if lankomumas[i] == 1:
#         print(f"{Studentai[i]} yra atvykęs")
#     else:
#         print(f"{Studentai[i]} neatvyko")

# array = np.array([1, 2, 3, 4, 5])

# np.sin(array)
# np.cos(array)
# np.tan(array)
# np.log(array)
# pi= np.pi

# skaiciu = 2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2
# print( skaiciu )
# print(len(str(skaiciu)))

# print(f"{pi:.50f}")


eilute = np.array([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3])
nuokrypis = eilute.std()
print("Eilutės nuokrypis:", nuokrypis)

