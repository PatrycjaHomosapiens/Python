"""
Pole = 3,14 * r2
Obwód = 2 * 3,14 * r

Napisz program do obliczania pola lub obwodu kola o wskazanym promieniu
Program powienien poprowsic o ponizsze dane
- podaj co bedziemy liczyc - pole czy obwod
- podaj promien kola
"""

obliczenia = input("Wpisz 'pole lub 'obwód': ")
promien = float(input("Wpisz promien koła: "))

if(obliczenia == "pole"):
    print(3.14 * promien * promien)   # zamiast "promien * promien" można "promien ** 2"
elif(obliczenia == "obwód"):
    print(2 * 3.14 * promien)
else:
    print("Wpisano źle")