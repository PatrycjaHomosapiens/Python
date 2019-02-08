from moduly.matematyka.algebra.macierze import dodaj, odejmij



def test_dodaj():
    assert 15 == dodaj(7,8)

def test_odejmij():
    assert 3 == odejmij(6,3)