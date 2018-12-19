# napisz program ktory wypelni liste liczbami od 1 do 10, a nastepnie wyswietli co trzeci element tablicy

"""
lista = [1,2,3,4,5,6,7,8,9,10]

for x in lista:
    if (x % 3 == 0):
        print(x)
"""

"""
for x in range(1, 10):
    if (x % 3 == 0):
        print(x)
"""


lista = []
for x in range(1, 11):
    lista.append(x)

print(lista)

for x in range(0, 10, 3):
    print(x)   #
    print(lista[x])   # odwolujac sie do listy przypisuje do indeksow wartosci; petla jest niezalezna od listy
  # dla for to jest liczba, dla print(lista[x]) to jest indeks
  # list to taki magazyn danych



#for x in range(100)
 #   print(x)