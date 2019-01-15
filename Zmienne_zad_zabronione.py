"""
Sprawdź czy można wykorzystać, jako zmienną nazwę zabronioną (and, if, break)
"""

and = 8
print(and)

zm = False
print(type(zm))

zm = 3.14159
print(int(zm))
print(round(zm,0))
print(round(zm,1))
print(round(zm,2))

zm1 = bool(0) # fałsz
zm2 = bool("")
print(zm1, zm2)
