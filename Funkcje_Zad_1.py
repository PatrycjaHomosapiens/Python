# robimy test w pytest; wczesniej musimy go zainstalować w terminalu, przez "(venv) C:\Users\kurs\Desktop\Projekty ALX>pip install pytest"

def czy_parzysta(dane_wejsciowe):
    return dane_wejsciowe % 2 == 0

# TDD (test driven development)
# GIVEN
# przygotowanie środowiska
# WHEN
# odpalenie funkcjonalności do przetestowania
# THEN
# sprawdzenie czy efekty są zgodne z oczekiwaniami

def test_sprawdz_nieparzysta():
    dane_wejsciowe = 9
    wynik = czy_parzysta(dane_wejsciowe)
    assert True == wynik    # assert sprawdza czy wynik jest zgodny z oczekiwaniami, po lewej stronie jest to co oczekujemy
                            # assert ma podobna funkcjonalność

def test_sprawdz_parzysta():
    dane_wejsciowe = 12
    wynik = czy_parzysta(dane_wejsciowe)
    assert True == wynik

# aby sprawdzić test dajemy kursor poza funkcję (na białej linijce) i klikamy "Run 'pytest' in Zad_1_testy"
# jeśli odpalam test stojąć w objębie jakiegoś kawałka, to odpalam ten kawałek, jest puste miejsce, to całość
# sprawdziliśmy test, to co
# test - ja mówie co ma się zdarzyć, a nie jak, np. potrzebuje wykopac rów i stwierdzam, że ma się zaczynać tu i kończyć tam, nieważne jak