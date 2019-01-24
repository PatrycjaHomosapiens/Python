# dochodzi do 5 i się wykrzacza
"""lista = [1,2,3,4,5,6,7,8,9]

for i in range(len(lista)):
    print(i)
    del(lista[i])

print(lista)
"""

# usuń element, taki zapis usuwa co drugi element listy
lista = [1,2,3,4,5,6,7,8,9]

for i in range(len(lista)):
    print(i)
    try:
        del(lista[i])
    except:
        break

print(lista)

# usuń element, ale od końca
lista = [1,2,3,4,5,6,7,8,9]

for i in range(len(lista)-1,0,1):
    print(i)
    try:
        del(lista[i])
    except:
        break

print(lista)


# kasowanie listy od końca
lista = [1,2,3,4,5,6,7,8,9]

for i in range(len(lista)-1,-1,-1):  # pierwsze -1 od czego zaczyna, drugie -1 to pierwszy element poza zakresem, trzecie to poza zakresem
    print(i)
    try:
        del(lista[i])
    except:
        break

print(lista)