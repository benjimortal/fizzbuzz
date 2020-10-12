def get_input():
    value = input("Enter a value")
    if value == 'True' or value == 'False':
        return bool(value)
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


def main():
    pass


if __name__ == '__main__':
    main()
