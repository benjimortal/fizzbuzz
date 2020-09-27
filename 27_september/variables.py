def main():
    number1 = ""  #vi skappar en tom träng
    number2 = ""  #vi skappar en tom träng
    while not number1.isdigit() or not number2.isdigit(): # så länge som inte  number1 eller number2  innehåller numeriska värden då skriv koden under
        number1 = input("Enter value 1: ")
        number2 = input("Enter value 2: ")

    #number1 och number2 är strängar med bara numeriska värden

    number1 = int(number1)
    number2 = int(number2)
    result = number1 + number2
    print(result)


if __name__ == '__main__':
    main()
