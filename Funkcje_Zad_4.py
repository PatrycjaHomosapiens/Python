# Napisz funkcję silnia

# przyklad:
# silnia(10) = 1*2*3*4*5*6*7*8*9*10

print('\n----- Funkcja SILNIA - sposób 1: iteracyjny, czyli krok po kroku w pętli-----')
def silnia(liczba):
    wynik = 1
    for i in range(1, liczba+1):
        wynik *= i
    return wynik
print(silnia(10))

print('\n----- Funkcja SILNIA - sposób 2: rekurencyjny-----')
# w rekurencji najważniejsze jest to, żeby określić, kiedy ma się zatrzymać
# 1. ustalamy warunek stopu
# 2. wykonujemy krok rekurencyjny (podział zadania na mniejsze kawałki)

def silnia_rek(liczba):
    if liczba == 0:
        return 1

    wynik = liczba * silnia_rek(liczba-1)   # mamy 11 kopi zmiennej liczba, każda z inną wartością
    return wynik

print(silnia_rek(10))









"""
liczba = [1,2,3,4,5,6,7,8,9,10]

def silnia(liczba):
    silnia = 1
    for i in liczba:
        silnia *= liczba
        i +=1
    return
print(silnia(liczba))
"""