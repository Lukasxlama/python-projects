"""
author: Lukas Sanz
file: and1.py
catnr: 1BHIF-24
"""


print(f"  a  |  b  | a and b |")
print(f"----------------------")

for a in [0, 1]:
    for b in [0, 1]:
        c = a and b
        print("  {}  |  {}  |    {}    |".format(a, b, c))

print(f"----------------------")