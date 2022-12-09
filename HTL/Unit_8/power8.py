"""
author: Lukas Sanz
file: power8.py
catnr: 1BHIF-24
"""


### Funktionen
## Berechnung für die Hochzahlen bei der Potenzmethode
def indizes_berechnen():
    try:
        index = []
        for i in range(len(oktalzahl)):
            index.append(len(oktalzahl) - (i + 1))
        return index
    except BaseException as Error_:
        print(f"\nUngültige Eingabe!\nFehler beim berechnen der Indizes\nFehlermeldung: {Error_}")


## Berechnung der Dezimalzahl [Potenzmethode]
def dezimal_berechnen(index: list):
    ergebnis_ = 0
    for stelle in range(len(oktalzahl)):
        ziffer = int(oktalzahl[stelle])
        ergebnis_ += ziffer * 8 ** index[stelle]  # Index von der Funktion 'indizes_berechnen'
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
        zahlen_indizes = indizes_berechnen()
        ergebnis = dezimal_berechnen(zahlen_indizes)
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
