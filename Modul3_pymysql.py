import pymysql

try:
    conn = pymysql.connect('localhost', 'root', 'alxalx', 'bd93', charset='utf8')
    c = conn.cursor()
    print("połączenie ustanowione!")
except:
    print("błąd połączenia")


def select():
    c.execute("SELECT * FROM pracownicy")
    result = c.fetchall()

    print("%10s %10s %10s %10s" % ("Imię", "Nazwisko", "Pensja", "Pesel"))
    for row in result:
        print("%10s %10s %10s %10s" % (row[1], row[2], row[3], row[4]))

def insert():
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    pensja = input("Podaj pensję: ")
    pesel = input("Podaj pesel: ")
    c.execute('INSERT INTO pracownicy (imie, nazwisko, pensja, pesel) VALUES (%s,%s,%s,%s)', (imie, nazwisko, pensja, pesel))
                # pod (imie, nazwisko, pensja, pesel) wstawiamy dane z inputów
                # (%s,%s,%s,%s) to jest miejsce "zarezerwowane" dla tych danych, to jest string

    dec = input("Czy dodać dane? T / N: ").upper()
    if dec == "T":
        conn.commit()
        print("Dodano pomyślnie!")
    else:
        conn.rollback()
        print("Operacja anulowana!")

def delete():
    doUsuniecia = input("Podaj pesel osoby do usunięcia: ")
    c.execute('DELETE FROM pracownicy WHERE pesel = (%s)', (doUsuniecia))

    dec = input("Czy na pewno chcesz usunąć? T / N: ").upper()
    if dec == "T":
        conn.commit()
        print("Usunięto pomyślnie!")
    else:
        conn.rollback()
        print("Operacja anulowana!")

def update():
    pesel = input("Podaj pesel osoby do modyfikacji: ")
    imie = input("Podaj nowe imię: ")
    nazwisko = input("Podaj nowe nazwisko: ")
    pensja = input("Podaj nową pensję: ")

    c.execute('SELECT idpracownicy FROM pracownicy WHERE pesel = (%s)', (pesel))
    id = c.fetchall()[0][0]
    print(id)
    c.execute('UPDATE pracownicy SET imie=%s, nazwisko=%s, pensja=%s, pesel=%s WHERE idpracownicy = (%s)',  (imie, nazwisko, pensja, pesel, id))

    dec = input("Czy na pewno chcesz zmienić dane? T / N: ").upper()
    if dec == "T":
        conn.commit()
        print("Zmieniono pomyślnie!")
    else:
        conn.rollback()
        print("Operacja anulowana!")






while(True):
    dec = input("S-show, I-insert, D-delete, U-update, Q-exit: ").upper()

    if(dec == "S"):
        select()
    elif(dec == "I"):
        insert()
    elif(dec == "D"):
        delete()
    elif(dec == "U"):
        update()
    elif(dec == "Q"):
        print("Koniec")
        conn.close()
        break