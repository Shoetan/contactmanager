#import the database functions module
import db_functions

#create a simple user menu
USER_CHOICE  = """
ENTER : 
A 'to add a contact'
C 'to get cell number'
H 'to get home address'
D 'to delete contact'
Q 'to quit program'

Please select Operation : 
"""

#list to store all the details of the contact
con_list = []

#create a function to display the text based user menu
def menu():
    print(USER_CHOICE)
    
# calling the user menu function
menu()

#asking user for desired operation
operation_choice = input()

#this code block will execute when the user has selected a operation
while operation_choice != "Q":
    #create table if the table alredy exists it will not create the table again for the second time
    db_functions.create_table()
    
    if operation_choice == "A":
        #create the table using the create table function or method
        
        #call function to receive contact details from user to insert into the database
        db_functions.add_details()
    elif operation_choice == "C":
        db_functions.get_cell()
        
    elif operation_choice == "H":
        db_functions.get_home()
        
    elif operation_choice =="D":
        db_functions.delete_details() 
    else:
        pass
    
    menu()
    operation_choice = input()

else:
    print("Thanks for using this program ")
        
    