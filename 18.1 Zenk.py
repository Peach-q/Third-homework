def print_shrug_smile():
    print("¯\_(ツ)_/¯")

def print_ktulhu_smile():
    print("{:€")

def print_happy_smile():
    print("(͡° ͜ʖ ͡°)")

for i in range(3):
    case = input("Введите название функции\n")
    if case == "print_shrug_smile()":
        print_shrug_smile()
    elif case == "print_ktulhu_smile()":
        print_ktulhu_smile()
    elif case == "print_happy_smile()":
        print_happy_smile()