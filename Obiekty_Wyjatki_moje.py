# łapanie wyjątków może być wielopoziomowe
#


class MojWyjatek(Exception):
    pass

b = 0
try:
    print('przed błędem')
    a = 1/b
    print('po błędzie')
except:     # łapanie WSZYSTKICH wyjątków jak leci
    print('nie dziel przez zero lamo')


b = 0
try:
    print('przed błędem')
    a = 1/b
    print('po błędzie')
except ZeroDivisionError:     # łapanie TYLKO wyjątek ZeroDivisionError
    print('nie dziel przez zero lamo')


b = 1
try:
    print('przed błędem')
    a = 1/b
    c = [1,2,3]
    c[3]                    # błąd, bo lista nie ma elementu 3
    print('po błędzie')
except ZeroDivisionError:  # łapanie TYLKO wyjątek ZeroDivisionError
    print('nie dziel przez zero lamo')
except IndexError:     # łapanie TYLKO wyjątek IndexError
    print('lista nie ma tylu elementów')



# wyrzucanie kilku bledów przez 1 except wpisanych w krotkę

b = 0
try:
    print('przed błędem')
    a = 1/b
    c = [1,2,3]
    c[3]                    # błąd, bo lista nie ma elementu 3
    print('po błędzie')

except (ZeroDivisionError, IndexError):  # można zrobić krotkę, w której wypiszę wszsytkie błędy do wyłapania
    print('wystąpił znany błąd')


# finally

b = 0
try:
    print('przed błędem')
    a = 1/b
    c = [1,2,3]
    c[3]                    # błąd, bo lista nie ma elementu 3
    print('po błędzie')

except (ZeroDivisionError, IndexError):  # można zrobić krotkę, w której wypiszę wszsytkie błędy do wyłapania
    print('wystąpił znany błąd')

finally:
    print('sprzątanie')     # blok kodu, który wywoła się ZAWSZE ("sprzątanie" wywoła się nawet, jeśli był błąd)



# nasz własny wyjątek

class MojWyjatek(Exception):
    pass

try:
    print('przed moim błędem')
    raise MojWyjatek()                # moge wyłapywać wyjątek, który nie jest zdefiniowany
    print('po moim błędzie')
except MojWyjatek:                    # lub tylko sam except:
    print('wyłapany mój wyjątek')

# nie jest dobrze zostawiać pustego except, taki except bez wypisania co łapie wycisza wszystkie możliwe błedy

# jeśli chcemy podejrzeć, jakie są Errory, to piszemy np. "a = Error" w konsoli i wyświetli się lista