"""
Cwiczenie 28 (zadanie domowe z pierwszego modułu kursu Python):
Interaktywny program
Napisz interaktywny program, który:
   -- Na zmienną a - przypisze wartość liczby całkowitej
   -- Na zmienną b - przypisze wartość liczby rzeczywistej
   -- Na zmienną c - przypisze wartość logiczną (Prawda | Fałsz)
   -- Na zmienną d – przypisze wartość tekstową
- Na zmiennej wynik zostanie przypisany iloczyn zmiennej b i 10
- A następnie, zmienna wynik zostanie podniesiona do potęgi a
- A następnie,  zmienna wynik zostanie pomnożona przez c
- Wypisz informacje 10x w postaci: Podano napis d, oraz obliczono wynik
- d i wynik – są zmiennymi
"""

a = int(input("A -> Wpisz liczbę całkowitą: "))
b = float(input("B -> Wpisz liczbę rzeczywistą (niecałkowitą): "))
c = bool(input("C -> Wpisz 'True' lub 'False': "))
d = str(input("D -> Wpisz dowolne słowo: "))
wynik = b * 10
print("Wynik dla   (B * 10)             to: ", wynik)
wynik **= a
print("Wynik dla  ((B * 10) ** A)       to: ", wynik)
wynik *= c
print("Wynik dla (((B * 10) ** A) * C)  to: ", wynik)
print(("Podano napis '" + d + "' oraz obliczono: " + str(wynik) + "." + "\n") * 10)

"""
# wersja Borysa

a=int(input('Podaj wartośc liczby całkowitej:'))
b=float(input('Podaj wartośc liczby rzeczywistej:'))
c=input('Podaj wartośc logiczną (Prawda lub Fałsz):')
d=input('Podaj wartośc tekstową:')

if c == 'Prawda':
    e=True
elif c == 'Fałsz':
    e=False
else:
    print('Podałeś niewłaściwą wartośc logiczną')
    exit()

wynik = b*10
wynik = pow(wynik,a)
wynik = wynik*e
i=0

for x in range(10):
    print('Podano napis {}, oraz obliczono {}'.format(d,wynik))
    i+=1
"""