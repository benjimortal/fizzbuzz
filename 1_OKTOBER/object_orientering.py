class Person:
    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def jump(self):
        print(self.firstname, "is jumping")




def main():
    p1 = Person("Anna", "Svensson", "anna@gmal.com")
    p2 = Person("Pelle", "Karlsson", "pelle@gmail.com")

    p1.jump()
    p2.jump()



if __name__ == '__main__':
    main()
