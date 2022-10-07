"""
author: Lukas Sanz
file: 14 - triangle6.py
catnr: 1BHIF-24
"""


from math import sqrt


kat_1 = float(input("Gib die erste Kathete ein: "))
kat_2 = float(input("Gib die zweite Kathete ein: "))
x = str(input("Gib ein Längenmaß ein (z.B. cm, m): "))
hyp = sqrt(kat_1 ** 2 + kat_2 ** 2)
U = kat_1 + kat_2 + hyp
A = (kat_1 * kat_2) / 2
print("Die Hypotenuse ist " + str(round(hyp, 2)) + x + " lang, der Umfang beträgt " + str(round(U, 2)) + x + " und die Fläche beträgt " + str(round(A, 2)) + x + "².")
