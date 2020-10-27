import random
import time
def bubble_sort(sequence):
    swapped = True
    while swapped:
        swapped = False
        stop_value = len(sequence)- 1
        for i in range(len(sequence)-1):
            if sequence[i] > sequence[i+1]:
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
                swapped = True
        stop_value -= 1
        print(sequence)
    return sequence

def main():
    values = []
    for _ in range(100):
        values.append(random.randrange(1, 10))
        start = time.time()

    """for i in values:
        values.sort()
    print(values)"""
    values = bubble_sort(values)
    end = time.time()
    print(f"it took {end-start} second")


if __name__ == '__main__':
    main()
