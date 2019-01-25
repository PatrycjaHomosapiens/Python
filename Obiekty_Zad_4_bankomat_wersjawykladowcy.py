# robimy bankomat
# bankomat ma pieniadze w srodku, ale nie chcemy, żeby każdy mógł zajrzeć ile
# czyli szuflada z banknotami ma być naszą zmienną prywatną
# bankomat umozliwia włożenie pieniedzy do szuflady
# i wyplaty gotówki
# wyplaca pieniadze tylko jesli kwota jest mozliwa do zrealizowania
# dostepnymi banknotami
# jesli nie mozna zrealizowac żądanej kwoty to bankomat zraca pustą listę

# przyklad
class CashMachine():
    def __init__(self):
        self._szuflada = []

    def put_money(self, banknotes):
        self._szuflada.extend(banknotes)
        self._szuflada.sort(reverse=True)

    def withdraw_money(self, amount):
        wyplata = []
        for papier in self._szuflada:
            if papier + sum(wyplata) <= amount:
                wyplata.append(papier)

        if sum(wyplata) == amount:
            for papier in wyplata:
                self._szuflada.remove(papier)
            return wyplata

        return []


# cash_machine = CashMachine()
# cash_machine.put_money([100,200,100,50])
# wyplata  = cash_machine.withdraw_money(150)
# print(wyplata) # ==> [100,50]
# druga_wyplata = cash_machine.withdraw_money(150)
# print(druga_wyplata) # ==> []
#
# cs = CashMachine()
# cs.put_money([20,20,20,50,100,200])
# wyplata = cs.withdraw_money(160)
#
# cs = CashMachine()
# cs.put_money([50,100,50,50,200])
# wyplata = cs.withdraw_money(300)