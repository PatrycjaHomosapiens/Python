from collections import defaultdict

slownik = defaultdict(int)    # po wpisaniu defaultdict() podkreśli się na czerwono, wtedy robimy
                              # lewy Alt+Enter i na samej górze pojawi się "from collections import defaultdict
print(slownik)
print(slownik['ala'])
print(slownik)
slownik['kot'] += 100
print(slownik)


slownik_znakow = defaultdict(str)
print(fr'#{slownik_znakow["ala"]}#')        # to jest pusty napis (pusty string), bo "ala" jest kluczem, pod którym
                                            # nie ma wartosci, więc zeby było widać, że nic nie ma opakowaliśmy to ##

# wartość domyślna inna niż 0
slownik = defaultdict(int)

def tralala():
    return 5
zmienna = tralala       # tralala bez nawiasów to obiekt, tralala() to
print('obiekt:', zmienna)
print('wywołanie:', zmienna())     # tutaj jest z () i to wywołuje return

slownik = defaultdict(tralala)
print(slownik)
print(slownik['ola'])


# lambda wyrażenie
# pomysł na krótkie zapisanie funkcji, która ma 1 linijkę
# tzn. tylko instrukcję return i nic wiecej

zmienna = lambda x,y,z: x+y+z
print(zmienna(2,3,4))

"""
teraz robimy przez lambda wyrażenie coś takiego jak wyżej:
def tralala():
    return 5
"""
# lambda z 0 parametrami, zwraca 5
tralala = lambda : 5
print(tralala())        # zwraca 5, chociaż nie podaję żadnych parametrów


# slownik z wartoscia domyslna 5
slownik = defaultdict(lambda : 5)       # slownik miał wart domyslna 5, ale nie mial klucza
print(slownik)
print(slownik['ala'])                   # teraz dopisalismy klucz
print(slownik)


