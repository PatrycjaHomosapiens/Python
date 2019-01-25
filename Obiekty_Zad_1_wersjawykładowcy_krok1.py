# napisz klasę Produkt
# zawierającą informacje o id produktu, nazwie produktu i jego cenie
# dodaj metode wypisującą info o produkcie

# przyklad użycia:
# >>> Produkt(1, 'jabłko', 3)
# >>> pr.wypisz_info()
# 'ID: 1, "jabłko", cena: 3.00 PLN'


# Krok 1:
# czytamy dokładnie treść zadania (wymagania projektowe).
# staramy się przełożyć wszystko co wiemy o zachowaniu obiektu na testy
# w trakcie pisania testów może się okazać niezbędna współpraca z zamawiającym,
#     żeby doszczegółowić wymagania, np. w przypadkach granicznych

# test to rodzaj umowy pomiędzy zamawiającym (klientem) a wykonawcą (programistą)
# na razie ten test nie jest spełniony. to jest na razie tylko nasza specyfikacja.
# tak chcemy żeby obiekt się zachowywał, jak już go zaprogramujemy.

def test_przyklad_uzycia():
    # chcemy stworzyć obiekt i zapamiętać go na zmiennej pr
    pr = Produkt(id=1, nazwa='jabłko', cena=3)
    # chcemy żeby taki produkt ładnie wypisywał informacje o sobie
    assert 'ID: 1, "jabłko", cena: 3.00 PLN' == pr.wypisz_info()

