"""
author: Lukas Sanz
file: HÜ - 1 - sort.py
catnr: 1BHIF-24
"""


### Funktionen
def sort():
    zahl_1, zahl_2, zahl_3, = float(input("Gib die erste Zahl ein: ")), float(input("Gib die zweite Zahl ein: ")), float(input("Gib die dritte Zahl ein: "))
    zahlen = [zahl_1, zahl_2, zahl_3]
    zahlen.sort()
    print("\nAusgabe:")
    print(f"1) {zahlen[0]}")
    print(f"2) {zahlen[1]}")
    print(f"3) {zahlen[2]}\n")
    schleife()

def schleife():
    q = input("Möchtest du das Programm wiederholen? (y/n): ").lower()
    if q == "y":
        sort()
    elif q == "n":
        exit()
    else:
        print("Ungültige Eingabe!")
        schleife()

### Ausgabe
sort()