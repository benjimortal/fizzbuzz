def main():
    vowels = "aeiouy"
    char = input("Enter a character :")
    #Make sure that the character that is passed in is lower case so it can be found in the vowels string
    if char.lower() in vowels:
        print(f"is a vowel {char}")
    else:
        print(f"is not a vowel {char}")


if __name__ == '__main__':
    main()
