"""
Cwiczenie 52 (zadanie domowe z pierwszego modułu kursu Python):
Pętle
Zaimplementuj własny mechanizm obliczania potęgi bez użycia operatora ** i innych wbudowanych funkcji matematycznych.
- Użytkownik podaje podstawę i wykładnik potęgi
- Wykorzystując mechanizm pętli zaimplementuj odpowiedni kod
- Pamiętaj… wszystko co jest podniesione do potęgi 0 jest równe 1
- Wykładnikiem potęgi są liczby >= 0
"""

podstawaPotegi = float(input("Podaj podstawę potęgi: "))
wykładnikPotegi = float(input("Podaj wykładnik potęgi (liczba dodatnia): "))

i = 1
wynik = podstawaPotegi

while i < wykładnikPotegi:
        wynik *= podstawaPotegi
        #print(wynik)
        i += 1
print(wynik)