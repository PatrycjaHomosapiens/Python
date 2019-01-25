# napisz klasę Produkt
# zawierającą informacje o id produktu, nazwie produktu i jego cenie
# dodaj metode wypisującą info o produkcie

# przyklad użycia:
# >>> Produkt(1, 'jabłko', 3)
# >>> pr.wypisz_info()
# 'ID: 1, "jabłko", cena: 3.00 PLN'


# Krok 4:
# używamu pyCarm do wykonania ciężkiej pracy
# trzeba poprawić __init__ żeby przyjmował 3 paramatry
#     ustawiamy kursor na id=1 i Alt+Enter
#     wybieramy opcję Change signature of __init__
#     zatwierdzamy zmiany (Refactor)
#     w definicji klasy, w metodzie __init__ pojawiły się 3 dodatkowe argumenty

# moje: uzupełniam init o parametry, nawet wartości nie powinno być ('jabłko')

class Produkt(object):
    def __init__(self, id=1, nazwa='jabłko', cena=3):
        pass

    def wypisz_info(self):
        pass


def test_przyklad_uzycia():
    # chcemy stworzyć obiekt i zapamiętać go na zmiennej pr
    pr = Produkt(id=1, nazwa='jabłko', cena=3)
    # chcemy żeby taki produkt ładnie wypisywał informacje o sobie
    assert 'ID: 1, "jabłko", cena: 3.00 PLN' == pr.wypisz_info()

