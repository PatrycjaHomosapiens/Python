# podajemy liczbę, jeżeli błąd (czyli nie int), to zamiast błędu, program pyta jeszcze raz o liczbę, aż do skutku

while True:
    try:
        a = int(input('Podaj liczbę całkowitą: \n'))
        break
    except:
        continue