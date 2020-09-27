def avg(sequence):
    return sum(sequence) / len(sequence)

def main():
    numbers = [4, 7, 9, 2, 4, 8, 16, 24, 15]
    result = avg(numbers)
    print(result)

    values = (34, 6, 18, 7)
    result = avg(values)
    print(result)

if __name__ == '__main__':
    main()
