"""
dane = (1,5,3,8)
print(dane)
dane[1] =   # nie da się modyfikowac krotki
print(dane[1])


dane = [1, 5, 3, 6]    # utworzenie listy
print(type(dane))      # sprawdzenie typu sekwencyjnego (lista, krotka...)
dane = tuple(dane)     # zamiana listy na krotkę (utworzenie krotki z listy)
print(type(dane))

dane = (1, 5, 3, 6)    # utworzenie krotki
print(type(dane))
dane = list(dane)      # zamiana krotki na listę (utworzenie listy z krotki)
print(type(dane))
"""

# najpierw tworzę krotkę z listy, później zmieniam wart. pierwszego indeksu w liście, dlatego krotka i lista są różne
dane = [1, 5, 3, 6]    # utworzenie listy
dane1 = tuple(dane)    # utworzenie krotki
dane[1] = "X"          # dodatnie elementu do listy
print(dane)
print(type(dane))
print(dane1)
print(type(dane1))

# najpierw zmieniam wart. pierwszego indeksu w liście, a później tworzę krotkę, dlatego krotka i lista są jednakowe
dane = [1, 5, 3, 6]
dane[1] = "X"
dane1 = tuple(dane)
print(dane)
print(dane1)

print(len(dane))
print(len(dane1))

"""
Napisz program, ktory tekst np. "Witaj na kursie Python"  przechowuje w postaci krotki slowo po slowu
Nastepnie wypisz na ekran calą zawartosc krotki
"""

tekst = ("Witaj", "na", "kursie", "Python")
print(tekst)
