# liczby 0-100 parzyste

for x in range(0, 101):
    if (x % 2 == 0):
        print(x)


# liczby podzielne przez 5, 1 sposób

for x in range(0, 101):
    if (x % 5 == 0):
        print(x)

# liczby podzielne przez 5, 2 sposób

for x in range(5, 101, 5):
    print(x)