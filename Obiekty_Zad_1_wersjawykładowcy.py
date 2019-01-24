# napisz klasę Produkt
# zawierającą informacje o id produktu, nazwie produktu i jego cenie
# dodaj metode wypisującą info o produkcie

# przyklad użycia:


class Produkt():
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena
        self.kolor = "biały"

    def wypisz_info(self):
        return f'ID: {self.id}, "{self.nazwa}", cena: {self.cena:.2f} PLN'


def test_ogolny():
    pr = Produkt(1, 'jabłko', 3)
    assert 'ID: 1, "jabłko", cena: 3.00 PLN' == pr.wypisz_info()