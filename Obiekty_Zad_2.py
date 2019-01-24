# Zadanie z BŁĘDAMI, dobre zadanie z testami zostanie dodane na Slacku przez wykładowce
# 
# zad 2
# napisz klasę Employee, służącą do rejestrowania czasu pracy pracownika
# i wypłacanie pensji na podstawie zdefiniowanej stawki za godzinę.
# Jeśli pracownik pracuje rejestruje na raz nie więcej niż 8 godzin
# to liczymy mu te godziny wg normalnej stawki.
# Wszystkie godziny powyżej 8 są traktowane jako nadgodziny i stawka jest podwójna.
# przykład:
# emp = Employee(name='Jan',surname='Nowak',rate=100.0)
# emp.register_time(5)
# emp.pay_salary()    # --> 500.0
# emp.pay_salary()    # --> 0.0
# emp.register_time(10)
# emp.pay_salary()    # --> 1200.0
# emp.register_time(8)
# emp.register_time(8)
# emp.register_time(8)
# emp.pay_salary()    # --> 2400.0

# moje: będziemy robić 2 metody
# emp to zewnętrzna zmienna, na którą wrzuce obiekt
# testy mają 2 rodzaje: funkcjonalne (to kiedy spisujemy umowe z klientem) i developerskie (na etapie tworzenia, klient tego nie widzi nigdy)

# ============ testy developerskie (sprawdzanie algorytmu) =========
def test_dev_create():
    emp = Employee(name='Jan', surname='Nowak', rate=100.0)
    assert 'Jan' == emp.name
    assert 'Nowak' == emp.surname
    assert 100.0 == emp.rate
    assert 0.0 == emp.hours
    assert  0.0 == emp.overtime

def test_dev_register_normal_hours():
    emp = Employee(name='Jan', surname='Nowak', rate=100.0)
    emp.register_time(5)
    assert 5 == emp.hours
    assert 0 == emp.overtime

def test_dev_pay_salary():
    emp = Employee(name='Jan', surname='Nowak', rate=100.0)
    emp.register_time(5)
    assert 500.0 == emp.pay_salary()
    assert 5 == emp.worked_hours   # chcę zobaczyć, że po wypłacie przepracowane godziny się zerują
    assert 0 == emp.overtime


# ============= testy funkcjonalne (umowa z klientem) ==============
def test_create2():
    emp = Employee(name='Jan', surname='Nowak', rate=100.0)
    assert 'Jan Nowak: 100.00' == emp.print_info()  # test print_info mogłoby nie być, jest trochę nadmiarowy

def test_register_normal_hours():
    emp = Employee(name='Jan', surname='Nowak', rate=100.0)
    emp.register_time(5)
    assert 500.0 == emp.pay_salary()

# rozwiązanie (nie testy):

class Employee():

    def __init__(self, name, surname, rate):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.worked_hours = 0
        self.overtime = 0

    def register_time(self, worked_hours):
        if self.worked_hours > 8:
            self.overtime += (self.worked_hours - 8)
        self.worked_hours += min(worked_hours, 8)


    def pay_salary(self):
        if self.worked_hours > 8:                       # jesli przepracowal wiecej niz 8 godz. to
            salary = 8 * self.rate + (self.worked_hours - 8) * 2 * self.rate
            self.worked_hours = 0
            return salary

        salary = self.rate * self.worked_hours
        self.worked_hours = 0
        return salary

        salary = self.rate * self.worked_hours
        self.worked_hours = 0


'''
# moje proby napisania: 

class Employee():
    def __init__(self, name, surname, rate):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.work_time = 0
        self.overhours = 0
        self.normal_hours = 0

    def pay.salary(self):
        if self.work_time > 8:
            normal_hours = register_time() * 100
            overhours = register_time() * 100 + overhours * 100 * 2

    def register_time(self):




print(emp.pay_salary(10))

emp = Employee(name='Jan',surname='Nowak',rate=100.0)
emp.register_time(5)
emp.pay_salary()    # --> 500.0
emp.pay_salary()    # --> 0.0
emp.register_time(10)
emp.pay_salary()    # --> 1200.0
'''