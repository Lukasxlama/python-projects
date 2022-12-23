"""
author: Lukas Sanz
file: ggt.py
catnr: 1BHIF-24
"""


from utils import ggt


n1 = float(input("Geben Sie die erste Zahl ein: "))
n2 = float(input("Geben Sie die zweite Zahl ein: "))
result = ggt(n1, n2)
print(f"Der Der größte gemeinsame Teiler von {n1} und {n2} ist --> {result}")