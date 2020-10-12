def greeting(greeter, name):
    return f"{greeter()} {name}"


def yo():
    return "Yo"


def hi():
    return "Hi"


def main():
    result = greeting(yo, "Bob")
    print(result)
    result = greeting(hi, "Alice")
    print(result)


if __name__ == '__main__':
    main()
