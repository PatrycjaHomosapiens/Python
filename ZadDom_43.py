"""
Cwiczenie 43 (zadanie domowe z pierwszego modułu kursu Python):
Instrukcje warunkowe
Napisz program, który oblicza wartość współczynnika BMI wg wzoru (waga / wzrost^2).
Wzrost podawany jest w metrach.
Jeżeli wynik jest w przedziale (18.5 – 24.9) to wypisuje „waga prawidłowa”, jeżeli poniżej to „niedowaga”, jeżeli powyżej to „nadwaga”.
"""

waga = float(input("Podaj swoją wagę (w kg): "))
wzrost = float(input("Podaj swój wzrost (w metrach): "))

BMI = (waga / wzrost ** 2)

if BMI > 18.5 and BMI < 24.9:
    print("Waga prawidłowa, BMI wynosi:", round(BMI, 1))
elif BMI <=18.5:
    print("Niedowaga, BMI wynosi:", round(BMI, 1))
else:
    print("Nadwaga, BMI wynosi:", round(BMI, 1))