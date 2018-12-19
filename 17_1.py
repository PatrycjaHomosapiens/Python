"""
Samochód na 100 km spala 8 l paliwa. Ile spali paliwa po przejechaniu 382 km?
"""

spalanie = 8
trasa = 100
droga = 382

ile_spali = (spalanie/trasa) * droga

print(round(ile_spali, 2))
print("Samochód, ktory spala " + str(spalanie) + " litrów na " + str(trasa) + " km, spala średnio " + str(ile_spali) + " na dystansie " + str(droga) + " km.")