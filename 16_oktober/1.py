def main():
    my_list = [12, 15, 32, 42, 55, 75, 122, 150, 180, 200]
    for item in my_list:
        if item > 150:
            break
        if item % 5 == 0:
            print(item)


if __name__ == '__main__':
    main()
