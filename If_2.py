"""
Napisz program ktory sprawdz czy wpisana liczba jest parzysta i nieparzysta
"""


liczba = input("Wpisz liczbę: ")
liczba = int(liczba)

if (liczba % 2 == 0):
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

"""
liczba = input("Wpisz liczbę: ")
liczba = int(liczba)

if (liczba % 2 != 0):
    print("Liczba nieparzysta")
else:
    print("Liczba parzysta")
"""