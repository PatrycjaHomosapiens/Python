"""
SLOWNIKI, stosujemy nawiasy klamrowe {}
"""

# utworzenie słownika
magazyn = {"chleb":10, "mleko":3, "masło":5, "szynka":8}
print(magazyn)

# dodanie elementu
magazyn["pomidor"] = 11
print(magazyn)
magazyn["banany"] = 500
print(magazyn)
magazyn["banany"] = 1500
print(magazyn)

# usuwanie elementu
del magazyn["banany"]
print(magazyn)

# pusty słownik, do którego dodajemy
z = {}
z["vvv"] = 200
print(z)


"""
Napisz progrma ktory zmieni podana przez uzytkowanika liczbe zapisana slownie na wartosc (z zakresu od 1 do 5) 
na odpowiadajaca jej liczbe dziesietną
"""

lista1 = {"jeden":1, "dwa":2, "trzy":3, "cztery":4, "pięć":5}
liczba1 = input("Podaj słownie liczbę [1-5]: ")
print(lista1[liczba1])

"""
coś nie dziala
lista2 = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"pięć"}
liczba2 = input("Podaj NIEsłownie liczbę [1-5]: ")
print(lista2[liczba2])
"""