"""
author: Lukas Sanz
file: Hü - 04 - smueckeck.py
catnr: 1BHIF-24
"""


### Variable
points = int(input("Gib eine Punktzahl von 0-5 ein: "))

### match-case Anweisung
match points:
    case 0:
        print("Null Punkte sind absolut zu wenig!")
    case 1:
        print("Ein Punkt ist viel zu wenig!")
    case 2:
        print("Zwei Punkte sind zu wenig!")
    case 3:
        print("Drei Punkte sind gerade genug!")
    case 4:
        print("Vier Punkte sind nicht schlecht!")
    case 5:
        print("Fünf Punkte sind sehr gut!")
    case _:
        print("Du hast anscheinend eine ungültige Punktzahl eingegeben!")