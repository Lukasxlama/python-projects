"""
author: Lukas Sanz
file: kgv.py
catnr: 1BHIF-24
"""


from utils import ggt


def kgv(a: float, b: float):
    calc = (a * b) / ggt(a, b)
    return round(calc, 2)


if __name__ == "__main__":
    n1 = float(input("Geben Sie die erste Zahl ein: "))
    n2 = float(input("Geben Sie die zweite Zahl ein: "))
    result = kgv(n1, n2)
    print(f"Das kleinste gemeinsame Vielfache von {n1} und {n2} ist --> {result}")