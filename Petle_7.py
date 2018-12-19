# liczby 0-100, podaj ich srednią


# tutaj print jest w środku pętli, więc podaje osobne sumy (wiele wyników)
"""
suma = 0
for x in range(1, 101):
    suma = suma + x
    print(suma)
    #print("Krok", x, "Suma", suma, "Średnia", suma/x)
"""

# tutaj print jest poza pętlą, więc podaje sumę całkowitą (jeden wynik)
suma = 0
for x in range(1, 101):
    suma = suma + x
print(suma)