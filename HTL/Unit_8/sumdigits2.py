"""
author: Lukas Sanz
file: sumdigits2.py
catnr: 1BHIF-24
"""


ziffernsumme = 0
try:
    zahl = input("Ganze Zahl: ")
    if zahl[0] == "-":
        zahl = zahl.replace("-", "")
        for ziffer in zahl:
            ziffernsumme += int(ziffer)
        print(f"Die Ziffernsumme von -{zahl} lautet {ziffernsumme}")

    elif zahl[0] != "-":
        for ziffer in zahl:
            ziffernsumme += int(ziffer)
        print(f"Die Ziffernsumme von {zahl} lautet {ziffernsumme}")

    else:
        print("Du hast keine gültige Zahl eingegeben!")

except BaseException as Error:
    print(f"Fehler im Programm!\nFehlermeldung: {Error}")

finally:
    exit("Programm beendet..")