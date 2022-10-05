"""
author: Lukas Sanz
file: hörtest.py
catnr: 1BHIF-24
"""


### Bibliotheken
import winsound as ws
from threading import Thread


### Funktionen
def ton_erzeugen():
    global frequenz
    while frequenz < 20000:
        ws.Beep(frequenz, 600)
        frequenz += 200

### Hauptprogramm
if __name__ == "__main__":
    global frequenz
    # noinspection PyRedeclaration
    frequenz = 5000

    thread = Thread(target=ton_erzeugen)
    thread.daemon = True
    thread.start()
    input("""Drücke Enter, sobald du nichts mehr hörst!
: """)
    print(f"Du hast den Ton bei {frequenz / 1000} kHz noch gehört.")
    if frequenz >= 19000:
        print("Deine Ohren sind somit unter 15 Jahre alt.")
    elif 17000 <= frequenz < 19000:
        print("Deine Ohren sind somit unter 20 Jahre alt.")
    elif 16000 <= frequenz < 17000:
        print("Deine Ohren sind somit unter 25 Jahre alt.")
    elif 15000 <= frequenz < 16000:
        print("Deine Ohren sind somit unter 30 Jahre alt.")
    elif 12000 <= frequenz < 15000:
        print("Deine Ohren sind somit unter 40 Jahre alt.")
    elif 8000 <= frequenz < 12000:
        print("Deine Ohren sind somit unter 50 Jahre alt.")
    else:
        print("Du hast vermutlich einen Hörschaden oder bist über 50 Jahre alt.")