def main():
    str1 = "Hej"
    str2 = "Hopp"
    str3 = "Tja"


    result = str1 + str2 + str3 # det här är lättare att förstå
    print(result)

    result = " ".join([str1, str2,str1])  # det är bättre och effektivare sätt
    print(result)

if __name__ == '__main__':
    main()
