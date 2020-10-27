def max(first, second, third):
    """if first > second and third:
        return first
    elif second > therd:
        return second
    else:
        return third"""

    #or you could code like that
    if first > second and first > third:
        return  first
    elif second > third:
        return second
    else:
        return third

def main():
    biggest = max(10, 16, 15)
    print(biggest)


if __name__ == '__main__':
    main()
