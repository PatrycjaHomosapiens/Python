"""
Cwiczenie 46-2 (zadanie domowe z pierwszego modułu kursu Python):
Instrukcje warunkowe
Napisz program, w którym zadeklarujesz dwie zmienne typu int o nazwach x oraz y.
Przypisz do nich wartości wprowadzone z „input”, a następnie za pomocą operatorów logicznych
i matematycznych wyświetl wynik następujących zdań logicznych:
- Czy x jest większe od y?
- Czy x pomnożone przez 2 jest większe od y?
- Czy y jest mniejsze od sumy x+3 i jednocześnie większe od x pomniejszonego o 2?
- Czy iloczyn liczb x i y jest parzysty? (Wykorzystaj do sprawdzenia operację modulo)
"""

x = int(input("Wprowadź dowolną liczbę całkowitą nr 1: "))
y = int(input("Wprowadź dowolną liczbę całkowitą nr 2: "))
print("Wynik:")

if x > y:
    print("-- 'x jest większe od 'y';")
elif x < y:
    print("-- 'x' jest mniejsze od 'y';")
else:
    print("-- 'x' jest równe 'y';")


if x * 2 > y:
    print("-- 'x * 2' jest większe od 'y' i wynosi:", str(x * 2) + ";")
elif x * 2 < y:
    print("-- 'x * 2' jest mniejsze od 'y' i wynosi;", str(x * 2) + ";")
else:
    print("-- 'x * 2' jest równe 'y' i wynosi;", str(x * 2) + ";")


if (y < x + 3) and (y > x - 2):
    print("-- 'y' spełnia jednocześnie dwa warunki: '(y < x + 3) and (y > x - 2)';")
else:
    print("-- 'y' nie spełnia jednocześnie dwóch warunków: '(y < x + 3) and (y > x - 2)';")


if (x * y) % 2 == 0:
    print("-- 'x * y' jest liczbą parzystą i wynosi:", str(x * y) + ".")
else:
    print("-- 'x * y ' nie jest liczbą parzystą i wynosi:", str(x * y) + ".")