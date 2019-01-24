# stwórz klasę wektor
# wektor ma dwie współrzędne (x i y)
# dodaj metodę __str__ z ładną reprezentacją napisową

class Wektor():
    licznik_wektorów = 0  # wspolne dla wszystkich obiektow

    def __init__(self, x, y):
        self.a = x
        self.b = y
        Wektor.licznik_wektorów += 1

    def __str__(self):
        return f'jestem wektor {self.a},{self.b}: {Wektor.licznik_wektorów}'

    def __add__(self, other):
        return Wektor(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Wektor(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Wektor(self.a * other, self.b * other)

    def dlugosc(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def __lt__(self, other):
        return self.dlugosc() < other.dlugosc()

    def __le__(self, other):
        return self.dlugosc() <= other.dlugosc()

    def __gt__(self, other):
        return self.dlugosc() > other.dlugosc()

    def __ge__(self, other):
        return self.dlugosc() >= other.dlugosc()

    def __eq__(self, other):
        return self.dlugosc() == other.dlugosc()

    def __ne__(self, other):
        return self.dlugosc() != other.dlugosc()


wek1 = Wektor(5, 6)
print(wek1)
wek2 = Wektor(-2, 8)
print(wek2)
print(wek1)

wynik_dodawania = wek1 + wek2  # add
print(wynik_dodawania)

wynik_odejmowania = wek1 - wek2  # sub
print(wynik_odejmowania)

wynik_mnozenia = wek1 * 3  # mul
print(wynik_mnozenia)

wynik_porównania = wek1 < wek2
print(f'czy wiekszy: {wynik_porównania}')

wynik_porównania = wek1 <= wek2
print(f'czy wiekszy lub równy: {wynik_porównania}')

# zdefiniowanie wszystkich funkcji porównujących pozwala
# używać standardowych mechanizmów np do sortowania
lista_wektorów = [Wektor(1, 1), Wektor(3, 5), Wektor(2, 2)]

print('\n======= przed sortowaniem ====\n')
for w in lista_wektorów:
    print(w, end='; ')

lista_wektorów.sort()

print('\n\n======= po sortowaniu ====\n')

for w in lista_wektorów:
    print(w, end='; ')

lista_wektorów.sort(reverse=True)

print('\n\n======= po sortowaniu odwrotnym ====\n')

for w in lista_wektorów:
    print(w, end='; ')

print()
