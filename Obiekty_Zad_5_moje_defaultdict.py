# sklep internetowy
# użyj klasy produkt
# zrób klase koszyk, do którego można wrzucić produkty
# na koniec niech koszyk powie jaka jest jego sumaryczna wartosc
from collections import defaultdict


class Produkt():
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena
        self.kolor = "biały"

    def wypisz_info(self):
        return f'ID: {self.id}, "{self.nazwa}", cena: {self.cena:.2f} PLN'

class Koszyk():
    def __init__(self):
        self._pudelko = defaultdict() # po wpisaniu defaultdict() podkreśli się na czerwono, wtedy robimy
                                    # lewy Alt+Enter i na samej górze pojawi się "from collections import defaultdict

    def dodaj(self, prod, ile):
        if prod in self._pudelko:
            self._pudelko[prod] += ile  # już był produkt w pudełku
        else:
            self._pudelko[prod] = ile   # wrzucamy pierwszy raz

    def podlicz_sie(self):

        wynik = 0
        for prod in self._pudelko:
            wynik += self._pudelko[prod] * prod.cena

        sum(x.cena * self._pudelko[x] for x in self._pudelko)   # to jest wyrażenie listowe
        return wynik

zakupy = Koszyk()
prod1 = Produkt(1,'jabłko',3)
zakupy.dodaj(prod1, 10)
prod2 = Produkt(2,'gruszka',10)
zakupy.dodaj(prod2, 6)
zakupy.dodaj(prod1, 10)


print(zakupy.podlicz_sie())     # ==> 120


"""
Moje notatki: tak tworzymy słownik i sprawdzamy, czy coś w nim jest:
sl = dict()
sl['klucz'] = 3
sl
{'klucz': 3}
'ala' in sl
False
"""
