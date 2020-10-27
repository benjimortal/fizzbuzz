def main():
    two_dice = []
    for d1 in range(1, 7):
        for d2 in range(1, 13):
            two_dice.append((d1, d2))
    print(two_dice)


    two_dice = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 13)]
    print(two_dice)
if __name__ == '__main__':
    main()
