"""
TYPY SEKWENCYJNE
Napisz program, ktory 5 razy poprosi o podanie imienia. Podane imiona beda zapisywane do listy.
Wypisz dla wszystkich imion ponizszy komunikat
Cześć <tutaj imię z listy>
"""

imiona = []   # pusta lista

im1 = input("Wpisz imię nr 1: ")
imiona.append(im1)

im2 = input("Wpisz imię nr 2: ")
imiona.append(im2)


im3 = input("Wpisz imię nr 3: ")
imiona.append(im3)

im4 = input("Wpisz imię nr 4: ")
imiona.append(im4)

im5 = input("Wpisz imię nr 5: ")
imiona.append(im5)

print("Cześć " + imiona[0] + "! Miło mi Cię poznać :)")   # odwołujemy się do listy, dlatego używamy imiona[0] a nie im1
print("Cześć " + imiona[1] + "! Miło mi Cię poznać :)")
print("Cześć " + imiona[2] + "! Miło mi Cię poznać :)")
print("Cześć " + imiona[3] + "! Miło mi Cię poznać :)")
print("Cześć " + imiona[4] + "! Miło mi Cię poznać :)")

print(imiona)
