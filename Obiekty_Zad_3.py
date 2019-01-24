# Zadanie z BŁĘDAMI, dobre zadanie z testami zostanie dodane na Slacku przez wykładowce
#
# stwórz klase wektor
# wektor ma 2 współrzędne (x i y)
# dodaj metodę __str__ z ładną reprezentacją napisową


class Wektor():
    def __init__(self, x, y):   # init to metoda, która odpala się zawsze jako pierwsza
        self.a = x
        self.b = y

    def __str__(self):
        return f'jestem wektor: [{self.a}, {self.b}]: {Wektor.licznik_wektorow}'

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

#    def __sub__(self, other):
#        return self.a - other.a, self.b - other.b

    def __lt__(self, other):
        dl1 = (self.a ** 2 + self.b **2) ** 0.5
        dl2 = (other.a ** 2 + other.b **2) ** 0.5
        return dl1 < dl2

wek1 = Wektor(5,6)
print(wek1)
wek2 = Wektor(-2, 8)
print(wek2)
print(wek1)

wynik_dodawania = wek1 + wek2   # add
print(wynik_dodawania)

wynik_odejmowania = wek1 - wek2 # sub
print(wynik_odejmowania)

wynik_mnozenia = wek1 * 3   # mul
print(wynik_mnozenia)

wynik_porownania = wek1 < wek2
print(f'czy większy: {wynik_porownania}')

wynik_porownania = wek1 <= wek2
print(f'czy większy lub równy: {wynik_porownania}')

# zdefiniowanie wszystkich funkcji porównujących pozwala używać standardowych mechanizmów np. do sortowania

lista_wektorow = [Wektor(1,1), Wektor(3,5), Wektor(2,2)]

for i in lista_wektorow:
    print(w, end='; ')

lista_wektorow.sort()

for w in lista_wektorow:
    print(w, end='; ')




















