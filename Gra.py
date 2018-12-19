"""
Gra w losowanie liczby, program mówi że liczba jest za mała lub za duża, aż do trafienia
Komentarz: można liczyć ilość prób
"""

import random

liczba = random.randint(0,100)   # kod na losowanie liczby losowej

while(True):
    x = int(input("Podaj liczbę: "))
    if (x == liczba):
        print("Brawo")
        break
    elif (x > liczba):
        print("Podana liczba jest za duża")
    elif (x < liczba):
            print("Podana liczba jest za mała")