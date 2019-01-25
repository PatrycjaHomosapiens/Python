# Stworzyć nową klasę EmployeeBonus rozszerzającą funkcjonalność Employee o możliwość dodawania uznaniowej premii
from Obiekty_obiektowosc.Obiekty_Zad_2_wersjawykładowcy import Employee


# emp = EmployeeBonus('Jan', 'Kopacz', 100)
# emp.register_time(10)
# emp.give_bonus(10000)
# print(emp.pay_salary())     # ==> 2200

class EmployeeBonus(Employee):  # Employee jest w innym pliku, dlatego musimy zaimportować
                                # najeżdżając na Employee dajem lewy Alt+Enter i wybieramy ten Employee, który
                                # chcemy, ja mam 2 wersje (moja i wykladowcy), wybralam wer wykladowcy
                                # po zaimportowaniu na gorze pojawia się
                                # "from Obiekty_obiektowosc.Obiekty_Zad_2_wersjawykładowcy import Employee"
    def __init__(self, imie, nazwisko, stawka, bonus):  # te nazwy nie musza być takie same jak w Employee
                                                        # były name, surnami, rate, ALE musi być ta sama kolejność
        super().__init__(imie, nazwisko, stawka)
        self.bonus = bonus

    def give_bonus(self, bonus):
        salary = (self.worked_hours * self.rate) + bonus
        return salary

    def pay_salary(self):
        return


emp = EmployeeBonus('Jan', 'Kopacz', 100)
emp.register_time(10)
emp.give_bonus(10000)
print(emp.pay_salary())  # ==> 2200
