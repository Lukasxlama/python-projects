"""
author: Lukas Sanz
file: mathelib.py
catnr: 1BHIF-24
"""


### Bibliotheken
from math import sqrt

### Funktionen
def arith_mean(numb_1: float, numb_2: float, numb_3: float):
    calc = round((numb_1 + numb_2 + numb_3) / 3, 2)
    return calc

def geom_mean(numb_1: float, numb_2: float):
    if numb_1 * numb_2 < 0:
        return -1
    calc = round(sqrt(numb_1 * numb_2), 2)
    return calc

def sum(numb_1: float, numb_2: float):
    calc = numb_1 + numb_2
    return calc

def velocity(t: float):
    if t < 0:
        return -1
    g = 9.81  # m/s²
    v = g * t
    v = round(v * 3.6, 2)
    return v

def space(t: float):
    if t < 0:
        return -1
    g = 9.81  # m/s²
    v = g * t  # Geschwindigkeit
    s = v * t  # Strecke
    s = round(s / 1000, 2)  # Runden und in Km umrechnen
    return s

def mod(dividend: int, divisor: int):
    calc = dividend - divisor * int(dividend / divisor)
    return calc

def square_root(radikant: float):  # TODO Exeption abfangen und return -1
    if radikant < 0:  # TODO Exeption abfangen und return -1
        return -1  # TODO Exeption abfangen und return -1
    calc = round(radikant ** 0.5, 2)  # TODO Exeption abfangen und return -1
    return calc  # TODO Exeption abfangen und return -1

def div(dividend: float, divisor:float):
    try:
        quotient = round(dividend / divisor, 2)
        return quotient
    except ZeroDivisionError:
        return 0