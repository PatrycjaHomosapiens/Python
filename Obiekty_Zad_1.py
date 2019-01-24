# Zadanie z BŁĘDAMI, dobre zadanie z testami zostanie dodane na Slacku przez wykładowce
#
# napisz klasę produkt
# zawierajaca informacje o id produktu, nazwie produktu i jego cenie
# dodaj metode wpisujaca info o produkcie
# przykład użycia:

# pr = Produkt(1, 'jabłko', 3)
# pr.wypisz_info()
#'>>> 'ID': 1, "jabłko", cena: 3.00 PLN'

'''
# TRADYCYJNE PODEJSCIE - robimy treść zadania

class Produkt():
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena
        self.kolor = "biały"    # to są jakieś moje wewnętrzne dane, nie musza być w nawiasie wyżej

    def podaj_dane_o_produkcie(self):
        return f'Jestem produktem o id: {self.id}, o nazwie: {self.nazwa}, w cenie: {self.cena:.2f} zł.'

pr = Produkt(1, 'jabłko', 3)
print(pr.podaj_dane_o_produkcie())
'''

# ROBIMY TEST - używamy treści zadania, aby zrobić test

class Produkt():
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena
    def wypisz_info(self):
        return f'ID: {self.id}, "{self.nazwa}", cena: {self.cena:.2f} PLN'  # return jest skopiowanym assert

def test_ogolny():
    pr = Produkt(1, 'jabłko', 3)
    assert 'ID: 1, "jabłko", cena: 3.00 PLN' == pr.wypisz_info()



