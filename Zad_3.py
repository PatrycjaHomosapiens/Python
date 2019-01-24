#Zadanie #3
# Napisz funkcję obliczającą liczbę znaków w zadanym napisie
# pomiędzy zadanymi znakami.
# Znaki, pomiędzy którymi ma odbywać się zliczanie,
# powinny być argumentami z wartościami domyślnymi odpowiednio < i >.
# Nawiasy mogą być zagnieżdżone i mogą wystąpić wiele razy.
# Znaki pomiędzy zagnieżdżonymi nawiasami liczone są
# zgodnie z poziomem zagnieżdżenia.
#
# Przykład użycia:
# >>> policz_znaki('ala ma <kota> a kot ma ale')
# 4
# >>> policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']')
# 18
# >>> policz_znaki('a <a<a<a>>>')
# 6
import pytest

"""
def policz_znaki(napis):
    gdzie_nawias_lewy = napis.find("<")   # wcześniej było "gdzie_nawias_lewy = napis.find("<")", ale find nie wyrzuca informacji o tym, gdzie mamy blad
    gdzie_nawias_prawy = napis.find(">")

    print(gdzie_nawias_lewy, gdzie_nawias_prawy)
    return gdzie_nawias_prawy - gdzie_nawias_lewy -1  # jeśli nie znaleziono w teście, to trzeba jeszcze dać -1
"""


def policz_znaki(napis, lewy_nawias='<', prawy_nawias='>'):
    gdzie_nawias_lewy = napis.find(lewy_nawias)
    gdzie_nawias_prawy = napis.find(prawy_nawias)

    if gdzie_nawias_lewy == -1 and gdzie_nawias_prawy == -1:
        return 0

    if gdzie_nawias_lewy == -1 or gdzie_nawias_prawy == -1:
        return None

    if gdzie_nawias_prawy - gdzie_nawias_lewy < 0:
        return None

    return gdzie_nawias_prawy - gdzie_nawias_lewy -1

def test_pojedynczy_nawias():
    assert 4 == policz_znaki('ala ma <kota> a kot ma ale')

def test_pusto_pomiedzy_nawiasami():
    assert 0 == policz_znaki('tralala <> tralala')# # sposób na sprawdzenie czy kawałek kodu rzuca błąd

# def test_pojedynczy_nawias():
#     assert 4 == policz_znaki('ala ma <kota> a kot ma ale')      # algoryt 'ala ma <kota> a kot ma ale' ma zwrócić 4
#
# def test_pusto_pomiedzy_nawiasami():
#     assert 0 == policz_znaki("tralala <> tralala")

# sposob na sprawdzenie czy kawałek kodu rzuca błąd
# CHCEMY ŻEBY RZUCIŁ BŁĄD
# def test_brakuje_nawiasu():
#     with pytest.raises(ValueError):
#         policz_znaki("dkasuhgliuacvrtuie")    # nie znalazł.......

def test_bez_nawiasow():
    assert 0 == policz_znaki("dkfadfjlkdfldskf")

def test_nawiasy_w_zlej_kolejnosci():
    assert None == policz_znaki("dkfadf>j<lkdfldskf")

def test_inne_nawiasy():
    assert 4 == policz_znaki('ala ma [kota] a kot ma ale','[',']')

