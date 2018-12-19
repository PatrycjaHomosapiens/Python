"""
dane = (1,5,3,8)
print(dane)
dane[1] =   # nie da się modyfikowac krotki
print(dane[1])
"""

dane = [1,5,3,6]
dane = tuple(dane)
print(type(dane))   # sprawdzenie rodzaju

dane = (1,5,3,6)
dane = list(dane)
print(type(dane))   # sprawdzenie rodzaju

dane = [1,5,3,6]
dane1 = tuple(dane)
dane[1] = "X"
print(dane)
print(dane1)

dane = [1,5,3,6]
dane[1] = "X"
dane1 = tuple(dane)
print(dane)
print(dane1)


# len(krotka)







"""
Napisz program, ktory tekst np. "Witaj na kursie Python"  przechowuje w postaci krotki slowo po slowu
Nastepnie wypisz na ekran calą zawartosc krotki
"""

tekst = ("Witaj", "na", "kursie", "Python")
print(tekst)