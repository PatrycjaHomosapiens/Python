""" Utwórz zmienne a, b, c, d, e, które posiadają odpowiednio wartości: 1, 2, 3, 4, 5.
Wykonaj różne działania matematyczne"""

a = 1
b = 2
c = 3
d = 4
e = 5

a = a * e         # zmienną "a" zwiększ o "e" razy
d = d - b         # zmienną "d" zmniejsz o "b"
c = c * a         # zmienną "c" zwiększ o "a" razy
a = (b + d + e) / 3         # zmienna "a" jest to suma "b", "d" i "e" podzielona przez 3
c = c / a         # zmienną "c" zmniejsz o "a" razy
b = b + b         # zmienną "b" powiększ o wartość samej siebie

a = a + a + c           # zmienną "a" zwiększ o wartość samej siebie i "c"
e = b * c * a           # zminna "e" jest iloczynem "b", "c" i "a"          
d = (a * b) + (c * e)   # zmienna "d" jest sumą iloczynów "a" i "b" oraz "c" i "e"
c = c - (a + e)         # zmienna "c" jest różnicą samej siebie i sumy "a" i "e" 
b = 3 * b               # zmienna "b" jest 3 razy większa niż dotychczas
d = b                   # zmienna "d" jest równa "b"
wynik = a + b + c + d + e   # zmienna "wynik" to suma "a", "b", "c", "d" i "e"

print(wynik)
