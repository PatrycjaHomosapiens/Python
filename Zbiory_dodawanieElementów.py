""" ZBIORY
Napisz program zliczajacy liczbe wartosci unikatowych wprowadzonych przez uzytkownika """

zbior = set()   # deklaracja pustego zbioru
liczba1 = input("Wpisz liczbę nr 1: ")
zbior.add(liczba1)
liczba2 = input("Wpisz liczbę nr 2: ")
zbior.add(liczba2)
liczba3 = input("Wpisz liczbę nr 3: ")
zbior.add(liczba3)

print("W zbiorze jest unikatowych cyfr: " + str(len(zbior)))

print(zbior)   # zwraca wpisane dane w losowej kolejnosci
