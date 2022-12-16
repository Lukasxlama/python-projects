"""
author: Lukas Sanz
file: squareroot.py
catnr: 1BHIF-24
"""

from math import sqrt


def quadratwurzel(zahl, schritte):
    x_n_minus_1 = zahl
    for i in range(schritte):
        x_n = (x_n_minus_1 + zahl / x_n_minus_1) / 2
        x_n_minus_1 = x_n
    fehler = abs(sqrt(zahl) - x_n)
    genau = sqrt(zahl)
    print(f"Errechnete Näherung: {x_n}")
    print(f"Genaue Lösung: {genau}")
    print(f"Fehler: {fehler}")


zahl_ = int(input("Bitte gib die Zahl ein, von der die Quadratwurzel bestimmt werden soll: "))
schritte_ = int(input("Bitte gib die Anzahl von Iterationsschritten ein: "))
quadratwurzel(zahl_, schritte_)
