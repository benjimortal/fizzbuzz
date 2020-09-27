def main():
    more = True
    while more:
        answer = input("More? y/n ")
        more = not answer.lower() == "n"
        #if answer.lower() == "n":
        #   more = False

    number = 10000

    while True:
        number = number / 3
        if number < 100:
            print("Jag är klar, number är nu", number)
            break
        print(number)
    print("Klar")

if __name__ == '__main__':
    main()
