# 3 poniższe linijki zbudują plik tekstowy, w którym będzie napisane 'czesc'

plik = open('ala.txt','w')      # to jest otwarcie pliku

plik.write('czesc')

plik.close()                    # to jest zamknięcie pliku


# oprócz trybu 'w' są jeszcze tryby "w+", "w-"