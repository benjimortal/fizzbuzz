def func(x):
    return x * 2

def main():
    values = [2, 3, 4, 5, 6]

    result = map(func, values)
    result = list(result)
    print(result)




if __name__ == '__main__':
    main()
