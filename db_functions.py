# import the sqlite3 module

import sqlite3

# create a connection to the sqlite3 module

con_list = []


def create_table():
    connection = sqlite3.connect("contact_database.db")

    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS condetails (first text,last text, email varchar(255),address text, cell varchar(255))"
    )

    connection.commit()

    connection.close()


def add_details():
    connection = sqlite3.connect("contact_database.db")
    cursor = connection.cursor()
    # receive details of contact from user
    con_first = input("Enter the contact fisrt name ")
    con_last = input("Enter the contact last name ")
    con_email = input("Enter contact email address ")
    con_address = input("Enter contact address ")
    con_cell = input("Enter contact cell number ")
    # add details to  list
    con_list.append(con_first)
    con_list.append(con_last)
    con_list.append(con_email)
    con_list.append(con_address)
    con_list.append(con_cell)
    cursor.execute("INSERT INTO condetails VALUES(?,?,?,?,?)", con_list)

    print("Contact details added successfully")
    connection.commit()
    connection.close()


def get_cell():
    connection = sqlite3.connect("contact_database.db")

    cursor = connection.cursor()

    con_first = input("Enter name to get cell number ")

    con_last = input("Enter last name to get correct cell number ")

    cursor.execute(
        "SELECT cell FROM condetails WHERE first = (?) AND last = (?) ",
        (con_first, con_last),
    )

    print(f"successful {cursor.fetchone()}")

    connection.commit()

    connection.close()


def get_home():
    connection = sqlite3.connect("contact_database.db")

    cursor = connection.cursor()

    con_first = input("Enter first name to get home address ")

    con_last = input("Enter last name also to get correct home address")

    cursor.execute(
        "SELECT  address FROM  condetials WHERE first  = (?) AND last = (?)",
        (con_first, con_last),
    )

    print(f"Successful {cursor.fetchone()}")

    connection.commit()

    connection.close()


def delete_details():
    connection = sqlite3.connect("contact_database.db")

    cursor = connection.cursor()

    con_first = input("Enter first name to delete details from table ")

    con_last = input("Enter Last name to confirm delete")

    cursor.execute(
    "DELETE FROM condetails WHERE first = (?) AND last = (?)", (con_first, con_last)
    )

    print("Successfully deleted")

    connection.commit()

    connection.close()