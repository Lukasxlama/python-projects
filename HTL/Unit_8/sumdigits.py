"""
author: Lukas Sanz
file: sumdigits.py
catnr: 1BHIF-24
"""

ziffernsumme = 0
zahl = input("Natürliche Zahl: ")
for ziffer in zahl:
    ziffernsumme += int(ziffer)
print(f"Die Ziffernsumme von {zahl} lautet {ziffernsumme}")
