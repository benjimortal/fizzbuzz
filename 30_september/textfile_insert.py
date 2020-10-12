import os

def main():
    with open("textfile.tmp", "w") as outfile:
        for i, line in enumerate(open("textfile.txt", "r")):
            if i == 1:
                outfile.write(line)
                outfile.write("Jawid\n")
            else:
                outfile.write(line)

    os.remove("textfile.txt")
    os.rename("textfile.tmp", "textfile.txt")


if __name__ == '__main__':
    main()
