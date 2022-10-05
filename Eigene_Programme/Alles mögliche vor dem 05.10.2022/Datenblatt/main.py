print("Hey, Ich bin hier, um deine Daten zu sammeln. Bist du damit einverstanden? ")
q1 = input("(Ja/Nein) : ")
if q1 == "Ja":
    print("Gut, machen wir weiter. Gib bitte folgende Daten an: ")
    name1 = input("Vorname: ")
    name2 = input("Nachname: ")
    job = input("Beruf: ")
    age = input("Alter: ")
    sex = input("Geschlecht: ")
    q2 = input("Sind die Daten korrekt? (Ja/Nein): ")
elif q1 == "Nein":
    print("Okay, dann wünsche ich dir noch einen schönen Tag.")
    quit()
if q2 == "Ja":
    print()
else:
    while q2 == "Nein":
        print("Okay, gib deine Daten bitte erneut ein: ")
        name1 = input("Vorname: ")
        name2 = input("Nachname: ")
        job = input("Beruf: ")
        age = input("Alter: ")
        sex = input("Geschlecht: ")
        q2 = input("Sind die Daten jetzt korrekt? (Ja/Nein): ")
print("So.. Ich habe die Daten notiert, du kannst sie jederzeit abrufen.")
q3 = input("Möchtest du deine Daten abrufen? (Ja/Nein): ")
if q3 == "Ja":
    print(
        "Dein Name ist " + name1 + " " + name2 + ", " + sex + ", du arbeitest derzeit als " + job + " und bist " + age + " Jahre alt.")
else:
    print("Okay, bis bald!")