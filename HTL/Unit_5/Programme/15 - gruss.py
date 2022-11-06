"""
author: Lukas Sanz
file: 15 - gruss.py
catnr: 1BHIF-24
"""


### Funktion
def gruss(fill1, fill2, fill3, fill4, fill5, fill6):
    print("\nDas ist dein Text:\n")
    print(f"{fill1}!\nHier {fill2} gefällt es mir {fill3}.\nGestern waren wir {fill4}. Das war {fill5}!\nBis bald,\n{fill6}")

### Text
print("Das hier ist der Text:\n\n<Füllwort 1>!\nHier <Füllwort 2> gefällt es mir <Füllwort 3>.\nGestern waren wir <Füllwort 4>. Das war <Füllwort 5>!\nBis bald,\n<Füllwort 6>\n")

### Variablen
text_fill1 = input("Gib das erste Füllwort ein: ")
text_fill2 = input("Gib das zweite Füllwort ein: ")
text_fill3 = input("Gib das dritte Füllwort ein: ")
text_fill4 = input("Gib das vierte Füllwort ein: ")
text_fill5 = input("Gib das fünfte Füllwort ein: ")
text_fill6 = input("Gib das sechste Füllwort ein: ")

### Ausgabe
gruss(text_fill1, text_fill2, text_fill3, text_fill4, text_fill5, text_fill6)