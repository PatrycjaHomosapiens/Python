# wyprodukuj listę liczb parzzystych

lista = []
for i in range(10):
    lista.append(i*2)

print(lista)


# inna wersja, wynik ten sam

lista = [i*2 for i in range(10)]
print(lista)

# bardziej skomplikowana lista, element nie musi byc prosty
# wyprodukuj liste tupli (i, i**2, i**3)

lista = [(i, i**2, i**3) for i in range(10)]
print(lista)

# wyrażenia listowe mogą wyprodukować coś innego niż lista, tutaj zrobić się generator
# generator to jest taki range, generator oddaje swoja zawartość w miarę potrzeb
# print(tuple(generator)) # to oddaje...
generator = ((i, i**2, i**3) for i in range(10))
print(generator)        # wynikiem jest: <generator object <genexpr> at 0x021CDC70>
print(generator.__next__())

zbior = {(i, i**2, i**3) for i in range(10)}
print(zbior)

slownik = {i:(i, i**2, i**3) for i in range(10)}
print(slownik)

# petla z warunkiem
lista = []
for i in range(10):
    if i % 2 == 0:
        lista.append(i)
print(lista)

lista = [i for i in range(10) if i % 2 == 0]
print(lista)


# zwroć co drugi znak z napisu
napis = 'ala ma kota a kot ma ale'

napis2 = [napis[i] for i, lit in enumerate(napis) if i % 2 == 0]     # lit to litera, enumerate wylicza litery
napis3 = [napis[i] for i in range(0, len(napis), 2)]                # inny sposób rozwiązania tego samego
napis4 = [napis[i] for i in range(len(napis)) if i % 2 == 0]        # jeszcze inny sposób

print(napis2)
print(napis3)
print(napis4)