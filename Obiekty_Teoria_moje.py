
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

