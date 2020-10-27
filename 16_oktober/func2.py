def my_len(list):
    counter = 0
    for x in list:
        counter += 1
    return counter


def main():
    my_list =([1, 2, 3, 4, 5, 6, 7, "Jawid ba Reyhane is ment to be"])
    print(my_len(my_list))
    my_set = {1, 2, 3, 4, 5, 6, 7, "Jawid ba Reyhane is ment to be"}
    print(my_len(my_set))
    my_str = "1, 2, 3, 4, 5, 6, 7, Jawid ba Reyhane is ment to be"
    print(my_len(my_str))



if __name__ == '__main__':
    main()
