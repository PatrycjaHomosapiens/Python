"""
Cwiczenie 21 (zadanie domowe z pierwszego modułu kursu Python):
Operatory
Napisz prosty algorytm, który policzy nam odległości dróg, wiedząc że:
A -> B = 100km
B -> C = 80km
C -> D = 25km
Oblicz odległość:
A -> D
B -> D
C -> A
"""

ab = 100
bc = 80
cd = 25

ad = ab + bc + cd
bd = bc + cd
ca = ab + bc

print("Odległość A -> D wynosi:", ad, " km.")
print("Odległość B -> C wynosi:", bd, " km.")
print("Odległość C -> D wynosi:", ca, " km.")

"""
# wersja Borysa

ab=100
bc=80
cd=25
AD=ab+bc+cd
BD=bc+cd
CA=bc+ab
print('Odległoś A --> D = {}km.'.format(AD))
print('Odległoś B --> D = {}km.'.format(BD))
print('Odległoś C --> A = {}km.'.format(CA))
"""
