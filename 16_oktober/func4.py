def translate(text):
    vowels = "a e i o u y "
    robberStr = ""
    for c in text:
        if c not in vowels and c.isalpha():
            robberStr += c + "o" + c
        else:
            robberStr += c
    return robberStr


def main():
    print(translate("hello, this is jawid. and i am 24 years old"))


if __name__ == '__main__':
    main()
