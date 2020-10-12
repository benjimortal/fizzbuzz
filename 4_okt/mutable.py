def main():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]

    list3 = [4, 5, 6]
    list4 = list3.copy()

    print(id(list1))
    print(id(list2))

    print(id(list3))
    print(id(list4))

if __name__ == '__main__':
    main()
