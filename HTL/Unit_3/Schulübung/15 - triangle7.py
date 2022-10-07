"""
author: Lukas Sanz
file: 15 - triangle7.py
catnr: 1BHIF-24
"""


from math import sqrt


kat_1 = float(input("Gib die erste Kathete ein: "))
hyp = float(input("Gib die Hypothenuse ein: "))
x = str(input("Gib ein Längenmaß ein (z.B. cm, m): "))
kat_2 = sqrt(hyp ** 2 - kat_1 ** 2)
U = kat_1 + kat_2 + hyp
A = (kat_1 * kat_2) / 2
print("Die zweite Kathete ist " + str(round(kat_2, 2)) + " " + x + " lang, der Umfang beträgt " + str(round(U, 2)) + " " + x + " und die Fläche beträgt " + str(round(A, 2)) + " " + x + "².")
