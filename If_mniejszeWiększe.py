""" 
Wczytaj z klawiatury 3 wartosci i wypisz je po kolei od najwiekszego do najmniejszego. """

a = input("Wpisz liczbę nr 1: ")    # czy tu nie trzeba dać int?
b = input("Wpisz liczbę nr 2: ")
c = input("Wpisz liczbę nr 3: ")

if ((a > b) and (a > c)):
    if (b > c):
        print(a, b, c)
    else:
        print(a, c, b)
elif((b > a) and (b > c)):
    if (a > c):
        print(b, a, c)
    else:
        print(b, c, a)
elif ((c > a) and (c > b)):
    if (a > b):
        print(c, a, b)
    else:
        print(c, b, a)
