
#  wyprodukuj liste liczb parzystych

lista = []
for i in range(10):
    lista.append(i*2)

print(lista)

lista = [i*2 for i in range(10)]
print(lista)


# wyprodukuj liste tupli (i, i**2, i**3)
lista = [(i,i**2,i**3) for i in range(10)]
print(lista)

generator = ((i,i**2,i**3) for i in range(10))
print(generator.__next__())

zbior = {(i,i**2,i**3) for i in range(10)}
print(zbior)

slownik = {i:(i,i**2,i**3) for i in range(10)}
print(slownik)

# petla z warunkiem
lista = []
for i in range(10):
    if i % 2 == 0:
        lista.append(i)
print(lista)

lista = [i for i in range(10) if i % 2 == 0 ]
print(lista)