"""
Cwiczenie 53 (zadanie domowe z pierwszego modułu kursu Python):
Pętle
Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:
Znaki nie będące cyframi mają być ignorowane konwertujemy cyfry, nie liczby, a zatem:
- 911 to "dziewięć jeden jeden"
- 1100 to "jeden jeden zero zero.
"""
# DO ZROBIENIA

slownik = {"0": "zero ", "1": "jeden ", "2": "dwa ", "3": "trzy ", "4": "cztery ", "5": "pięć ", "6": "sześć ", "7": "siedem ", "8": "osiem ", "9": "dziewięć "}

liczba = input("Podaj liczbę: ")
skonwertowane = []

for i in liczba:
    for y in slownik:
        if i == y:
            skonwertowane.append(slownik[y])
            #print(y)
            #print(skonwertowane)
        else:
            continue
print(skonwertowane)