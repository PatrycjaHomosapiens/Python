"""
Program, który oblicy pole trojkata, pod warunkiem ze uzytkownik poda wysokosc i dlugosz podstawy tego trojkata.
Uwzglednij, ze wysokosc i dlugosc podstawy moga byc liczbami niecalkowitymi.
"""


podstawa = float(input("Podaj podstawę trójkąta: "))   # zamiana na float może być również później (w obl. pola trójkąta), ale dobrą praktyka jest dawanie tego juz tutaj
wysokosc = float(input("Podaj wysokość trójkąta: "))

pole_trojkata = 0.5 * podstawa * wysokosc

print("Pole trójkąta wynosi: " + str(pole_trojkata) + ".")
