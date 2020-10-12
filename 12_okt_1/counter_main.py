import my_map
from my_map import add as adder


def add(a, b):
    return a + b + 10


def main():
    result = my_map.add(3, 4)
    print(result)
    result = add(3, 4)
    print(result)
    result = my_map.sub(3, 4)
    print(result)
    result = my_map.mul(3, 4)
    print(result)
    result = my_map.div(3, 4)
    print(result)


if __name__ == '__main__':
    main()
