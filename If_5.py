"""
Napisz program wczytujący 3 zmienne i sprawdzające czy z odcinków
o takich długościach da się zbudować trójkat prostokatny
a2 + b2 = c2
Na koncu ma wypisac informacje
"""

# trojkat prostokatny zrobi sie z danych 3, 4 i 5
# print(pow(2, 3))   - to jest 2 do potęgi 3

a = int(input("Wpisz bok a: "))
b = int(input("Wpisz bok b: "))
c = int(input("Wpisz bok c: "))

""" METODA z symbolem "**" potęgi
if(a**2 + b**2 == c ** 2):
    print("Z podanych liczb MOŻNA zbudować trójkąt prostokątny")
else:
    print("Z podanych liczb NIE można zbudować trójkąta prostokątnego")
"""

# metoda z potęgą zapisaną pow(a, 2)
if(pow(a,2) + pow(b, 2) == pow(c, 2)):
    print("Z podanych liczb MOŻNA zbudować trójkąt prostokątny")
else:
    print("Z podanych liczb NIE można zbudować trójkąta prostokątnego")