
#Importing from datetime ,read and write
from datetime import datetime
from read import l_data
from write import *
#Defining function renting
def renting(name, phone_number):
    while True:
        land_id = input("Enter the land id: ")#For land id
        if land_id not in l_data:
            print("Invalid land ID")
            continue

        elif l_data[land_id][4] == "Not Available":#Changing availablity, the land is already rented and not available 
            print("This land is already rented.")
            continue

        while True:
            anna = input("Enter anna: ")#For anna
            if anna == l_data[land_id][2]:
                break
            else:
                print("Please enter Anna again")
        
        while True:
            try:
                """
            Here when user month is asked if the user month is greater  than 0 and smaller than 12 then
            It display message enter the month again
            """
                user_month = int(input("Enter the number of months: "))#For number of months
                if 0 < user_month < 12:
                    break
                else:
                    print("Enter the number of months again")
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        sel_item = l_data[land_id]
        sel_item[4] = "Not Available"  # Updating availability to "Not Available"
        
        bills = []  # initialize empty list for bills
        bill = [land_id] + sel_item[:5] + [name, datetime.now(), user_month, user_month * int(sel_item[3])]
        bills.append(bill)
        for bill in bills:
            print(bill)

        #Calling function
        generate_bill_file(bill, name, phone_number)

        print("\n")
        print(" " *70 + "Technoproperty Nepal" + "\n")
        print("\n")
        print(" " * 70 + "Naxal,Kathmandu" + "\n")
        print("\n")
        print(" " * 70 + "Contact: " + phone_number + "\n")
        print(" " * 70 + "Email: technoprop@gmail.com" + "\n")
        print("\n")
        print("*" * 25 + "Rent Bill"+ "*" * 25 + "\n")
        print("*" * 110 + "\n\n")
        print("Customer Information:" + "\n")
        print("Name: " + name + "\n")
        print("Contact Number: " + phone_number + "\n")
        print("\n")
        print("Land Details:" + "\n")
        print("'"*100 + "\n")
        print("Land Kitta Number: " + bill[0] + "\n")
        print("Direction: " + str(bill[2]) + "\n")
        print("Area of Land: " + str(bill[3]) + " anna\n")
        print("Rent Details" + "\n") 
        print("************************************************************" + "\n")
        print("Rent Date: " + str(datetime.now()) + "\n")  #converted string
        total_amount = bill[-1]
        print("Total Amount: NPR " + str(total_amount) + "\n")
        print("\n\n")
        
        
            # Ask the user if they want to rent more lands
        choice = input("Do you want to rent more lands? (yes/no): ").lower()
        if choice != "yes":
                 
            return bill, sel_item
        
def returning(name_1, phone_number_1):
    land_id_1 = input("Enter the land id for returning: ")
    if land_id_1 not in l_data:
        print("Invalid land ID")
        return

    sel_item = l_data[land_id_1]
    rent_1 = int(input("Enter rent month: "))  # entering renting month
    return_2 = int(input("Enter return month: "))  # entering returning month
    price = int(sel_item[3])  

    city_district = sel_item[2]  # Retrieve city/district information from sel_item
    # Calculating total price after fine  for rent 
    if return_2 > rent_1:
        late = return_2 - rent_1
        fine = 0.1
        calc = fine * late * price
        t_price = rent_1 * price + calc
        print(t_price)

    late = return_2 - rent_1
    fine = 0.1
    calc = fine * late * price
    t_price = rent_1 * price + calc

    # Update land availability to "Available"
    sel_item[4] = "Available"

    bills = []  # initialize empty list for bills
    bill = [land_id_1] + sel_item[:5] + [name_1, datetime.now(), city_district, rent_1, return_2, t_price]
    bills.append(bill)
    #calling function generate_bill_file_1
    generate_bill_file_1(bill, name_1, phone_number_1)

    for bill in bills:
        print(bill)

    
        print("\n")
        print(" " * 70 + "Technoproperty Nepal" + "\n")
        print("\n")
        print(" " * 70+ "Naxal,Kathmandu" + "\n")
        print("\n")
        print(" " * 70 + "Contact: " + phone_number_1 + "\n")
        print("\n")
        print(" " * 70 + "Email: technopro@gmail.com" + "\n")
        print("\n")
        print("*" * 25 + "Return Bill" +"*" * 25 + "\n")
        print("*" * 110 + "\n\n")
        print("Customer Information:" + "\n")
        print("**************************************************" + "\n")
        print("Name: " + name_1 + "\n")
        print("Contact Number: " + phone_number_1 + "\n")
        print("\n")
        print("Land Details:" + "\n")
        print("**********************************************" + "\n")
        print("Land Kitta Number: " + bill[0] + "\n")
        print("Direction: " + str(bill[2]) + "\n")
        print("Area of Land: " + str(bill[3]) + " anna\n")
        print("Rent Details" + "\n") 
        print("************************************************************" + "\n")
        print("Return Date: " + str(datetime.now()) + "\n")  
        #For total amount
        total_amount = bill[-1]
        print("Total Amount: NPR " + str(total_amount) + "\n")
        print("\n\n")

        

    # Ask the user if they want to return more lands
        choice = input("Do you want to return more lands? (yes/no): ").lower()
        if choice == "yes":
            returning(name_1, phone_number_1)
        else:
            return bill#returning the bill
