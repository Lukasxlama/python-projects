"""
author: Lukas Sanz
file: horner8.py
catnr: 1BHIF-24
"""


### Funktionen
## Berechnung der Dezimalzahl [Hornermethode]
def dezimal_berechnen():
    ergebnis_ = 0
    for stelle in range(len(oktalzahl) + 1):
        ziffer = int(oktalzahl[stelle])
        try:
            ziffer_add = int(oktalzahl[stelle + 1])
            if stelle == 0:
                ergebnis_ = ziffer * 8 + ziffer_add
            elif stelle != 0:
                ergebnis_ = ergebnis_ * 8 + ziffer_add
        except IndexError:
            return ergebnis_
    return ergebnis_


### Ausgabe
while True:

    ## Input
    try:
        oktalzahl = input("""
Gib eine Oktalzahl ein:
Erlaubte Zeichen : 0, 1, 2, 3, 4, 5, 6, 7
--> """)
    except BaseException as Error:
        print(f"\nUngültige Eingabe!\nFehlermeldung: {Error}")
        continue

    ## Überprüfung, ob es sich um eine Oktalzahl handelt
    try:
        oktalzahl_int = int(oktalzahl)
    except ValueError:
        print(f"\nUngültige Eingabe!\nDeine Eingabe ist keine Zahl!")
        continue

    if "8" in oktalzahl or "9" in oktalzahl:
        print(f"\nUngültige Eingabe!\nDeine Eingabe ist keine Oktalzahl!")
        continue

    ## Berechnung der Dezimalzahl
    try:
        ergebnis = dezimal_berechnen()
        print(f"\n{oktalzahl} (B=8) --> Dezimal = {ergebnis} (B=10)")
    except BaseException as Error:
        print(f"\nUngültige Eingabe!\nFehler bei der Berechnung\nFehlermeldung: {Error}")

    ## Abfrage, ob das Programm wiederholt werden soll
    loop = input("\nMöchtest du das Programm wiederholen? (Y/N): ").lower()
    if loop == "y":
        continue
    elif loop == "n":
        break
    else:
        exit("Ungültige Eingabe!\nProgramm wird beendet..")

exit()
