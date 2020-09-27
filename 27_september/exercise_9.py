def main():
    word = "hello"
    vowel = "aeiouy"

    for letter in word:
        if letter in vowel:
            print(letter.upper(), end="")  #end = "" gör att koden skrives på en rad
        else:
            print(letter, end="")


if __name__ == '__main__':
    main()
