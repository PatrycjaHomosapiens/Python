"""
Cwiczenie 42 (zadanie domowe z pierwszego modułu kursu Python):
Instrukcje warunkowe
Wykonaj prosty test poprawności logowania
- Jeżeli użytkownik podał login: admin i hasło: hasloadmina – przejdź do panelu administratora
- Jeżeli użytkownik podał login: user i hasło: haslousera – przejdź do panelu użytkownika
- W przeciwnym razie wyświetl stosowny komunikat
- W zadaniu wykorzystaj słownik: konta = {'admin': ‚hasloadmina', 'user': ‚haslousera'}
"""


konta = {"admin": "hasloadmina", "user": "haslousera"}

login = input("Podaj login 'admin' lub 'user': ")

if login == "admin":
    print("Logujesz się jako administrator.")
    haslo = input("Wprowadź 'hasloadmina', aby przejść do panelu administratora: ")
    if haslo == konta["admin"]:
        print("Zalogowałeś się do konta administratora :)")
    else:
        print("Błędne hasło!")
elif login == "user":
    print("Logujesz się jako użytkownik.")
    haslo = input("Wprowadź 'haslousera', aby przejść do panelu użytkownika: ")
    if haslo == konta["user"]:
        print("Zalogowałeś się do konta użytkownika :)")
    else:
        print("Błędne hasło!")
else:
    print("Podałeś błędny login!")