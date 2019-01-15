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
