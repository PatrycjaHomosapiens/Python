
b= 0
try:
    print('przed bledem')
    a = 1/b
    print('po bledzie')
except :    # łapanie WSZYSTKICH wyjątkow jak leci
    print('nie dziel przez zero lamo')


b=1
try:
    print('przed bledem')
    a = 1/b
    c = [1,2,3]
    c[3]
    print('po bledzie')
except ZeroDivisionError:   # łapię TYLKO wyjątek ZeroDivisionError
    print('nie dziel przez zero lamo')
except IndexError:          # łapię TYLKO wyjątek IndexError
    print('lista nie ma tylu elementów')


b=0
try:
    print('przed bledem')
    a = 1/b
    c = [1,2,3]
    c[3]
    print('po bledzie')

except (ZeroDivisionError, IndexError):   # łapię TYLKO wypisane wyjątki
    print('wystapil znany błąd')

b=0
try:
    print('przed bledem')
    a = 1/b
    c = [1,2,3]
    c[2]
    print('po bledzie')

except (ZeroDivisionError, IndexError):   # łapię TYLKO wypisane wyjątki
    print('wystapil znany błąd')

finally:    # blok kodu, który wykona się ZAWSZE, niezależnie czy był  błąd czy go nie było
    print('sprzątanie')



class MojWyjatek(Exception):
    pass

try:
    print('przed moim bledem')
    raise MojWyjatek()
    print('po moim bledzie')
except MojWyjatek:
    print('wylapany moj wyjatek')
