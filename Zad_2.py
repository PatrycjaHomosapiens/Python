# Napisz funkcje, która dostanie jako parametr napis i liczbę
# jako wynik zwróci zbiór znaków, które występują w napisie
# więcej niż <liczba> razy
# przykład:
# więcej_niz_('ala ma kota, a kot ma ale', 2)
# >>> {'a', ' '}

"""
najpierw piszemy test, później zmieniamy funkcję jesli coś nie wyszło
Najpierw było tak:
def wiecej_niz(dane_wejsciowe, liczba):
    if not dane_wejsciowe or liczba<0: # jeśli nie ma danych wejściowych, to wychodzimy
        return

    return {'a', ' '}
"""

# rozwiązanie zadania
def wiecej_niz(dane_wejsciowe, liczba):
   if  not dane_wejsciowe or liczba<0:
       return

   wynik = set()
   for znak in dane_wejsciowe:
       if dane_wejsciowe.count(znak)>liczba:
               wynik.add(znak)
   return wynik

# testy sparwdzające czy zadanie jest poprawnie wykonane
def test_dlugi_napis():
    dane_wejsciowe = 'ala ma kota, a kot ma ale'
    wynik = wiecej_niz(dane_wejsciowe, 2)
    assert {'a', ' '} == wynik

def test_pusty_napis():
    assert None == wiecej_niz('', 3)            # funkcja wiecej_niz nie zwrocila wyniku, wynikiem będzie None

# liczba wystapien jest wiecej niz 10, czyli litera musialaby wystapic wiecej niz 10 razy
# spodziewam się pustego zbioru
def test_liczba_duza():
    assert set() == wiecej_niz('ala ma kota', 10)   # pusty słownik to {}, pusty zbiór to set()

def test_liczba_ujemna():
    assert None == wiecej_niz('ala ma kota', -10)    # jesli liczba będzie ujemna, to wynikiem bedzie pusty zbiór
                                                   # zamiasta None wcześniej było set()
def test_liczba_zero():
    assert {'a', 'l', ' ', 'm', 'k', 'o', 't'} == wiecej_niz('ala ma kota', 0)