nazwa = "ALX"

print(nazwa[2])
print(len(nazwa))   # zlicza wszystkie znaki

print(nazwa.capitalize())   # zamienia pierwsza litera zawsze na WIELKA reszta małe
print(nazwa.count("X"))   # zlicza podane znaki
print(nazwa.replace("X", "V"))   # zamienia znaki, zastępuje stary podciąg nowym
print(nazwa.strip())   # usuwa początkowe i końcowe białe znaki
print(nazwa.isdigit())      # sprawdza, czy wszystkie znaki są cyframi, wynik to True/False
print(nazwa.islower())      # sprawdza, czy wszystkie litery są małe, wynik to True/False
print(nazwa.isupper())      # sprawdza, czy wszystkie litery są duże, wynik to True/False
