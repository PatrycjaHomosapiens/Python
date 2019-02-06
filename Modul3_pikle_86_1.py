# Zadanie 86_1

import pickle

try:
    f = open("86_1.dat", "rb")
    f.close()
except:
    kontakty = {}
    f = open("86_1.dat", "wb")
    pickle.dump(kontakty, f)
    f.close()


while(True):

    dec = input("D - dodaj, P - pokaż, U - usuń, Q - koniec: ").upper()

    f = open("86_1.dat", "rb")
    kontakty = pickle.load(f)
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

# Sposób z usuwaniem, gdu na poczatku program pyta, co chcemy usunąć - moje, nie działa
        # doUsuniecia = input("UK - usuń cały kontakt, UT - usuń tylko telefon: ").upper()
        # znaleziono2 = False
        # # for v in kontakty:
        # #     if v != imieNazwisko or v != telefon:
        # #         znaleziono2 = False
        # #         break
        # if znaleziono2 == True and doUsuniecia == "UK":
        #     kontaktDoUsuniecia = input("Podaj imię i nazwisko do usunięcia: ").upper()
        #     del kontakty[kontaktDoUsuniecia]
        # elif znaleziono2 == True and doUsuniecia == "UT":
        #     osobaDoUsuniecia = input("Podaj imię i nazwisko, dla którego chcesz usunąć telefon: ").upper()
        #     telefonDoUsuniecia = input("Podaj telefon, który chcesz usunąć: ").upper()
        #     del kontakty[telefonDoUsuniecia]

    elif dec == "Q":
        break

    f = open("86_1.dat", "wb")
    pickle.dump(kontakty, f)
    f.close()