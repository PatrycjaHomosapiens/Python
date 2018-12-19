"""
Napisz program wczytujacy z klawiatury wartości, a następnie wyswietlajacy srednia tych wartości,
niech program konczy wprowadzanie, kiedy natrafi na cyfre 0, ktorej nie bierzemy do liczenia
Komentarz: najlepiej wykorzystać while, zaczynamy z pustym kontem, czyli suma jest 0
i ilosc wpisanych liczb (jako mianownik do średniej) też jest równy zero
"""

suma = 0
ile = 0
while(True):
    x = int(input("Podaj liczbę (0 aby zakończyć): "))

    if x == 0:
        break
    else:
        suma = suma + x
        ile = ile +1

print(suma/ile)


# inny sposob na rozwiązanie:

sum = 0
x = 0
srednia = 0
a = int(input("Wprowadź liczbę: "))

while (a != 0)
    x = x + 1
    sum = sum + a
    srednia = sum / x
    print(x, srednia)
    a = int(input("Wprowadź liczbę: "))
else:
    print("Koniec", "Średnia = ", srednia)