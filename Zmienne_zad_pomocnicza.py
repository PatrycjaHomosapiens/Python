"""
Utwórz 5 zmiennych (zm1, zm2...). Przypisz zmienne do zmiennych tak, by otrzymać zdanie "Programowanie jest ciekawe i wciagajace".
Być może potrzebna będzie dodatkowa zmienna pomocnicza
"""

zm1 = "Ciekawe"
zm2 = "Programowanie"
zm3 = "Jest"
zm4 = "Wciągające"
zm5 = "I"

pomocnicza = zm1
zm1 = zm2
zm2 = pomocnicza

pomocnicza = zm2
zm2 = zm3
zm3 = pomocnicza

pomocnicza = zm4
zm4 = zm5
zm5 = pomocnicza

print(zm1, zm2, zm3, zm4, zm5)
