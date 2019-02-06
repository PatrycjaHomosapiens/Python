# Zadanie 75:

from tkinter import *

root = Tk()
root.title("Książka telefoniczna")
root.geometry("700x300")

kontakty = []

def dodajKotakt():
    imie = entry_Imie.get()
    nazwisko = entry_Nazwisko.get()
    telefon = entry_Telefon.get()
    email = entry_Email.get()

    dane = [imie, nazwisko, telefon, email]
    kontakty.append(dane)
    listaKontaktow()

    wyczyscEntry()
    entry_Imie.focus()      # kursor ma powrócić do pola imie

def wyczyscEntry():
    entry_Imie.delete(0, END)
    entry_Nazwisko.delete(0, END)
    entry_Telefon.delete(0, END)
    entry_Email.delete(0, END)

def listaKontaktow():
    listbox_ListaKontaktow.delete(0, END)
    for index, value in enumerate(kontakty):     # index, value to wew. tablica
        listbox_ListaKontaktow.insert(index, value[0]+" "+value[1])     # doda się tylko imię[0] i nazwisko[1]

def pokazSzczegoly():
    index = listbox_ListaKontaktow.index(ACTIVE)     # pobiera index aktywnej wartości, czyli tego, co jest zaznaczone
    label_ImieBottomValue["text"] = kontakty[index][0]
    label_NazwiskoBottomValue["text"] = kontakty[index][1]
    label_TelefonBottomValue["text"] = kontakty[index][2]
    label_EmailBottomValue["text"] = kontakty[index][3]

def usunKontakt():
    index = listbox_ListaKontaktow.index(ACTIVE)
    kontakty.pop(index)
    listaKontaktow()        # po usunięciu wywołujemy nową listę
    label_ImieBottomValue["text"] = ""  # czyścimy pola label po usunięciu i wyświetleniu nowej listy
    label_NazwiskoBottomValue["text"] = ""
    label_TelefonBottomValue["text"] = ""
    label_EmailBottomValue["text"] = ""

def edytujKontakt():
    index = listbox_ListaKontaktow.index(ACTIVE)

    wyczyscEntry()                                  # czyszczenie pól przed wprowadzeniem nowych danych
    entry_Imie.insert(0, kontakty[index][0])        # dodawanie nowego imienia
    entry_Nazwisko.insert(0, kontakty[index][1])
    entry_Telefon.insert(0, kontakty[index][2])
    entry_Email.insert(0, kontakty[index][3])

    button_DodajKontakt["text"] = "Zmień kontakt"
    button_DodajKontakt["command"] = zmienKontakt

def zmienKontakt():
    index = listbox_ListaKontaktow.index(ACTIVE)

    kontakty[index][0] = entry_Imie.get()
    kontakty[index][1] = entry_Nazwisko.get()
    kontakty[index][2] = entry_Telefon.get()
    kontakty[index][3] = entry_Email.get()

    button_DodajKontakt["text"] = "Dodaj kontakt"
    button_DodajKontakt["command"] = dodajKotakt

    wyczyscEntry()
    entry_Imie.focus()
    listaKontaktow()







appLeft = Frame(root, pady=20)      # pady to dopełnienie, żeby nie dochodziło do samej krawędzi
appRight = Frame(root, pady=20)
appBottom = Frame(root, padx=20)    # pad od x
appLeft.grid(row=0, column=0)
appRight.grid(row=0, column=1)
appBottom.grid(row=1, column=0, columnspan=2)

# lewa strona aplikacji
label_ListaKontaktow = Label(appLeft, text="Lista kontaktów: ")
listbox_ListaKontaktow = Listbox(appLeft, width=20, height=7)
button_PokazKontakt = Button(appLeft,  text="Pokaż szczegóły kontaktu", command=pokazSzczegoly)
button_UsunKontakt = Button(appLeft,  text="Usuń kontakt", command=usunKontakt)
button_EdytujKontakt = Button(appLeft,  text="Edytuj kontakt", command=edytujKontakt)

label_ListaKontaktow.grid(row=0, column=0, columnspan=3)
listbox_ListaKontaktow.grid(row=1, column=0, columnspan=3)
button_PokazKontakt.grid(row=2, column=0)
button_UsunKontakt.grid(row=2, column=1)
button_EdytujKontakt.grid(row=2, column=2)

# prawa strona aplikacji
label_NowyKontakt = Label(appRight, text="Nowy kontakt: ")
label_Imie = Label(appRight, text="Imię: ")
entry_Imie = Entry(appRight)
label_Nazwisko = Label(appRight, text="Nazwisko: ")
entry_Nazwisko = Entry(appRight, width=30)
label_Telefon = Label(appRight, text="Telefon: ")
entry_Telefon = Entry(appRight)
label_Email = Label(appRight, text="Email: ")
entry_Email = Entry(appRight)

label_NowyKontakt.grid(row=0, column=0, columnspan=2)
label_Imie.grid(row=1, column=0, sticky=W)
label_Nazwisko.grid(row=2, column=0, sticky=W)
label_Telefon.grid(row=3, column=0, sticky=W)
label_Email.grid(row=4, column=0, sticky=W)
entry_Imie.grid(row=1, column=1, sticky=W)
entry_Nazwisko.grid(row=2, column=1, sticky=W)
entry_Telefon.grid(row=3, column=1, sticky=W)
entry_Email.grid(row=4, column=1, sticky=W)

button_DodajKontakt = Button(appRight, text = "Dodaj kontakt: ", command=dodajKotakt)
button_DodajKontakt.grid(row=5, column=0, columnspan=2)

# dolna część aplikacji
label_SzczegolyKontaktu = Label(appBottom, text="Szczegóły kontaktu:")
label_ImieBottom = Label(appBottom, text="Imię:")
label_ImieBottomValue = Label(appBottom, width=15)
label_NazwiskoBottom = Label(appBottom, text="Nazwisko:")
label_NazwiskoBottomValue = Label(appBottom, width=15)
label_TelefonBottom = Label(appBottom, text="Telefon:")
label_TelefonBottomValue = Label(appBottom, width=15)
label_EmailBottom = Label(appBottom, text="Email:")
label_EmailBottomValue = Label(appBottom, width=15)

label_SzczegolyKontaktu.grid(row=0, column=0, columnspan=2, sticky=W)
label_ImieBottom.grid(row=1, column=0)
label_ImieBottomValue.grid(row=1, column=1)
label_NazwiskoBottom.grid(row=1, column=2)
label_NazwiskoBottomValue.grid(row=1, column=3)
label_TelefonBottom.grid(row=1, column=4)
label_TelefonBottomValue.grid(row=1, column=5)
label_EmailBottom.grid(row=1, column=6)
label_EmailBottomValue.grid(row=1, column=7)


root.mainloop()