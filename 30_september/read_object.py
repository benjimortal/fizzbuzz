import pickle
from person import Person
def main():

    with open("persons.dat", "rb") as person_file:
        p1 = pickle.load(person_file)
        p2 = pickle.load(person_file)

    print(p1.name, p1.age)
    print(p2.name, p2.age)



if __name__ == '__main__':
    main()
