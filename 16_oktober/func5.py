def sum(inlist):
    result = 0
    for i in inlist:
        result += i
    return result

def multiply(inlist):
    result =  10000
    for i in inlist:
        result *= i
    return result

def main():
    print(sum([1, 2, 3, 4]))
    print(multiply([1, 2, 3, 4]))


if __name__ == '__main__':
    main()
