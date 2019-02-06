# Zadanie 86_2

import json

try:
    f = open("86_1.json", "r")
    f.close()
except:
    kontakty = {}
    f = open("86_1.json", "w")
    json.dump(kontakty, f)
    f.close()


while(True):

    dec = input("D - dodaj, P - pokaż, U - usuń, Q - koniec: ").upper()

    f = open("86_1.json", "r")
    kontakty = json.load(f)
    f.close()


    if dec == "D":
        imieNazwisko = input("Podaj imię i nazwisko: ")
        telefon = input("Podaj telefon: ")

        znaleziono = False
        for v in kontakty:      # v to klucz, czyli imie i nazwisko
            if v == imieNazwisko:
                znaleziono = True
                break
        if znaleziono == True:
            kontakty[imieNazwisko].append(telefon)
        else:
            kontakty[imieNazwisko] = [telefon]

    elif dec == "P":
        for v in kontakty:
            print(v)
            for value in kontakty[v]:
                print("tel.: "+str(value))

    elif dec == "U":
        nazwisko = input("Podaj imię i nazwisko do usunięcia: ")
        tel = input("Podaj telefon do usunięcia: ")
        if tel == "":
            del kontakty[nazwisko]
        else:
            kontakty[nazwisko].remove(tel)

    elif dec == "Q":
        break

    f = open("86_1.json", "w")
    json.dump(kontakty, f)
    f.close()