# stwórz klasę CashMachine która będzie rzucać wyjatki:
# - jeśli błędna kwota (nie dzieli się przez 50) WrongAmountError
# - jeśli nie da się wydać banknotów EmptyError
# - za dużo banknotów w szufladzie BasketFullError

from Obiekty_obiektowosc.Obiekty_Zad_4_bankomat_wersjawykladowcy import CashMachine
from Obiekty_obiektowosc.Obiekty_Zad_7_wyjatki_dla_bankomatu import *


class CashMachineLimit(CashMachine):  # trzeba było zaimportować klasę CashMachine z "Obiekty_Zad_4_bankomat_wersjawykladowcy"
    def __init__(self, limit):
        super().__init__()
        self._limit = limit

    def put_money(self, banknotes):
        if len(self._szuflada) + len(banknotes) > self._limit:
            raise BasketFullError           # to obsługa przykłdu szczególnego, gdy chcialibyśmy wrzucić za dużo
        super().put_money(banknotes)        # to jest z nadklasy

    def withdraw_money(self, amount):
        if amount % 50 != 0:
            raise WrongAmountError

        wyplata = super().withdraw_money(amount)
        if not wyplata:         # najpierw było tak: if sum(wyplata) != amount:
            raise EmptyError

        return wyplata



cm = CashMachineLimit(5)    # ile banknotów miesci szuflada

try:
    cm.put_money([100,200,100,50,100,100]) # ==> BasketFullError
    cm.put_money([200,100,100])
    cm.withdraw_money(150)   # ==> EmptyError, ten błąd jest kiedy nie można zrealizować
    cm.withdraw_money(140)   # ==> WrongAmountError, ten błąd jest kiedy się nie dzieli przez 50
except CashMachineError as a:            # złap błąd i wrzuć go na zmienną
    print('hurra, mamy błąd :) ')
    print(type(a))


"""
raise WrongAmountError  # trzeba napisać przyk. błąd z pliku "Obiekty_obiektowosc.Obiekty_Zad_7_wyjatki_dla_bankomatu"
      # to co się pojawi u góry "from Obiekty_obiektowosc.Obiekty_Zad_7_wyjatki_dla_bankomatu import WrongAmountError"
      # zamieniam na "from Obiekty_obiektowosc.Obiekty_Zad_7_wyjatki_dla_bankomatu import *"
Po zaimportowaniu możemy ten raise wyrzucić lub zakomentować
"""
