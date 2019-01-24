# deklaracja funkcji

"""def moja_prosta_funkcja():  # jeśli coś się skończyło dwukropkiem, to następna linia będzie wcięta
    pass    # to jest instrukcja pusta, przynajmniej jedna linia w funkcji musi być pusta"""


def moja_prosta_funkcja():
    print("cześć, działam")


moja_prosta_funkcja()
moja_prosta_funkcja()


# m
def funkcja_z_parametrami(a, b):
    return a + b


c = funkcja_z_parametrami(2, 3)
print(c)
print(funkcja_z_parametrami(2, 3))

d = funkcja_z_parametrami("ala", "makota")
print(d)  # zadziała, bo stringi potrafią się dodawać

# Python nie potrafi dodawać int do str
# e = funkcja_z_parametrami(1, "ala")
# print(e)    # błąd bo nie można dodać int do str

# wielokrotne przypisanie
a, b, c = 1, 2, 3

# coś z tuplą
(a, b, c) = (1, 2, 3)
print(f"a={a}, b={b}, c={c}")  # to jest tupla, tupla się nie zmieni
tupla = (a, b, c)
print(tupla)
a = 33
print(tupla)  # to się nie zmieni, zostanie (1,2,3), bo tupla jest niezmienna
(a, b) = (b, a)  # to robi: co spr.
print(f"a={a}, b={b}")


# PEP 8 - to jest dokument opisujący np. jak mają wyglądać funcje, zmienne, gdzie przecinki, spacje itd.
# lewy alt + ENTER, następnie wybieram "Reformat file" i wszystko się poprawi automatycznie (zrobią się spacje, tam gdzie trzeba)

def funkcja_zwracajaca_wiele_wynikow():
    return 1, "ala", [2, 3, 4]


a, b, c = funkcja_zwracajaca_wiele_wynikow()
print(f"a={a}, b={b}, c={c}")


def funkcja_z_parametrami(a, b):
    c = a + b
    return a + b  # "return" kończy funkcję, nie mozna nawet dać print pod tą linijką
    print(c)  # to się nie wydrukuje, bo jest po return, musi być bez wcięcia


def funkcja_dwie_sytuacje(a, b):
    if type(a) == int:
        return a
    return b  # nie trzeba w tej konstrukcji daewać innego if
    print("ta linia nigdy nie zostanie wywołana,\n"
          "bo jest po retunr")


# ZADANIE: napisz progrmam, który określi czy liczba jest parzysta czy nie

print("====== zad 1 - wersja 1, opcja z wydrukiem")


# to jest tylko budowanie napisu na konsoli, ale funckja tutaj nie zwraca wyniku
def czy_parzysta(liczba):  # to jest PRZEPIS NA CIASTO
    if liczba % 2 == 0:
        print(f'{liczba}: to jest liczba parzysta')
    else:
        print(f"{liczba}: to jest liczba nieparzysta")


print(czy_parzysta(7))  # to ma zrócić False, to jest WYNIK PRZEPISU NA CIASTO, np. muffinek
print(czy_parzysta(12))  # to ma zrócić True

print("====== zad 1 - wersja 2, budujemy funkcje =====")


def czy_parzysta_v2(liczba):  # to jest PRZEPIS NA CIASTO
    if liczba % 2 == 0:
        return True
    else:  # to możemy wyrzucić, w następnym przykładzie jest bez 'else'
        return False


print(czy_parzysta_v2(7))  # to ma zrócić False, to jest WYNIK PRZEPISU NA CIASTO, np. muffinek
print(czy_parzysta_v2(12))  # to ma zrócić True

print("====== zad 1 - wersja 3, budujemy funkcje, ale bez 'else' =====")


def czy_parzysta_v3(liczba):  # to jest PRZEPIS NA CIASTO
    if liczba % 2 == 0:
        return True
    return False


print(czy_parzysta_v3(7))  # to ma zrócić False, to jest WYNIK PRZEPISU NA CIASTO, np. muffinek
print(czy_parzysta_v3(12))  # to ma zrócić True

print("====== zad 1 - wersja 4, budujemy funkcje, wersja najkrótsza =====")


def czy_parzysta_v4(liczba: int) -> bool:  # nie wiem co to jest "(liczba:int) -> bool"
    return liczba % 2 == 0


print(czy_parzysta_v4(7))  # to ma zrócić False, to jest WYNIK PRZEPISU NA CIASTO, np. muffinek
print(czy_parzysta_v4(12))  # to ma zrócić True

print('===== *args ========')


def duzo_parametrow(*args):  # to jest zestaw parametrów, czyli krotka
    print(args)


duzo_parametrow(1)
duzo_parametrow(1, 2, 3)
duzo_parametrow()

print('\n------ piszemy własną uproszczona wersję print-------')

print('ala', 'ola', 'zenek', sep='#', end='@')  # sep to separator, a end to znak na końcu
print('ala', 'ola', 'zenek', sep='#', end='@')
print('ala', 'ola', 'zenek', sep='#', end='@')

# print()     # pusty print łamie linię
print('\n-------moje_wypisz---------')


def moje_wypisz(*args, lacznik=' ', koniec='\n'):
    print(lacznik.join(args) + koniec, sep='', end='')

moje_wypisz('ala', 'ola', 'zenek', lacznik='#', koniec='@')
moje_wypisz('ala', 'ola', 'zenek', lacznik='#', koniec='@')
moje_wypisz('ala', 'ola', 'zenek', lacznik='#', koniec='@')

print('\n------ **kwargs-----')
def moje_parametry(**kwargs):
    print(kwargs)

moje_parametry(ala=9, ola=7, zenek='jakis nais')
# moje parametry nie umieją zrozumieć nienazwanych parametrów (pozycyjnych)
# moje_parametry

print('\n-----FUNKCJA Z DOWOLNĄ LICZBĄ PARAMETRÓW-----DOBRE ROZWIĄZANIE')
# FUNKCJA Z DOWOLNĄ LICZBĄ PARAMETRÓW
# A co jeśli nie wiemy ile i jakich argumentów nazwanych dostaniemy
# Słownik **kwargs

x = 5
y = 6
z = 7

def dowolneArgumenty(*args, **kwargs):
    print(f'argumenty bez nazw (krotka args): {args}')
    print(f'argumenty nazwane (słownik kwargs): {kwargs}')

dowolneArgumenty(1000,2,3,x,y,z, ala=67, kot=90, mleko='3,2%')  # 1000,2,3,x,y,z - te są nienazwane, czyli pozycyjne
                                                                # ala=67, kot=90, mleko='3,2%' - te są nazwane



print('\n-----FUNKCJA Z DOWOLNĄ LICZBĄ PARAMETRÓW-----EKSPERYMENTY, robimy specjalnie błędy------błąd 1----')
# FUNKCJA Z DOWOLNĄ LICZBĄ PARAMETRÓW
# A co jeśli nie wiemy ile i jakich argumentów nazwanych dostaniemy
# Słownik **kwargs

x = 5
y = 6
z = 7

def dowolneArgumenty(*args, **kwargs):
    print(f'argumenty bez nazw (krotka args): {args}')
    print(f'argumenty nazwane (słownik kwargs): {kwargs}')

dowolneArgumenty(1000,2,3,x,y,z, ala=67, kot=90, mleko='3,2%')  # 1000,2,3,x,y,z - te są nienazwane, czyli pozycyjne
                                                                # ala=67, kot=90, mleko='3,2%' - te są nazwane


"""
print('====== łączenie przez join =====')

a = ['ala','ola','zenek']
' '.join(a)
print(a)
"""


# PROGRAMOWANIE OBIEKTOWE (czyli OOP):
# Zasadniczą koncepcją w podejściu obiektowym do programowania jest połączenie w całość danych oraz algorytmów, które na tych danych operują
# Obiekt posiad pewne własnosci, czyli dane oraz pewne metody, czyli algorytmy do przetwarania tych danych
# Zbior obiektów o tych samch własnosciach i metodach nazywamy klasą
# Pakowanie paczki, czyli dane-algorytm, dane-algorytm...
# Jak tworzymy słownik, to jest tworzenie obiektu, lista tak samo
# Jest programowanie proceduralne oraz obiektowe
# Obiektowość: abstrakcja, hermetyzacja, polimorfizm, dziedziczenie
# Klasa to przepis na ciasto, a czy ja upiekę 1 czy 50 ciast, to zależne od sytuacji
# Abstrakcja -
# Hermetyzacja - Python ma cały kod na wierzchu, ale jest taka umowa, żeby tylko zobaczyć, ale tego nie zmieniać
# Polimorfizm - można mieć wiele robotów wg tega samego schematu, ale każdy jest np. innego koloru, ma inną szybkość
# Dziedziczenie - można rozbudowywac, to co już mamy, czyli powstaje nowy przepis na ciasto, bo do tego co już istnieje dodaję coś nowego. Rozwijam funkcjonalność, ne

# Klasa - przepis na ciasto, to podstawowy schemat
# Konstruktor
# Pola - wszystko co jest w środku
# Metody - to wszystko co robot potrafi (np. polecenia dla robota: rusz się, kop, biegnij)
# Obiekty - to te roboty, upieczone ciasta, czyli wyniki
# Obiekty nazwywamy z małej litery, klasy z Wielkiej Litery