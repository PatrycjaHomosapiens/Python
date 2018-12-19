#for x in range(0, 100, 10):
#    print("%4i%6i%8i" % (x, x**2, x**3))

#for x in range(100):
#    print("%4i%16i%8i" % (x, x**2, x**3))

#for x in range(100):
#    print("%4i%10.2f" % (x, x**0.5))

#for x in range(-100, 100):
#    print("%+4i" % (x))

#for x in range(-100, 100):
#    print("%+4i%10i" % (x, x**2))


# puste miejsca uzupelnione zerami
#for x in range(-100, 100):
#    print("%+4i%010i" % (x, x**2))

# ze znakiem -+, wyrównanie
for x in range(-100, 100):
    print("%+-4i%010i" % (x, x**2))