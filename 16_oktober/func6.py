def revers(in_str):
    new_str = ""
    for i in range(len(in_str)- 1, -1, -1):
        new_str += in_str [i]

    return new_str


def main():
    print(revers("I am testing"))


if __name__ == '__main__':
    main()
