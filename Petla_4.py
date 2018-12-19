lista = [1,2,3,4,5,6,7,8,9,10]

# wypisuje liczby parzyste, wynik: 2,4,6,8,10
for element in lista:
    if (element % 2 == 0):
        print(element)

# wypisuje liczby parzyste, wynik: 1,3,5,7,9
for element in lista:
    if (element % 2 != 0):
        print(element)