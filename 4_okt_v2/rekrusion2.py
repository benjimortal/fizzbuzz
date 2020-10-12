def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def fac_rec(n):
    if n == 1:
        return 1
    return n * fac_rec(n -1)


def main():
    print(fac_rec(3))



if __name__ == '__main__':
    main()
