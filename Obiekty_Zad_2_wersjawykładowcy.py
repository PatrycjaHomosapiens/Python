# zad 2
# napisz klasę Employee, służącą do rejestrowania czasu pracy pracownika
# i wypłacanie pensji na podstawie zdefiniowanej stawki za godzinę.
# Jeśli pracownik pracuje (rejestruje) na raz nie więcej niż 8 godzin
# to liczymy mu te godziny wg normalnej stawki.
# Wszystkie godziny powyżej 8 są traktowane jako nadgodziny i stawka jest
# podwójna.
# przykład:
# emp = Employee(name='Jan',surname='Nowak',rate=100.0)
# emp.register_time(5)
# emp.pay_salary()    --> 500.0
# emp.pay_salary()    --> 0.0
# emp.register_time(10)
# emp.pay_salary()    --> 1200.0
# emp.register_time(8)
# emp.register_time(8)
# emp.register_time(8)
# emp.pay_salary()    --> 2400.0


class Employee:

    def __init__(self, name, surname, rate):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.worked_hours = 0
        self.overtime = 0

    def register_time(self, new_hours):
        if new_hours > 8:
            self.overtime += (new_hours - 8)
        self.worked_hours += min(new_hours, 8)

    def pay_salary(self):
        salary = self.overtime * 2 * self.rate + self.worked_hours * self.rate
        self.worked_hours = 0
        self.overtime = 0
        return salary


# ============ testy developerskie (sprawdzanie algorytmu) =========
def test_dev_create():
    emp = Employee(name='Jan', surname='Nowak', rate=100.0)
    assert 'Jan' == emp.name
    assert 'Nowak' == emp.surname
    assert 100.0 == emp.rate
    assert 0.0 == emp.worked_hours
    assert 0.0 == emp.overtime


def test_dev_register_normal_hours():
    emp = Employee(name='Jan', surname='Nowak', rate=100.0)
    emp.register_time(5)
    assert 5 == emp.worked_hours
    assert 0 == emp.overtime

def test_dev_register_overtime():
    emp = Employee(name='Jan', surname='Nowak', rate=100.0)
    emp.register_time(10)
    assert 8 == emp.worked_hours
    assert 2 == emp.overtime

def test_dev_pay_salary():
    emp = Employee(name='Jan', surname='Nowak', rate=100.0)
    emp.register_time(5)
    assert 500.0 == emp.pay_salary()
    assert 0 == emp.worked_hours
    assert 0 == emp.overtime


# ============= testy funkcjonalne (umowa z klientem) ==============
# def test_create():
#     emp = Employee(name='Jan', surname='Nowak', rate=100.0)
#     assert 'Jan Nowak: 100.00' == emp.print_info()


def test_register_normal_hours():
    emp = Employee(name='Jan', surname='Nowak', rate=100.0)
    emp.register_time(5)
    assert 500.0 == emp.pay_salary()


def test_global():
    emp = Employee(name='Jan',surname='Nowak',rate=100.0)
    assert 0.0 == emp.pay_salary()
    emp.register_time(5)
    assert 500.0 == emp.pay_salary()
    assert 0.0 == emp.pay_salary()
    emp.register_time(10)
    assert 1200.0 == emp.pay_salary()
    emp.register_time(8)
    emp.register_time(8)
    emp.register_time(8)
    assert 2400.0 == emp.pay_salary()