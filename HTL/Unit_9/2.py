"""
author: Lukas Sanz
file: 2.py
catnr: 1BHIF-24
"""


print("a)")
sum=0
i=0
count=0

while i <= 199:
    sum += i
    i += 2
    count += 1
    print(f"{count}. Zahl: {sum}")

print("\n\nb)")
sum = 0
i = 1
count=0

while i <= 199:
    sum += i
    i += 2
    count += 1
    print(f"{count}. Zahl: {sum}")

print("\n\nc)")
sum = 0
i = 2
durchschnitt = 0

while i <= 201:
    sum += i
    i += 2

durchschnitt = sum / 100
print(f"Durchschnitt = (2 + 4 + 6 + 8 + ... + 100) / 100 = {durchschnitt}")