"""
SLOWNIKI, stosujemy nawiasy klamrowe {}
"""

# utworzenie słownika
magazyn = {"chleb": 10, "mleko": 3, "masło": 5, "szynka": 8}
print(magazyn)

# dodanie elementu
magazyn["pomidor"] = 11
print(magazyn)
magazyn["banany"] = 500
print(magazyn)
magazyn["banany"] = 1500    # zamiana elementu, podmieniamy wartość dla danego klucza
print(magazyn)

# usuwanie elementu
del magazyn["banany"]
print(magazyn)

# pusty słownik, do którego dodajemy
z = {}
z["vvv"] = 200
print(z)

magazyn["kaki"] = 666
print(magazyn)
del magazyn["kaki"]
print(magazyn)
