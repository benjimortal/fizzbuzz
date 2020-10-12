def main():
    with open("textfile.txt", "r") as file: # r: betyder read
        text = file.readlines() #readlines tar fram hela texten i filen som fins.
        """for line in text:
            # print(line, end="") den gör att print inte lägga extra mellanslag
            line = line.strip() #strip tar bort extra withespaces till höger om texten
            print(line)"""

        with open("textfile.txt", "r") as file:
            line = file.readline()
            print(line.strip())
            line = file.readline()
            print(line.strip())

        print("___________________")
        for line in open("textfile.txt", "r"):
            print(line.strip())

if __name__ == '__main__':
    main()