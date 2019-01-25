# napisz klasę Produkt
# zawierającą informacje o id produktu, nazwie produktu i jego cenie
# dodaj metode wypisującą info o produkcie

# przyklad użycia:
# >>> Produkt(1, 'jabłko', 3)
# >>> pr.wypisz_info()
# 'ID: 1, "jabłko", cena: 3.00 PLN'


# Krok 5:
# poprawiamy definicję metody wypisz_info
# KOPIUJEMY (lepiej nie przepisywać, bo można zrobić literówkę!) spodziewany wynik

# moje: robimy return, najlepiej to skopiować, bo przepisując można zrobić łatwo błąd

class Produkt(object):
    def __init__(self, id=1, nazwa='jabłko', cena=3):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def wypisz_info(self):
        return 'ID: 1, "jabłko", cena: 3.00 PLN'


def test_przyklad_uzycia():
    # chcemy stworzyć obiekt i zapamiętać go na zmiennej pr
    pr = Produkt(id=1, nazwa='jabłko', cena=3)
    # chcemy żeby taki produkt ładnie wypisywał informacje o sobie
    assert 'ID: 1, "jabłko", cena: 3.00 PLN' == pr.wypisz_info()

