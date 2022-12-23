"""
author: Lukas Sanz
file: or1.py
catnr: 1BHIF-24
"""


print(f"  a  |  b  | a or b  |")
print(f"----------------------")

for a in [0, 1]:
    for b in [0, 1]:
        c = a or b
        print(f"  {a}  |  {b}  |    {c}    |")
        print(f"  {a}  |  {b}  |    {c}    |")

print(f"----------------------")