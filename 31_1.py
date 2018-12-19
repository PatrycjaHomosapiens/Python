"""
Utworz liste z 5 skladająca się z elementow artykulow spozywczych
wyswietla na ekranie jako tekst zawartosc pierszego i ostatniego elementu z listy (wykorzystaj 2 spowoby)
Uwzględnij przypadek, ze dlugosc listy moze ulec zmianie
"""

lista = ["chleb", "jabłko", "sok", "woda", "piwo"]

# wyświetlanie pierwszego, sposoby:
print(lista[0])
print(lista.pop(0))

# wyświetlanie ostatniego, sposoby:
print(lista[-1])   # nie podajemy nr kolejnego, tylko odnosimy sie do ostatniego, bo ilosc moze sie zmienic
print(lista[len(lista)-1])
lista.reverse()
print(lista.pop(-1))
print(lista)   # ostatni sposób usunął 1 i ostatni element po jego wyświetleniu, takze to tylko ciekawostka
