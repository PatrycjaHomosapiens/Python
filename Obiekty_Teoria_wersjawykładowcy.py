
a = [1,2,3,4]
print(sum(a))
print(a.reverse())

class Człowiek():
    def __init__(self, imie, nazwisko): # konstruktor
        self.imie = imie                # pola obiektowe (instancyjne)
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return f'Jestem człowiekiem, nazywam się {self.imie} {self.nazwisko}'

    def __str__(self):
        return f'jestem {self.imie}'

x = Człowiek('Ania', 'Kowalska')
print(x.imie, x.nazwisko)

x.imie = "Karolina"
print(x.imie, x.nazwisko)

karol = Człowiek('Karol', 'Karolak')
print(karol.imie, karol.nazwisko)

print(x.przedstaw_sie())
print(karol.przedstaw_sie())

print(karol)
print(str(karol))
print(karol.__str__())

lista_ludzi = [x, karol]
print(lista_ludzi)

class Sejf:
    def __init__(self):
        self.__zawartosc = None     # pole prywatne

    def schowaj(self, skarb):
        self.__zawartosc = skarb

    def wyjmij(self):
        ret = self.__zawartosc
        self.__zawartosc = None
        return ret

dziupla = Sejf()
dziupla.schowaj('jabłko')

print(dziupla.__zawartosc)      # to dziala, ale jest naruszenniem wew. zasad Pythona, żeby nie zagladać do pól prywatnych

skarb = dziupla.wyjmij()
print(skarb)

