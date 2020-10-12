def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))


def main():
    print(recur_fibo(3))
    print(recur_fibo(4))
    print(recur_fibo(6))
    print(recur_fibo(8))
    print(recur_fibo(9))


if __name__ == '__main__':
    main()
