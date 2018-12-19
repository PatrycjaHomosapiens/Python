"""
ZBIORY
Napisz program zliczajacy liczbe wartosci unikatowych wprowadzonych przez uzytkownika
"""

zbior = set()   # deklaracja pustego zbioru
liczba1 = input("Wpisz liczbę: ")
zbior.add(liczba1)
liczba2 = input("Wpisz liczbę: ")
zbior.add(liczba2)
liczba3 = input("Wpisz liczbę: ")
zbior.add(liczba3)

print("W zbiorze jest unikatowych cyfr " + str(len(zbior)))

print(zbior)   # zwraca wpisane dane w losowej kolejnosci


# kolejnosc, + , ilosc liczb