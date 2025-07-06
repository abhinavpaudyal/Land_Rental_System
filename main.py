from datetime import datetime
from read import *  # Importing functions for reading data
from operations import *  # Importing functions for operations
from write import *  # Importing function for write

# Name, Address, Email
print("*" * 150)
print("\n\n")
print(" Name: Techno Property Nepal".center(100))
print("Address: Naxal, Kathmandu".center(100))
print("Email: technoprop@gmail.com".center(100))
print("*" * 150)

# calling functions from read. It reads land data from file
read_land_data()
print("kita number\t\tPlace\t\t\t\tface\t\t\tAnna\t\t\tPrice\t\t\tAvailability")  # Header for land data
print()
print_land_data()  # prints land data form read file
print("*" * 150)

# Main loop
main_loop = True
while main_loop==True:
    print(" 1. For renting ")
    print(" 2. For returning")
    print(" 3. For exit ")
    # choice between 1,2,3
    try:
        u_input = int(input(" Enter your choice: "))
    except Value8Error:
        print("Invalid input. Please enter a number.")
        continue

    # For renting
    if u_input == 1:
        name = input("Enter your name: ")  # for user name
        while True:
            phone_number = input("Enter your contact number: ")  # user contact details
            if not phone_number.isdigit():
                print("Enter digit")
                continue
            else:
                break
        bill, sel_item = renting(name, phone_number)  # calling renting function form operations
        
        rent_update(l_data)  # After renting is done by the user it updates the data
        print("It's rented!!")

    # For returning
    elif u_input == 2:
        name_1 = input("Enter your name: ")#user name
        while True:
            phone_number_1 = input("Enter your contact number: ")
            if not phone_number_1.isdigit():
                print("Enter digit")
                continue
            else:
                break
        bill = returning(name_1, phone_number_1)  # calling renting functions from
        
        return_update(l_data)  # After the land is returned it updates the data
        print("Thank you for returning")

    # Exiting from loop
    elif u_input == 3:
        main_loop = False
        print("Exited")

print("*" * 80)
