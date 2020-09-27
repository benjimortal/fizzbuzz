def main():
    values = [2, 3, 4, 5, 6]
    result = [value * 2 for value in values]
    print(result)

    result = [value * 2 for value in values if value % 2 == 0]
    print(result)

    name = "Jawid"
    result = [str(value) + c for value in values for c in name]
    print(result)

    result = []
    for value in values:
        for c in name:
            result.append(str(value) + c)


if __name__ == '__main__':
    main()
