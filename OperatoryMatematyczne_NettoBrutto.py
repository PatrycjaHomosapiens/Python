"""
Napisz program przeliczający zadaną kwotę brutto np. 1000 na kwotę netto.
Zastosuj kilka zmiennych do obliczania stawek VAT (3%, 7%, 23%) oraz wynik działania programu zaokrąglij do dwóch miejsc po przecinku
"""

kwota_brutto = 1000
vat1 = 1.03
vat2 = 1.07
vat3 = 1.23

kwota_netto1 = kwota_brutto / vat1
kwota_netto2 = kwota_brutto / vat2
kwota_netto3 = kwota_brutto / vat3

print(kwota_netto1)
print(kwota_netto2)
print(kwota_netto3)

#print("%.3f" % kwota_netto2)

print(round(kwota_netto1,3))
print(round(kwota_netto2,3))
print(round(kwota_netto3,3))

""" Można też zapisać to tak:
kwotaBrutto = 1000
vat1 = 3 
vat2 = 7
vat3 = 23

kwotaNetto1 = kwotaBrutto / (1 + vat1/100)
kwotaNetto2 = kwotaBrutto / (1 + vat2/100)
kwotaNetto3 = kwotaBrutto / (1 + vat3/100)

print(kwotaNetto1)
print(kwotaNetto2)
print(kwotaNetto3)

kwotaBrutto1 = kwotaNetto1 + (kwotaNetto1 * vat1/100)
kwotaBrutto2 = kwotaNetto2 + (kwotaNetto2 * vat2/100)
kwotaBrutto3 = kwotaNetto3 + (kwotaNetto3 * vat3/100)

print(kwotaBrutto1)
print(kwotaBrutto2)
print(kwotaBrutto3)
"""
