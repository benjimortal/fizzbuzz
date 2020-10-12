def main():
    file = open("textfile.txt", "w") #w: betyder write
    file.write("Hej hej \n") #\n gör en radbryttning,
    file.write("Bye \n")
    file.close()

    with open("textfile.txt", "a") as file:  #a: betyder ppend, lägg till sist i den här filen
        file.write("Hepp\n")
        file.write("Hopp\n")


if __name__ == '__main__':
    main()
