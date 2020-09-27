value = 10


def non_pure_function():
    global value
    value += 1
    return value + a


def main():
    print(non_pure_function(2))
    print(non_pure_function(2))
    print(non_pure_function(2))
    print(non_pure_function(2))

if __name__ == '__main__':
    main()
