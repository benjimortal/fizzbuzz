import sqlite3

#connect to database
connection = sqlite3.connect('customer.db')

#create a cursor
cursor = connection.cursor()

#create a Table
cursor.execute("""CREATE TABLE customers ()
""")

def main():
    pass


if __name__ == '__main__':
    main()
