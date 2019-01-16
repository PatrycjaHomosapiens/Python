lista = [0, 2, 4, 6, 8]
print(lista)
print(lista[0])   # wyświetla element o wybranym indeksie, tutaj indeks nr 0
print(lista[4])   # wyświetla element o wybranym indeksie, tutaj indeks nr 4
lista.append(10)   # dodaje zawsze jeden element zawsze na końcu
print(lista)
del lista[2]   # usuwa element o wybranym indeksie, tutaj o indeksie nr 2
print(lista)
lista.insert(2, 4)   # dodaje na konkretnej pozycji, tutaj na indeksie nr 2 (czyli pozycja 3-cia od lewej) doda 4
print(lista)
print(2 in lista)       # zwraca wartość logiczną True (jeśli podany element jest w liście) lub False (gdy nie ma)
print(lista.pop(1))     # zwraca i-ty element i usuwa go z listy, tutaj zwraca i usuwa cyfrę 2 (bo ma indeks 1)
                        # POP usuwa po indeksie, a REMOVE po wartości
print(lista)
# lista.extend()      # (??? jakiś błąd w zapisie) dodaje nową listę "t" na końcu "lista"
print(lista.count(10))  # zlicza wystąpienia 10 w liście
print(lista.index(6))   # zwraca najmniejszy indeks i, tutaj zwraca indeks 2, bo na tej pozycji jest cyfra 6
print(lista.remove(4))  # odnajduje x i usuwa go z listy, daje wynik "None" jeśli znajdzie i usunie dany element
                        # REMOVE usuwa po wartości, a POP po indekscie
print(lista)
lista.reverse()         # odwraca kolejność elementów, przestawia elementy [1,2,3,4] zamienia na [4,3,2,1]
print(lista)

kursy = [ ["Python", 15, "Katowice"], ["Java", 10, "Kraków"] ]   # 2 elementy, może być więcej elementów, ale zwykle są 2
# jak dostać się do informacji "Java"
print(kursy[1][0])
