def say_hello(first_name, second_name):
    print("Hallo " + first_name + " und " + second_name + ".")

def say_bye(first_name, second_name):
    print("Bis bald " + first_name + " und " + second_name + "!")

def counter(numb_1, numb_2):
    for count in range(numb_1, numb_2):
        print(count)

def maximum(a, b):
    if a < b:
        return b
    elif a == b:
        return a
    else:
        return b
