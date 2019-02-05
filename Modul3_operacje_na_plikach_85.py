# Zadanie 85:

def dodaj():
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    grupa = input("Podaj grupę: ")

    plik = open("85.txt", "a")
    # plik.write("%s, %s, %s\n" % (imie, nazwisko, grupa))    # 1 sposób
    plik.write(imie+","+nazwisko+","+grupa+"\n")                 # 2 sposob, można jeszcze 3 sposób  f-stringiem
    plik.close()

def pokaz():
    plik = open("85.txt", "r")
    for wiersz in plik:
        lista = wiersz.strip().split(",")       # strip usuwa enter, split rozdziela elementy przez ","
        print("Imie: "+lista[0]+" nazwisko: "+lista[1]+" grupa: "+lista[2]) # odwolanie do elementów wiersza
        # print(lista)
        # print(wiersz, end="")
    plik.close()

def usun():
    nazwisko = input("Podaj nazwisko do usunięcia: ")
    plik = open("85.txt", "r")
    zm = ""                         # zmienna pomocnicza
    for wiersz in plik:
        lista = wiersz.strip().split(",")
        if lista[1] != nazwisko:    #
            zm += wiersz
    plik.close()

    plik = open("85.txt", "w")
    plik.write(zm)
    plik.close()

def zmien():
    nazwisko = input("Podaj nazwisko do zmiany: ")
    imieN = input("Podaj nowe imie: ")
    nazwiskoN = input("Podaj nowe nazwisko: ")
    grupaN = input("Podaj nową grupę: ")
    plik = open("85.txt", "r")
    zm = ""
    for wiersz in plik:
        lista = wiersz.strip().split(",")
        if lista[1] == nazwisko:

             if imieN != "":
                lista[0] = imieN

             if nazwiskoN != "":
                lista[1] = nazwiskoN

             if grupaN != "":
                lista[2] = grupaN

        zm += lista[0] + "," + lista[1] + "," + lista[2] + "\n" # to można by zamknąć całe w nawias, traktujemy to jako
                        # 1 wiersz, czyli wykonuje się tyle razy, ile wierszy mamy w pliku, do którego się odwolujemy

    plik.close()

    plik = open("85.txt", "w")
    plik.write(zm)
    plik.close()

def szukaj():
    szukaj = input("Podaj szukaną daną: ")
    plik = open("85.txt", "r")
    for wiersz in plik:
        lista = wiersz.strip().split(",")
        if (lista[0].find(szukaj) > -1 or lista[1].find(szukaj) > -1): # -1, bo gdy find nie znajdzie, to daje wynik -1
            print(wiersz, end="")

    plik.close()


while (True):
    dec = input("D-dodaj, U-usun, P-pokaz, S-szukaj, Z-zmien, Q-koniec: ").upper()
    if (dec == "D"):
        dodaj()
    elif (dec == "P"):
        pokaz()
    elif (dec == "U"):
        usun()
    elif (dec == "Z"):
        zmien()
    elif (dec == "S"):
        szukaj()
    elif (dec == "Q"):
        pass

