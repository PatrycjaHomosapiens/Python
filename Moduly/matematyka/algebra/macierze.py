# dodaj jest zrobione rekurencyjnie

def dodaj(macierz_a, macierz_b):
    if type(macierz_a) != list:
        return macierz_a + macierz_b

    wynik = []
    for i in range(len(macierz_a)):
        wynik.append(dodaj(macierz_a[i], macierz_b[i]))

    return wynik

def odejmij(macierz_a, macierz_b):
    if type(macierz_a) != list:
        return macierz_a - macierz_b

    wynik = []
    for i in range(len(macierz_a)):
        wynik.append(odejmij(macierz_a[i], macierz_b[i]))

    return wynik