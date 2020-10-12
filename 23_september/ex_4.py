import time

def recur_fibo(n, mem={}):
    if n <= 1:
        return n
    else:
        if n - 1 in mem:  # om n-1 finns i dictonary
            n1 = mem[n - 1]
        else:
            n1 = recur_fibo(n - 1)  # annars lägg till den till i dictionary
            mem[n - 1] = n1

        if n - 2 in mem:
            n2 = mem[n - 2]
        else:
            n2 = recur_fibo(n - 2)
            mem[n - 2] = n2
        return n1 + n2


def recur_fibo2(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo2(n-1) + recur_fibo2(n-2))


def main():
    start = time.time()
    print(recur_fibo(40))
    end = time.time()
    print(f"It took {end-start} seconds")

    start = time.time()
    print(recur_fibo2(40))
    end = time.time()
    print(f"It took {end - start} seconds")


if __name__ == '__main__':
    main()
