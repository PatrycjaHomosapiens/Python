"""
Firma X w styczniu miala dochod 700 zł ....
"""

dochod = 700
koszty = 500 # koszty są stałe w każdym miesiącu
zysk = dochod - koszty

dochod2 = dochod * 1.5
zysk2 = dochod2 - koszty

dochod3 = dochod2 * 1.5
zysk3 = dochod3 - koszty

dochod4 = dochod3 * 1.5
zysk4 = dochod4 - koszty

dochod5 = dochod4 * 1.5
zysk5 = dochod5 - koszty

dochod6 = dochod5 * 1.5
zysk6 = dochod6 - koszty

print(round(zysk, 2))
print(round(zysk2, 2))
print(round(zysk3, 2))
print(round(zysk4, 2))
print(round(zysk5, 2))
print(round(zysk6, 2))

""" wynik:
200
500
1075
1862.50
3043.75
4815.62
"""
