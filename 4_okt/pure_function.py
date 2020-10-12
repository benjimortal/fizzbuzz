value = 10


def non_purefunction(a):
    global value
    value += 1
    return value + a


def purefunction(a):
    return 10 + a


def main():
    print(non_purefunction(2))
    print(non_purefunction(2))
    print(non_purefunction(2))
    print(non_purefunction(2))

    print(purefunction(2))
    print(purefunction(2))
    print(purefunction(2))
    print(purefunction(2))



if __name__ == '__main__':
    main()
