"""
Utworz liste skladająca się z 5 artykulow spozywczych
wyswietla na ekranie jako tekst zawartosc pierszego i ostatniego elementu z listy (wykorzystaj 2 spowoby)
Uwzględnij przypadek, ze dlugosc listy moze ulec zmianie
"""

lista = ["chleb", "jabłko", "sok", "woda", "piwo"]

# wyświetlanie pierwszego, sposoby:
print(lista[0])
print(lista.pop(0))

# wyświetlanie ostatniego, sposoby:
print(lista[-1])   # nie podajemy nr kolejnego, tylko odnosimy sie do ostatniego, bo ilosc moze sie zmienic
print(lista[len(lista)-1])  # nie wiem, jak to działa, ale zwraca ostatni element z listy
print(len(lista))      # podaje ilość elementów w liście
print(lista.pop(-1))    # ostatni sposób usunął 1 i ostatni element po jego wyświetleniu, takze to tylko ciekawostka
print(lista)
lista.reverse()     # przestawia elementy [1,2,3,4] zamienia na [4,3,2,1]
print(lista)
