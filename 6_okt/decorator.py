def modify(func):
    def inner(name):
        return "<<<" + func(name) + ">>>"
    return inner


def produce(name):
    return f"Hello {name}"


def a(n):
    x = 10 + n
    def b():
        print(x)
    return b

def main():
    f = a(5)
    #result = produce("Bill")
    #print(result)
    f()


if __name__ == '__main__':
    main()
