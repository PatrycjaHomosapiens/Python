"""
Cwiczenie 55 (zadanie domowe z pierwszego modułu kursu Python):
Pętle
Wyświetl kwadraty liczb od 3 do 9.
"""


i = 3

while i < 10:
    wynik = i ** 2
    print(wynik)   # może być również na końcu, po "i =+ 1"
    i += 1

"""
# wersja Borysa

for i in range (3,10):
    print(pow(i,2))
"""