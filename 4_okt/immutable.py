def main():
    x = 20
    y = 20

    print(id(x))
    print(id(y))

    x += 1
    print(id(x))
    print(id(y))

    str1 = "hej"
    str2 = "hej"
    print(id(str1))
    print(id(str2))

    str2 += "i"
    print(id(str1))
    print(id(str2))

if __name__ == '__main__':
    main()
