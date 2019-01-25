# napisz klasę Produkt
# zawierającą informacje o id produktu, nazwie produktu i jego cenie
# dodaj metode wypisującą info o produkcie

# przyklad użycia:
# >>> Produkt(1, 'jabłko', 3)
# >>> pr.wypisz_info()
# 'ID: 1, "jabłko", cena: 3.00 PLN'


# Krok 5:
# używamu pyCarm do wykonania ciężkiej pracy
# nadal pracujemy w definicji __init__
# stajemy po kolei na każdym parametrze i Alt+Enter
# wybieramy opcję Add field <cena|nazwa|id> to class Produkt
# zatwierdzamy czerwone ramki

# moje: robimy self

class Produkt(object):
    def __init__(self, id=1, nazwa='jabłko', cena=3):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def wypisz_info(self):
        pass


def test_przyklad_uzycia():
    # chcemy stworzyć obiekt i zapamiętać go na zmiennej pr
    pr = Produkt(id=1, nazwa='jabłko', cena=3)
    # chcemy żeby taki produkt ładnie wypisywał informacje o sobie
    assert 'ID: 1, "jabłko", cena: 3.00 PLN' == pr.wypisz_info()

