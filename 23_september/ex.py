def exp(a, b):
    if b == 0:
        return 1
    return a * exp(a, b-1)
# 2^3 = 2* 2^3-1
# 2^2 = 2*2^2-1
# 2^1 = 2
# 2^2 = 2*2
# 2^3 = 2*2*2


def main():
    print(2**3)
    print(3**2)
    print(exp(2, 3))
    print(exp(3, 2))


if __name__ == '__main__':
    main()
