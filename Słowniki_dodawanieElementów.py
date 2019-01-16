"""
Podaj dwie liczby slownie, wynik ma byc liczbą. Zakres [1-5]. Następnie odwrotnie (wynik słownie)"""

slownik = {"jeden": 1, "dwa": 2, "trzy": 3, "cztery": 4, "pięć": 5}
liczba1 = input("Podaj słownie liczbę nr 1 z zakresu [1-5]: ")
liczba2 = input("Podaj słownie liczbę nr 2 z zakresu [1-5]: ")
print(slownik[liczba1] + slownik[liczba2])
# print(lista[liczba1 + liczba2])   taki zapis tutaj nie działa

slownik2 = {1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć"}   # to będzie działać, ale do sumy max "pięć", bo innych liczb nie zdefiniowaliśmy
liczba3 = int(input("Podaj NIEsłownie liczbę nr 1 z zakresu [1-5]: "))   # trzeba zamienić na intiger
liczba4 = int(input("Podaj NIEsłownie liczbę nr 2 z zakresu [1-5]: "))
print(slownik2[liczba3 + liczba4])  # tutaj trzeba dodać liczby w ramach jednego nawiasu []
print(slownik2[liczba3] + slownik2[liczba4])    # tutaj znak "+" będzie potraktowany jako konkatenacja
