print("Anfang des Programms")
age = input("Gib dein  Alter ein: ")
name = input("Gib deinen Namen ein: ")
print("Du heißt " + name + " und bist derzeit " + age + " Jahre alt, ist das richtig?")
yn = input("""Gib "yes" oder "no" ein: """)

if yn == "yes":
    print("Super!")
elif yn == "no":
    while yn == "no":
        age = input("Gib dein  Alter ein: ")
        name = input("Gib deinen Namen ein: ")
        print("Du heißt " + name + " und bist derzeit " + age + " Jahre alt, ist das richtig?")
        yn = input("""Gib "yes" oder "no" ein: """)

        if yn == "yes":
            print("Super!")
print("Ende des Programms")