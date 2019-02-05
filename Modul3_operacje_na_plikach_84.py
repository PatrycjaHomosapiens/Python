# OPERACJE NA PLIKACH
# tworzenie pliku, zamknięcie i dopisywanie nowych wierszy do utworzonego pliku

dane = open("84.txt", "w")
dane.write("Adam\n")
dane.write("Ewa\n")
dane.close()

dane = open("84.txt", "a")
for i in range(1, 51):
    dane.write(str(i)+"\n")

dane.close()
