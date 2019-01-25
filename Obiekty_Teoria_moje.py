
a = [1,2,3,4]
print(sum(a))
print(a.reverse())

class Czlowiek():       # nazwy klas piszemy Wielką Literą
    def __init__(self, imie, nazwisko): # konstruktor, imie i nazwisko to parametr, można dodać dowolną ilość parametrów
        self.imie = imie                # to jest pole obiektowe (instancyjne), imie i nazwisko to pola, wewnętrzna zmienna imie przypisuję
        self.nazwisko = nazwisko        # przegrodka, zmienna, gdzie chcę przechoywać wartość parametru
    def przedstaw_sie(self):            # self jest z automatu, niczego więcej nie potrzebujemy
        return f'Jestem człowiekiem, nazywam się {self.imie} {self.nazwisko}'       # self.imie to obiekt.pole (atrybut)

    #def __str__(self):
     #   return f'jestem {self.imie}'

x = Czlowiek('Ania', 'Kowalska')     # ania to zmienna
print(x.imie, x.nazwisko)

x.imie = 'Karolina'      # nadpisanie zmiennej, to jest naruszenie hermetyzacji
print(x.imie, x.nazwisko)

karol = Czlowiek('Karol', 'Karolak')
print(karol.imie, karol.nazwisko)

print(x.przedstaw_sie())
print(karol.przedstaw_sie())

# wsszytkie 3 poniższe rzeczy pokazują to samo
print(karol)
print(str(karol))
print(karol.__str__())  # pokazuje, gdzie jest

# jeśli odkomentuję poniższe, to zamiast "<__main__.Czlowiek object at 0x00350C90>" pokaże się "jestem Karol"
# def __str__(self):
#   return f'jestem {self.imie}'

lista_ludzi = [x, karol]
print(lista_ludzi)  # wypisuje ludzi jako obiekty


# dziedziczenie

class Student(Czlowiek):        # jeśli damy tylko tę linijkę i pass pod spodem, to już jest działająca klasa student, ktory jest studentem
    def __init__(self, imie, nazwisko, kierunek, rok):
        super().__init__(imie, nazwisko)        # imie i nazwisko zniknelo, musimy zrobic super init
                                                # można tu dać też na sztywno dane: super().__init__('Ania', 'Kowalska')
                                # super init pojawia się wewnątrz klas, bo w nowej klasie odwoluje sie do starego inita
        self.kierunek = kierunek
        self.rok = rok

    def wypisz_na_konsole(self):
        print(self.przedstaw_sie())

    def przedstaw_sie(self):        # to przedstaw się przekryje poprzednie przedstaw się od Czlowieka
        wynik = super().przedstaw_sie()
        wynik += f'\nJestem studentem: {self.kierunek} {self.rok}'
        return wynik

ania = Student('Ania', 'Kowalska', 'Socjologia', 3)
print(ania.przedstaw_sie())
ania.wypisz_na_konsole()

"""
Opis dziedziczenia na powyższych przykładzie:
initowi przypisujemy
1 instrukcja to zajrzyj do nadlkasy, czyli do czlowieka init, znajdujemy czlowieka i jego init i odpalamy
w pudelku mamy 5 rzeczy: imie, nazwisko, przedstaw sie, string i init (str i init to funkcja ?)
wracamy do init studenta i doklepujemy do czlowieka dodatkowe pudelko z: kierunek, rok i wypisz_na_konsole
z automatu dostajemy jeszcze jedno dodatkowe pudelko z automatu z wcześniej zrobionymi rzeczami
init Student musi miec to samo co Czlowiek i dodatkowe rzeczy
nie można napisać drugiej metody, która się tak samo nazywa
"""

