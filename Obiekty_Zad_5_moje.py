# sklep internetowy
# użyj klasy produkt
# zrób klase koszyk, do którego mozna wrzucić produkty
# na koniec niecch koszyk powie jaka jest jego sumaryczna wartość

# moje: robimy 2 różne klasy, które będą ze sobą współpracować

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
        pass

    def dodaj(self, prod, ile):
        pass

    def podlicz_sie(self):
        pass


zakupy = Koszyk()
prod1 = Produkt(1, 'jabłko',3)
zakupy.dodaj(prod1, 10)
prod2 = Produkt(2,'gruszka',10)
zakupy.dodaj(prod2, 6)
zakupy.dodaj(prod1, 10)

print(zakupy.podlicz_sie())     # ==> 120
