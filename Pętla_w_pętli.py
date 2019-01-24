"""
tablica = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]               # lista w liście

for el in tablica:
    print(el)



# aby chodzić po tablicy robimy tak:

for wiersz in tablica:
    for el in wiersz:
        print(el)
"""

# sumowanie elementów tablicy

tablica = [
    [1,2,3,4,5],
    [4,5,6,7,8],
    [7,8,9,10,11]
]

suma = 0
for wiersz in tablica:
    for el in wiersz:
        suma += el
print(suma)


print(wiersz)   # wiersz nie jest dostępny poza listą, wiec się nie wyświetli


#zwykla_lista = [1,2,3,4]
#for wiersz in zwykla_lista:
#    for el in wiersz:  # wyświetli się kod "1", dostajemy
#        print(el)

# przzechodzenie po pierwszym wiersu
for el in tablica[0]:
    print(f"pierwszy wiersz {el}")  # musi być "f' przed stingiem, aby nie wyśweitlio się literalnie, tylko jako obliczenie

#zwykla_lista = [1,2,3,4]
#for wiersz in zwykla_lista:
#    for el in wiersz:   # tu jest problem, bo elementami lilsty są int-y
#        print(el)


tablica3d = [[      # można robić tablice wielowymiarowe, mogą być różnych rozmiarów
    [1,2,3,4,5],
    [4,5,6,7,8],
    [7,8,9,10,11]
],
[
    [101,102,103,104,105],
    [104,105,106,107,108],
    [107,108,109,110,111]
],
[
    [1,2,3,4,5],
    [4,5,6,7,8],
    [7,8,9,10,11]
]]

suma = 0
for plaster in tablica3d:
    for wiersz in plaster:
        for el in wiersz:
            suma += el
print(suma)

# print(sum(tablica3d))  - nie wiem co to, coś nie wyszło

