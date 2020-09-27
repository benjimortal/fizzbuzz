def main():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        if i == 42:
            print("Here is the lucky number!")
        else:
            print(i)




if __name__ == '__main__':
    main()
