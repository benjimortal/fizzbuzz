def vowels_to_upper(text):
    vowels = "aeiouy"
    newstr = ""
    for i in text:
        if i in vowels:
            newstr += i.upper()
        else:
            newstr += i
    return newstr

def main():
    print(vowels_to_upper("hey, my name is jawid"))


if __name__ == '__main__':
    main()