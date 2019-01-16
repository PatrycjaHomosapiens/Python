"""
Napisz program, ktÓry sprawdz czy wpisana liczba jest parzysta czy nieparzysta """

liczba = input("Wpisz liczbę: ")
liczba = int(liczba)

if (liczba % 2 == 0):
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

""" ODWROTNY ZAPIS:

if (liczba % 2 != 0):
    print("Liczba nieparzysta")
else:
    print("Liczba parzysta")
"""
