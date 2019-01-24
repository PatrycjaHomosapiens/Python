# robimy bankomat
# bankomat ma pieniadze w srodku, ale nie chcemy, żeby każdy mógł zajrzeć ile
# czyli szuflada z banknotami ma być naszą zmienną prywatną
# bankomat umozliwia włożenie pieniedzy do szuflady
# i wyplaty gotówki
# wyplaca pieniadze tylko jesli kwota jest mozliwa do zrealizowania
# dostepnymi banknotami
# jesli nie mozna zrealizowac żądanej kwoty to bankomat zraca pustą listę

# przyklad
cash_machine = CashMachine()
cash_machine.put_money([200,100,100,50])
wyplata  = cash_machine.withdraw_money(150)
print(wyplata) # ==> [100,50]
druga_wyplata = cash_machine.withdraw_money(150)
print(druga_wyplata) # ==> []