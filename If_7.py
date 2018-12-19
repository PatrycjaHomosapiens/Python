"""
Wczytaj od uzytkownika 5 liczb calkowitych i wypisz na ekran najwiekszą oraz najmniejsza z nich
Zakładają ze wrowadzone liczby rożnią się od siebie

Nie mozna uzywac sortowania, min i max, bo jeszcze tego nie znamy
"""

liczba = int(input("Podaj liczbę: "))
max = liczba
min = liczba

liczba = int(input("Podaj liczbę: "))

if (liczba > max):
    max = liczba
elif (liczba < min):
    min = liczba

liczba = int(input("Podaj liczbę: "))

if (liczba > max):
    max = liczba
elif (liczba < min):
    min = liczba

liczba = int(input("Podaj liczbę: "))

if (liczba > max):
    max = liczba
elif (liczba < min):
    min = liczba

liczba = int(input("Podaj liczbę: "))

if (liczba > max):
    max = liczba
elif (liczba < min):
    min = liczba

print(max, min)



"""
a = int(input("Wpisz 1-szą liczbę całkowitą: "))
b = int(input("Wpisz 2-gą liczbę całkowitą: "))
c = int(input("Wpisz 3-cią liczbę całkowitą: "))
d = int(input("Wpisz 4-tą liczbę całkowitą: "))
e = int(input("Wpisz 5-tą liczbę całkowitą: "))

if (a > b > c > d > e):
    print(a)
    print(e)
"""