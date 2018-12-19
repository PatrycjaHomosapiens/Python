lista = [0, 2, 4, 6, 8]
print(lista)
print(lista[0])   # wyświetla element o wybranym indeksie, tutaj indeks nr 0
print(lista[4])   # wyświetla element o wybranym indeksie, tutaj indeks nr 4
lista.append(10)   # dodaje zawsze jeden element zawsze na końcu
print(lista)
del lista[2]   # usuwa
print(lista)
lista.insert(2, 4)   # dodaje na konkretnej pozycji
print(lista)
print(2 in lista)
lista.pop(1)
print(lista)

kursy = [ ["Python", 15, "Katowice"], ["Java", 10, "Kraków"] ]   # 2 elementy, może być więcej elementów, ale zwykle są 2
# jak dostać się do informacji "Java"

print(kursy[1][0])
