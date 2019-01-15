"""
Cwiczenie 60 (zadanie domowe z pierwszego modułu kursu Python):
Pętle
Napisz program, który pobiera od użytkownika ciąg liczb całkowitych.
Pobieranie danych kończone jest podaniem wartości 0 (nie wliczana do danych).
W następnej kolejności program powinien:
- wyświetlić wartości największej oraz najmniejszej z podanych liczb (przy wykorzystaniu pętli !)
- Wyliczyć średnią arytmetyczną z podanych liczb.
"""

podaneLiczby = []
wynik = 0
srednia = 0

while True:
    liczba = int(input("Podaj liczbę całkowitą: "))
    if (liczba != 0):
        podaneLiczby.append(liczba)
        wynik += liczba
        srednia = wynik / len(podaneLiczby)
        print("Aktualny wynik dodawania to:", wynik)
    else:
        print("Podano zero. Koniec!")
        break
print("Całkowity wynik dodawania to:", wynik)
print("Wartość najmniejszej z podanych liczb to:", min(podaneLiczby),".")
print("Wartość najwięjszej z podanych liczb to:", max(podaneLiczby), ".")
print("Średnia arytmetyczna podanych liczb to:", srednia, ".")

"""
najwyzsza = int()
najnizsza = 400000000000000000000

for i in podaneLiczby:
    if i > najwyzsza:
        najwyzsza = i
    if i < najnizsza:
        najnizsza = i
print(podaneLiczby)
print(najnizsza)
print(najwyzsza)
"""