lista1 = [2, 8, 11, 66, 99]
lista2 = lista1   # przypisanie zmiennej do zmiennej
print(lista1)     # lista1 i lista2 to obecnie to samo
print(lista2)

lista1[0] = 123
print(lista1)     # lista1 i lista2 to nadal to samo, tylko powiększone o element 123 na indeksie 0
print(lista2)
