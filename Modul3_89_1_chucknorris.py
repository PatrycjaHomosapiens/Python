# Zad. 89_1
# Pobierz za pośrednctwem API listę kategorii, żartósz Chuckiem Norrisem
# Użytkownik z otrzymanej listy wpisuje kategorię, z której ma zostać wyświetlon lasowy żart
# Imię i Nazwisko Chucka Norrisa w wylosowanym żarcie zmień na swoje, a następnie żart wyświetl w konsoli

# Podłączanie się do api i pobieranie

import requests     # wcześniej trzeba było zainstalować requests (File-Settings...)

res = requests.get('https://api.chucknorris.io/jokes/categories')
print(res.json())


kategoria = input("Z jakiej kategorii chcesz otrzymać żarcik? ")

zart = requests.get('https://api.chucknorris.io/jokes/random?category='+kategoria)
lista = zart.json()
zart = lista['value']

zart = zart.replace("Chuck Norris","Patrycja Matalewska")
zart = zart.replace(" he "," she ")
print(zart)

#print(zart.json()['value'])

