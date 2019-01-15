"""
program ktory wczyta od uzytkowanika dowolny tekst
program ma za zadanie wypisac:
- ile wprowadzono znakow w wprowadzonych tekscie,
- ile jest spacji we wprowadzonym tekscie
"""

# bez użycia tekst.count(" ")
tekst = input("Podaj dowolny tekst: ")
ilosc_znakow = len(tekst)
tekst2 = tekst.replace(" ", "")     # zamienia znaki, w tym przykładzie likwiduje spacje
ilosc_znakow2 = len(tekst2)
print(tekst)
print(len(tekst))
print(tekst2)
print(len(tekst2))

print("W tekście jest " + str(ilosc_znakow) + " znaków.")
print("W tekście jest " + str(ilosc_znakow - ilosc_znakow2) + " spacji.")

# z użyciem tekst.count(" ")
tekst = input("Podaj dowolny tekst: ")
ilosc_znakow = len(tekst)
ilosc_spacji = (tekst.count(" "))   # zlicza znaki, w tym przykładzie zlicza spacje
print("W podanym tekście jest: " + str(ilosc_znakow) + " sztuk znaków.")
print("W podanym tekście jest: " + str(ilosc_spacji) + " sztuk spacji.")
