"""
author: Lukas Sanz
file: e.py
catnr: 1BHIF-24
"""


from factorial import fak


def calculate_e(n_):
    e = 0

    for i in range(n_ + 1):
        e += 1 / fak(i)
    return e


if __name__ == "__main__":
    n = int(input("Gib eine Zahl für n ein: "))
    result = calculate_e(n)
    print(f"e = {result}")