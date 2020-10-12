def exp(a, b):
    if b == 0:
        return 1
    return a * exp(a, b-1)


def main():
    print(exp(2, 3))
    print(exp(3, 2))

if __name__ == '__main__':
    main()
