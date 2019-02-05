""" Zadanie 81A:
Klasa Pracownicy:
- pola: imie, nazwisko, kontrakt (domyślnie: staż), pensja (domyślnie: 1000)
- konstruktor ustawiający wartości na ww. pól
- Gettery i Settery
"""
class Pracownicy:

    def __init__(self, imie, nazwisko, kontrakt, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kontrakt = kontrakt
        self.pensja = pensja

    def setImie(self, imie):
        self.imie = imie

    def setNazwisko(self, nazwisko):
        self.nazwisko = nazwisko

    def setKontrakt(self, kontrakt):
        self.kontrakt = kontrakt

    def setPensja(self, pensja):
        self.pensja = pensja

    def getImie(self):
        return self.imie

    def getNazwisko(self):
        return self.nazwisko

    def getKontrakt(self):
        return self.kontrakt

    def getPensja(self):
        return self.pensja

    def __str__(self):
        return "Imie: " + self.imie + ", Nazwisko: " + self.nazwisko + ", Kontrakt: " + self.kontrakt + ", Pensja: " + str(self.pensja)


class PracownicyController:     # to jest klasa do pracy na pracownikach

    def __init__(self):
        self.listaPracownik = []

    def dodajPracownika(self, imie, nazwisko, kontrakt="staż", pensja=1000):
        obj = Pracownicy(imie, nazwisko, kontrakt, pensja)
        self.listaPracownik.append(obj)

    def pokazPracownikow(self):     # pracownicy lądują w liście, to będzie lista obiektów
        for obiekt in self.listaPracownik:
            print(obiekt)       # ten print uruchamia __str__ czyli jakiś zdefiniowany przez nas napis

    def usunPracownika(self, nazwisko):
        for i, v in enumerate (self.listaPracownik):
            if v.getNazwisko() == nazwisko: # można zrobić "v.Nazwkisko == nazwisko", ale to niepraktyczne i eleganckie
                                # można zastosować remove, ale to niebezpieczne, bo usuwa po obiekcie, a pop po indeksie
                                # do tego usuwanie po indeksie jest szybsze
                self.listaPracownik.pop(i)
                break

    def zmienKontrakt(self, nazwisko, pensja):
        for i, v in enumerate (self.listaPracownik):
            if v.getNazwisko() == nazwisko:
                v.setKontrakt("etat")       # zmieniamy kotrakt każdemu na etat
                v.setPensja(pensja)
                break



class Firma(PracownicyController):

    def __init__(self, nazwaFirmy):
        super().__init__()      # to jest konstruktor listy nadrzędnej
        self.nazwaFirmy = nazwaFirmy
        self.menu()

    def menu(self):
        while(True):
            dec = input("D-dodaj, P-pokaz, U-usun, Z-zmiana kontraktu, Q-koniec: \n").upper()  # dec to decyzja, upper podciągnie litere do gory, czyli obojetnie czy wpisze duza czy mala litere

            if (dec == "D"):

                typ = input("Kogo dodajesz? S-stazysta, E-etatowiec: ").upper()

                imie = input("Podaj imię pracownika: ")
                nazwisko = input("Podaj nazwisko pracownika: ")

                if (typ == "E"):
                    pensja = input("Podaj pensję pracownika: ")
                    self.dodajPracownika(imie, nazwisko, "etat", pensja)
                else:
                    self.dodajPracownika(imie, nazwisko)    # dot. stażysty, bo stazysta ma tylko 2 informacje

            elif (dec == "P"):
                self.pokazPracownikow()

            elif (dec == "U"):
                nazwisko = input("Podaj nazwisko do usunięcia: ")
                self.usunPracownika(nazwisko)

            elif (dec == "Z"):
                nazwisko = input("Podaj nazwisko pracownika do zmiany: ")
                pensja = input("Podaj pensje pracownika: ")
                self.zmienKontrakt(nazwisko, pensja)

            elif (dec == "Q"):
                break


obj = Firma("XYZ")