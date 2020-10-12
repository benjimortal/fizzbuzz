def func(x):
    if x % 2 == 0:
        return True
    return False


def main():
    values = [2, 3, 4, 5, 6]
    result = filter(func, values)

    result = list(result)
    print(result)


if __name__ == '__main__':
    main()
