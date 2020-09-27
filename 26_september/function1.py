
def greet(name, age):  # age och name är parametrar för def greet
    print("Hello", name.title())
    print("You are", age, "years old")


def main():
    greet("Jawid", 24) #jawid och 24 är argument, två st argumenter
    greet("Lisa", 23)


if __name__ == '__main__':
    main()
