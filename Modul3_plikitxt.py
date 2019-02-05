# ODCZYTYWANIE zawartości pliku tekstowego "tekst.txt" utworzonego w tym samym katalogu

# odczytywanie linijka po linijce
# dane = open("tekst.txt", "r")   # musimy mieć utworzony wcześniej plik "tekst.txt"
# print(dane.readline(), end="")  # odczytywanie wiersza po wierszu
# print(dane.readline(), end="")  # end="" usuwa 1 enter
# print(dane.readline(), end="")
# print(dane.readline(), end="")
# dane.close()

# wersja krótsza - wszystkie linijki (całość pliku)
# dane = open("tekst.txt", "r")
# lines = dane.readlines()
# print(lines)
# for line in lines:
#     print(line, end="")

# wersja najkrótsza - wszystkie linijki (całość pliku)
dane = open("tekst.txt", "r")
for line in dane:
    print(line, end="")
# dane.close()
