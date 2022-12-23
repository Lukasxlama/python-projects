"""
author: Lukas Sanz
file: ggt.py
catnr: 1BHIF-24
"""


def ggt(a: float, b: float):
    while b != 0:
        h = a % b
        a = b
        b = h
    return round(a, 2)