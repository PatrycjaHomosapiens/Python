wynagrodzenie_netto = 5500
godziny_pracy = 168

stawka_godzinowa_netto = wynagrodzenie_netto / godziny_pracy
print(stawka_godzinowa_netto)   # bez zaokrąglenia
print(round(stawka_godzinowa_netto, 2))   # z zaokrągleniem

podatek_dochodowy = 18

stawka_godzinowa_brutto = stawka_godzinowa_netto * (1 + podatek_dochodowy/100)
print(stawka_godzinowa_brutto)   # bez zaokrąglenia
print(round(stawka_godzinowa_brutto, 2))   # z zaokrągleniem