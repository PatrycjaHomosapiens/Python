# napisz klasę Produkt
# zawierającą informacje o id produktu, nazwie produktu i jego cenie
# dodaj metode wypisującą info o produkcie

# przyklad użycia:
# >>> Produkt(1, 'jabłko', 3)
# >>> pr.wypisz_info()
# 'ID: 1, "jabłko", cena: 3.00 PLN'


# Krok 3:
# używamu pyCarm do wykonania ciężkiej pracy
#
# teraz świecą się kawałki kodu pod spodem:
# 1. (id=1, nazwa='jabłko', cena=3)
# 2. wypisz_info

# ad 1. tu trzeba stworzyć konstruktor (metodę __init__) który przyjmie 3 argumenty
# dodajemy ją do klasy Produkt (niestety trzeba wpisać ręcznie ;-)
# ad 2. ustawiamy kursor na wypisz_info i Alt+Enter
# wybieramy opcję Add method wypisz_info() to class Produkt
# zatwierdzamy czerwone ramki

# moje: w tym kroku dodajemy metodę, metoda jest pusta, na razie robimy szkielet
# układamy pudełka, do których później bedziemy wkladać rzeczy

class Produkt(object):
    def __init__(self):
        pass

    def wypisz_info(self):
        pass


def test_przyklad_uzycia():
    # chcemy stworzyć obiekt i zapamiętać go na zmiennej pr
    pr = Produkt(id=1, nazwa='jabłko', cena=3)
    # chcemy żeby taki produkt ładnie wypisywał informacje o sobie
    assert 'ID: 1, "jabłko", cena: 3.00 PLN' == pr.wypisz_info()

