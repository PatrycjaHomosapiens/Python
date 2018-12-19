"""
program ktory wczyta od uzytkowanika dowolny tekst
program ma za zadanie wypisac:
- ile wprowadzono znakow w wprowadzonych tekscie,
- ile jest spacji we wprowadzonym tekscie
"""

tekst = input("Podaj dowolny tekst: ")
ilosc_znakow = len(tekst)
znak2 = tekst.replace(" ", "")
ilosc_znakow2 = len(znak2)

print(tekst)
print(znak2)

print("W tekście jest " + str(ilosc_znakow) + " znaków.")
print("W tekście jest " + str(ilosc_znakow - ilosc_znakow2) + " spacji.")

""" nieudana proba:
ilosc_spacji = (tekst.count(" "))   # zlicza spacje
print("W podanym tekście jest: " + str(ilosc_znakow) + " sztuk znaków.")
print("W podanym tekście jest: " + str(ilosc_spacji) + " sztuk spacji.")
print(tekst.replace(" ", ""))   # zamienia znaki
print(tekst.count("0"))   # zlicza podane znaki
print(ilosc_spacji)
"""
