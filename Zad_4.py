# Napisz funkcję silnia

# przyklad:
# silnia(10) = 1*2*3*4*5*6*7*8*9*10

print('\n----- Funkcja SILNIA - sposób 1: ......')
def silnia(liczba):
    wynik = 1
    for i in range(1, liczba+1):
        wynik *= i
    return wynik
print(silnia(10))

print('\n----- Funkcja SILNIA - sposób 2: ......')









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