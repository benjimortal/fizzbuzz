def func1(value):
    value += 1
    print(value)

def func2(sequence):
    sequence.append("Hossein")
    print(sequence)

def main():
    x = 10
    func1(x)
    print(x)


    names = ["Jawid", "Marielle", "Mohammad", "Reyhaneh"]
    func2(names.copy())
    print(names)


if __name__ == '__main__':
    main()
