"""
author: Lukas Sanz
file: logical1.py
catnr: 1BHIF-24
"""


print(f" a  | b  | c  | a and b or not c  |")
print(f"-----------------------------------")

for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            d = a and b or not c
            print(f" {a}  | {b}  | {c}  |         {int(d)}         |")

print(f"-----------------------------------")