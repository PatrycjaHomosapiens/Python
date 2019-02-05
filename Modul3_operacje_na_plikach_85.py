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


while (True):
    dec = input("D-dodaj, U-usun, P-pokaz, S-szukaj, Z-zmien, Q-koniec: ").upper()
    if (dec == "D"):
        dodaj();
    elif (dec == "P"):
        pokaz()
    elif (dec == "U"):
        usun()

