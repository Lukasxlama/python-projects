"""
author: Lukas Sanz
file: squareroot.py.py
catnr: 1BHIF-24
"""


from math import sqrt, pi


zahl = float(input("Gib eine Zahl ein: "))
iteration = int(input("Gib eine Anzahl von Iterationsschritten ein: "))
x0, a = zahl, zahl
x_iter = 0

for _ in range(iteration):
    x1 = (x0 + a / x0) / 2
    x2 = (x1 + a / x1) / 2
    x3 = (x2 + a / x2) / 2
    ...
    x_iter = (x_iter + a / x2) / 2
    genau = sqrt(zahl)
    # fehler = abs(pi - x_iter)  # ???
    fehler = abs(x_iter - genau)

print(f"\nNäherung = {x3}\nGenaue Lösung = {genau}\nFehler = {fehler}")
