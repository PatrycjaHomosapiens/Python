"""
posiadamy 2 drukarki czarnobiale i kolorowa, kolora drukuje 2 kartki na 5 minyt, czarnobiala 8 kartek na 2 minuty.
mamy 45 minut czasu na druki
ile wydrukujemy w sumie kartek w kolorze i czarnobieli
jaki jest wynik

wynik to 198
kolorowych 18
czarnobialych 180
"""

czarno_biala = 2/5
kolorowa = 8/2
czas = 45

print(czarno_biala*czas + kolorowa*czas)