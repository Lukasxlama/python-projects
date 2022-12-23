"""
author: Lukas Sanz
file: show_numbers.py
catnr: 1BHIF-24
"""


i=1
step=1

print(f"-------------------------------------------------")

while i <= 32:
    dezimal, binaer, hexadezimal = str(i), str(bin(i)), str(hex(i)).upper()
    binaer, hexadezimal = binaer.rjust(8, " "), hexadezimal.rjust(2, " ")
    binaer = binaer.replace("0b", "")
    if i < 10:
        print(f"| Dezimal: {i}  | Binär: {binaer} | Hexadezimal:  {hexadezimal[2:]} |")
    if 10 <= i < 16:
        print(f"| Dezimal: {i} | Binär: {binaer} | Hexadezimal:  {hexadezimal[2:]} |")
    if i >= 16:
        print(f"| Dezimal: {i} | Binär: {binaer} | Hexadezimal: {hexadezimal[2:]} |")
    i += 1

print(f"-------------------------------------------------")