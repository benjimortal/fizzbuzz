def main():
    notes = {"1" : "Gerge Washington",
              "2" : "Thomas Jefferson",
              "5" : "Abraham Lincoln",
              "10" : "Alexander Hamilton",
              "20" : "Abdrew Jackson",
              "50" : "Ulysses S.Grant",
              "100" : "Benjamin Franklin"}  #Make a dictionary
    value = input("Please enter the value of an US dollar note: ")
    if value not in notes:
        print("Sorry that is not a valid US dollar note")
    else:
        print(f"On that not you will finde, {notes[value]}")



if __name__ == '__main__':
    main()
