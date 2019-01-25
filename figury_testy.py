# SPOSÓB 1:
from moduly.matematyka.geometria.figury \
    import pole_kwadratu, pole_trojkata

def test_kwadrat():
    assert 16 == pole_kwadratu(4)

def test_trojkat():
    assert 6 == pole_trojkata(3,4)


#  SPOSÓB 2:
# from moduly.matematyka.geometria import figury
# def test_kwadrat():
#     assert 16 == figury.pole_kwadratu(4)
#
# def test_trojkat():
#     assert 6 == figury.pole_trojkata(3,4)


# TAK NIE WOLNO:
# from moduly.matematyka import geometria.figury
# def test_kwadrat():
#     assert 16 == geometria.figury.pole_kwadratu(4)
#
# def test_trojkat():
#     assert 6 == geometria.figury.pole_trojkata(3,4)