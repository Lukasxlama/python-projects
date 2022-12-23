"""
author: Lukas Sanz
file: factorial.py
catnr: 1BHIF-24
"""


def fak(n):
    product = 1

    for i in range(1, n + 1):
        product *= i
    return product


if __name__ == "__main__":
    number = int(input("Gib eine ganze Zahl ein: "))
    result = fak(number)
    print(f"{number}! = {result}")