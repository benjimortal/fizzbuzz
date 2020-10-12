def main():
    values = [2, 3, 4, 5, 6]
    result = [value * 2 for value in values] #resuktatet av det vad jag gör här ska bli en lista.
    print(result)

    result = [value for value in values if value % 2 == 0]
    print(result)

    name = "Jaiwd"
    result = [str(value) + i for value in values for i in name]
    print(result)


if __name__ == '__main__':
    main()


#den här metoden är mer för python