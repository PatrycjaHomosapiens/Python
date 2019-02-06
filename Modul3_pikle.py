# Importowanie pickle

import pickle

print("Marynowanie listy do pliku.")
smak = ["łagodny", "pikantny", "kwaszony"]
firma = ["Dawtona", "Klimex", "Vortumnus"]

f = open("dane.dat", "wb")      # tworzy się plik

pickle.dump(smak, f)
pickle.dump(firma, f)
f.close()

print("Odmarynowanie list.")

f = open("dane.dat", "rb")      # odczytuje się plik 

smak = pickle.load(f)
firma = pickle.load(f) # funkcja ta przyjmuje 1 argument, czyli plik, z którego ma załadować kolejny zamarynowany obiekt

print(smak)
print(firma)
f.close()