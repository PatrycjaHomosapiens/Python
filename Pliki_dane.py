# plik = open('ala.txt','w')
# plik.write('czesc')
# plik.close()

# plik = open('dane.txt', 'r')
# s = plik.read()
# print(s)
# plik.close()


# otwieranie pliku:

with open('Pliki_dane.py', 'r') as f:
    s = f.read()
    print('w obrębie with', f.closed)
    # instr 2
    # instr 3

print(s)
print('poza with', f.closed)