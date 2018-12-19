"""# zwraca liczby
liczby = [-2, -1, 0, 1, 2]
for x in liczby:
    if x < 0:
        continue
    print(x)
"""

# Wypisz liczby od 0 do 10 bez 5
for x in range(11):
    if x == 5:
        continue
    print(x)


# Wypisz liczby od 0 do 10 parzyste - rozwiązanie z continue
for x in range(11):
    if x % 2 != 0:
        continue
    print(x)

# Wypisz liczby od 0 do 10 parzyste - rozwiązanie BEZ continue
for x in range(11):
    if x % 2 == 0:
        print(x)