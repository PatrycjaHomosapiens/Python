"""
Napisz prosty kalkulator dla liczb zmiennoprzecinkowych, ktory pozwala uzytkownikowi kolejno:
- wprowadzenie pierwszej liczby
- wprowadzenie jednego z podstawowych dzialam matematycznych (plus, minus, podzeil, pomnoz) w postaci znaków = - * /
- wprowadzenie drugie liczby
"""

a = float(input("Wpisz pierwszą dowolną liczbę rzeczywistą: "))
b = input("Wpisz jeden wybrany znak '+', '-', '*', '/': ")
c = float(input("Wpisz pierwszą dowolną liczbę rzeczywistą: "))

if (b == "+"):
    print(a + c)
elif(b == "-"):
    print(a + c)
elif (b == "*"):
    print(a * c)
elif (b == "/"):
    if (c == 0):
        print("Dzielenie przez zero")
    else:
        print(a / c)