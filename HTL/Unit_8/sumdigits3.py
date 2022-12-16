"""
author: Lukas Sanz
file: sumdigits3.py
catnr: 1BHIF-24
"""


ziffernsumme = 0
try:
    zahl = input("Gib eine Zahl ein: ")
    zahl_output = zahl[:]
    if zahl[0] == "-":
        zahl = zahl.replace("-", "")
        if "." in zahl:
            zahl = zahl.replace(".", "")
        for ziffer in zahl:
            ziffernsumme += int(ziffer)
        print(f"Die Ziffernsumme von {zahl_output} lautet {ziffernsumme}")

    elif zahl[0] != "-":
        if "." in zahl:
            zahl = zahl.replace(".", "")
        for ziffer in zahl:
            ziffernsumme += int(ziffer)
        print(f"Die Ziffernsumme von {zahl_output} lautet {ziffernsumme}")

    else:
        print("\nDu hast keine gültige Zahl eingegeben!")

except BaseException as Error:
    print(f"\nFehler im Programm!\nFehlermeldung: {Error}")

finally:
    exit("\nProgramm beendet..")