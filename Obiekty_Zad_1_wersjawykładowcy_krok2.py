# napisz klasę Produkt
# zawierającą informacje o id produktu, nazwie produktu i jego cenie
# dodaj metode wypisującą info o produkcie

# przyklad użycia:
# >>> Produkt(1, 'jabłko', 3)
# >>> pr.wypisz_info()
# 'ID: 1, "jabłko", cena: 3.00 PLN'


# Krok 2:
# używamu pyCarm do wykonania ciężkiej pracy
# ustawiamy kursor na podkreślonym na czerwono Produkt i używamy kombinacji Alt+Enter
# wybieramy opcję Create class 'Produkt'
# w automatycznie wygenerowanej klasie zatwierdzamy wszystko co się podświetla czerwoną ramką
#     object - mozna skasować, można zostawić, nie robi różnicy. i tak nasz Produkt dziedziczy po object

# moje: w tym kroku wyprodukowaliśmy pustą klasę

class Produkt(object):
    pass


def test_przyklad_uzycia():
    # chcemy stworzyć obiekt i zapamiętać go na zmiennej pr
    pr = Produkt(id=1, nazwa='jabłko', cena=3)
    # chcemy żeby taki produkt ładnie wypisywał informacje o sobie
    assert 'ID: 1, "jabłko", cena: 3.00 PLN' == pr.wypisz_info()

