"""
author: Lukas Sanz
file: HÜ - 1 - sort.py
catnr: 1BHIF-24
"""


### Funktionen
def sort():
    zahl_1 = int(input("Gib die erste Zahl ein: "))
    zahl_2 = int(input("Gib die zweite Zahl ein: "))
    zahl_3 = int(input("Gib die dritte Zahl ein: "))
    liste = [zahl_1, zahl_2, zahl_3]
    print("\nAusgabe:")
    print(f"1) {min(liste)}")
    print(f"2) {zahl_1 + zahl_2 + zahl_3 - min(liste) - max(liste)}")
    print(f"3) {max(liste)}\n")
    frage()

def frage():
    q = input("Möchtest du noch eine Zahl eingeben? (y/n): ").lower()
    if q == "y":
        sort()
    elif q == "n":
        exit()
    else:
        print("Ungültige Eingabe!")
        frage()

### Ausgabe
sort()