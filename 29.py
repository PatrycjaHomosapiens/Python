chleb = 6.50
sok = 4
paczek = 5.50

suma_chleb = int(input("Wpisz, ile sztuk chleba chcesz kupić? "))
suma_sok = int(input("Wpisz, ile litrów soku chcesz kupić? "))
suma_paczek = int(input("Wpisz, ile sztuk pączków chcesz kupić? "))
print("Twoje zamówienie to:")
print(" - " + str(suma_chleb) + " chleby po " + str(chleb) + " zł za bochenek,")
print(" - " + str(suma_sok) + " soki po " + str(sok) + " zł za litr,")
print(" - " + str(suma_paczek) + " pączki po " + str(paczek) + " zł za sztukę.")
zamówienie = round(suma_chleb * chleb + suma_sok * sok + suma_paczek * paczek, 2)

print("Twoje zamówienie razem to: " + str(zamówienie) + " zł.")




