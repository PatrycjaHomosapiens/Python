"""
podaj dwie liczby slownie, wynik ma byc liczbą
zakres [1-5]
i odwrotnie
"""


lista = {"jeden":1, "dwa":2, "trzy":3, "cztery":4, "pięć":5}
liczba1 = input("Podaj słownie liczbę pierwszą z zakresu [1-5]: ")
liczba2 = input("Podaj słownie liczbę drugą z zakresu [1-5]: ")
print(lista[liczba1] + lista[liczba2])
# print(lista[liczba1 + liczba2])   taki zapis tutaj nie działa


lista2 = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"pięć"}   # to będzie działać, ale do sumy max "pięć", bo innych liczb nie zdefiniowaliśmy
liczba3 = int(input("Podaj NIEsłownie liczbę pierwszą z zakresu [1-5]: "))   # trzeba zamienić na intiger
liczba4 = int(input("Podaj NIEsłownie liczbę drugą z zakresu [1-5]: "))
print(lista2[liczba3 + liczba4])


