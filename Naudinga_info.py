"""

 <
 >
 ≤
 ≥
 
Spalvų kodai
\033[<style>;<text color>;<background>m

Pagrindinės spalvos:
Spalva	Teksto kodas	Fonas kodas
Juoda	30	40
Raudona	31	41
Žalia	32	42
Geltona	33	43
Mėlyna	34	44
Violetinė	35	45
Žydra	36	46
Balta	37	47

Stilius	Kodas
Normalus	0
Pariebintas	1
Pabrauktas	4
Inversija	7
 
Grąžinti į normalų:
"\033[0m"

Kad spausdinant nemestų į kitą eilutę:
end = " "


"""

# Logistinė regresija yra skirta KLASIFIKACIJOS uždaviniams, o ne regresijos!

# Eksperimentams!

tekstas1 = "Čia sugeneruotas tekstas"
tekstas2 = "Mano tekstas"
pasaka = "Vieną kartą gyveno diedukas ir bubutė"

print ( "\033[31m", tekstas1, "\033[0m" )
print ( "\033[1;31m", "paryškintas ", tekstas1, "\033[0m" )
print ( "\033[4;33;41m", "pabraukatas ", tekstas2, "\033[0m" )
print ( "\033[7;33;41m", "inversija ", tekstas2, "\033[0m" )
print ( "\033[0;31;43m", "tas pats be inversijos ", tekstas2, "\033[0m" )
print ( "\033[0;30;41m", "raudonas fonas ", tekstas2, "\033[0m" )


print ( tekstas2 )


def suma(skaicius1, skaicius2): sum = skaicius1 + skaicius2; return sum

def keiciam_sarasa(s):
    s = s + [4]
    return s

mano = [1, 2, 3]
print(keiciam_sarasa(mano))
print(mano)

import numpy as np

a = np.array([2,3,4,5])
a = np.delete(a, 0)
print ( "masyvas a: ", a )

# a = np.array([10, 20, 30, 40, 50])
# naujas = np.delete(a, 2)  # ištrins reikšmę su indeksu 2 (t. y. 30)

# print ( "Originalus masyvas: ", a )
# print ( "Po trynimo: ", naujas )


else: # jeigu yra, bet pilna, einam prie sekančios raidės, B, C, D ir t.t. (iki Z)
            # ord() — tai "ordinal" funkcija. Ji paverčia simbolį į jo skaitinį kodą pagal Unicode (arba ASCII). | chr(65)  # grąžina 'A'
            # chr() — tai "character" funkcija. Ji paverčia skaičių atgal į raidę. ||| chr(ord(group_letter) + 1) grąžina 'B'
            group_letter = chr(ord(group_letter) + 1)
            if group_letter > 'Z':
                raise Exception("Visos grupės nuo A iki Z jau pilnos")