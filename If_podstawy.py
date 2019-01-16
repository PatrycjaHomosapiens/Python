if (2 > 5):
    print("OK")
print("OK2")   # to nie jest częścią if
print("OK3")   # to nie jest częścią if

if (2 > 5):
    print("OK")   # to jest częścią if
    print("OK2")    # to jest częścią if
    print("OK3")    # to jest częścią if

# if ((2>5) and ()):   stosujemy nawiasy

if (2 > 5):
    print("OK")
else:
    print("OK2")
    print("OK3")
    print("OK4")

zmienna = input("Podaj cyfrę: ")
zmienna = int(zmienna)

if (zmienna > 10):
    print("Wpisałeś cyfrę większą niż dziesięć")
else:
    print("Wpisałeś cyfrę mniejszą niż dziesięć")
print("Koniec programu")


if (zmienna > 0):
    print("Wpisałeś cyfrę dodatnią")
elif (zmienna == 0):
    print("Wpisałeś zero")
else:
    print("Wpisałeś cyfrę ujemną")
print("Koniec programu")


if (zmienna > 0):
    print("Wpisałeś cyfrę dodatnią")
    if (zmienna % 2 == 0):
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")
elif (zmienna == 0):
    print("Wpisałeś zero")
else:
    print("Wpisałeś cyfrę ujemną")
print("Koniec programu")


