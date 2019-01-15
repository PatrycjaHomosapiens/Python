"""
Posiadamy 2 drukarki czarnobiale i kolorowa, kolora drukuje 2 kartki na 5 minut, czarnobiala 8 kartek na 2 minuty.
Mamy 45 minut czasu na druki. Ile wydrukujemy w sumie kartek w kolorze i czarnobieli.
Wynik to 18 kolorowych i 180 czarnobiałych (razem 198 kartek)
"""

# 1 sposób zapisu:

czarno_biala = 2/5
kolorowa = 8/2
czas = 45

print(czarno_biala*czas + kolorowa*czas)


# 2 sposób zapisu:

kolorowa = 45 / (5/2)
czarnoBiala = 45 / (2/8)

print(czarnoBiala)
print(kolorowa)
print(czarnoBiala + kolorowa)
