# Stworzyć nową klasę EmployeeBonus rozszerzającą funkcjonalność Employee o możliwość dodawania uznaniowej premii
from Obiekty_obiektowosc.Obiekty_Zad_2_wersjawykładowcy import Employee

# emp = EmployeeBonus('Jan', 'Kopacz', 100)
# emp.register_time(10)
# emp.give_bonus(10000)
# print(emp.pay_salary())     # ==> 2200


# class EmployeeBonus(Employee):
#
#    def __init__(self, imie, nazwisko, pensja):
#        super().__init__(imie, nazwisko, pensja)
#        self.skarbonka = 0
#
#    def give_bonus(self, napiwek):
#        self.skarbonka += napiwek
#        return napiwek
#
#    def pay_salary(self):
#        wyp = super().pay_salary() + self.skarbonka
#        self.skarbonka = 0
#        return wyp

# class EmployeeBonus(Employee):
#     def __init__(self, name, surname, rate): #mozna rownie dobrze dac 'x y z' w parametrach
#         super().__init__(name,surname,rate)
#         self.bonus = 0
#
#     def give_bonus(self, bonus):
#         self.bonus += bonus             # self bonus jest moim koszyczkiem do ktorego dorzucam kazdy nastepny bonus
#
#     def pay_salary(self):
#         pensja = super().pay_salary()  # wywoluje metode pay salary z nadklasy
#         total = pensja + self.bonus
#         self.bonus = 0
#         return total

class EmployeeBonus(Employee):

   def __init__(self,name,surname,rate):
       super().__init__(name,surname, rate)
       self.bonus = 0


   def give_bonus(self,bonus):
       self.bonus += bonus


   def pay_salary(self):
       wyplata = super().pay_salary() + self.bonus
       self.bonus = 0
       return wyplata

emp = EmployeeBonus('Jan', 'Kopacz', 100)
emp.register_time(10)
emp.give_bonus(1000)
print(emp.pay_salary())  # ==>2200
emp.give_bonus(500)
emp.give_bonus(500)
emp.give_bonus(500)
print(emp.pay_salary())  # ==>1500



"""
Moje notatki:

class EmployeeBonus(Employee):  # Employee jest w innym pliku, dlatego musimy zaimportować
                                # najeżdżając na Employee dajem lewy Alt+Enter i wybieramy ten Employee, który
                                # chcemy, ja mam 2 wersje (moja i wykladowcy), wybralam wer wykladowcy
                                # po zaimportowaniu na gorze pojawia się
                                # "from Obiekty_obiektowosc.Obiekty_Zad_2_wersjawykładowcy import Employee"
    def __init__(self, imie, nazwisko, stawka):  # te nazwy nie musza być takie same jak w Employee
                                                        # były name, surnami, rate, ALE musi być ta sama kolejność
                                                        # w tym init nie muszę dawać bonus, bo to jest zero na starcie
                                                        # gdyby coś było na starcie, to musiałoby być
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

"""










