from datetime import datetime#Importing from datetime

#Function for updating land data after renting it is called in main file
def rent_update(l_data):
    with open("land.txt", "w") as file:
        #writing each entry to file for renting
        for key, value in l_data.items():
            file.write(key + "," + ",".join(value) + "\n")
#Function for updating the land data after renting .it is called in main file 
def return_update(l_data):
    with open("land.txt", "w") as file:
        #writing each entry to file for returning 
        for key, value in l_data.items():
            file.write(key + "," + ",".join(value) + "\n")

#Function to generate bill for renting
def generate_bill_file(bill, name, phone_number):
    if not bill:#Here bill is  variable and it check  wether it is empty 
        return
    
    todays_date_and_time = datetime.now()
    year = todays_date_and_time.year
    month = todays_date_and_time.month
    day = todays_date_and_time.day
    hour = todays_date_and_time.hour
    minute = todays_date_and_time.minute
    second = todays_date_and_time.second
    
#Generating unique file name for renting 
    unique = str(todays_date_and_time.year) + str(todays_date_and_time.month) + str(
        todays_date_and_time.day) + str(todays_date_and_time.hour) + str(
        todays_date_and_time.minute) + str(todays_date_and_time.second)
    filename = "rent" + unique + "_" + name + ".txt"
    
#Writing format for rental bill details
    
    with open(filename, "w") as rent_bill:
        rent_bill.write("\n")
        rent_bill.write("*" *180+"\n")
        rent_bill.write(" " *70  + "Techno Property Nepal" + "\n")
        rent_bill.write("\n")
        rent_bill.write(" " *70+ "Naxal,Kathmandu" + "\n")
        rent_bill.write(" " * 35 + "Contact: " + "9854558585" + "\n")
        rent_bill.write(" " * 35 + "Email: technoprop@gmail.com" + "\n")
    #For costumer information
        rent_bill.write("\n")
        rent_bill.write("Rent Bill"+"*"*50 + "\n")
        rent_bill.write("*" * 100 + "\n\n")
        rent_bill.write("Customer Information:" + "\n")
        rent_bill.write("*"*100 + "\n")
        rent_bill.write("Name: " + name + "\n")
        rent_bill.write("Contact Number: " + phone_number + "\n")
        rent_bill.write("\n")
        rent_bill.write("Land Details:" + "\n")
        rent_bill.write("'"*100 + "\n")

        rent_bill.write("Land Kitta Number: " + bill[0] + "\n")
        rent_bill.write("City/District: " + str(bill[1]) + "\n")
        rent_bill.write("Direction: " + str(bill[2]) + "\n")
        rent_bill.write("Area of Land: " + str(bill[3]) + " anna\n")

        rent_bill.write("Rent Details" + "\n")
        rent_bill.write("************************************************************" + "\n")
        rent_bill.write("Rent Date: " + str(datetime.now()) + "\n")
        

        total_amount = bill[-1]
        rent_bill.write("Total Amount: NPR " + str(total_amount) + "\n")
        print("\n\n")
        



#Function to generate bill for returning
def generate_bill_file_1(bill, name_1, phone_number_1):
    if not bill:
        return
    
    todays_date_and_time = datetime.now()
    year = todays_date_and_time.year
    month = todays_date_and_time.month
    day = todays_date_and_time.day
    hour = todays_date_and_time.hour
    minute = todays_date_and_time.minute
    second = todays_date_and_time.second
    
#Generating unique file name for returning
    unique = str(todays_date_and_time.year) + str(todays_date_and_time.month) + str(
        todays_date_and_time.day) + str(todays_date_and_time.hour) + str(
        todays_date_and_time.minute) + str(todays_date_and_time.second)
    filename = "return" + unique + "_" + name_1 + ".txt"
    #Writing format for returning bill details
    with open(filename, "w") as returning_bill:
        returning_bill.write("\n")
        returning_bill.write("*" *180+"\n")
        
        returning_bill.write(" " *70  + "Techno Property Nepal" + "\n")
        returning_bill.write("\n")
        returning_bill.write(" " *70+ "Naxal, Kathmandu" + "\n")
        returning_bill.write("\n")
        returning_bill.write("*" * 35 + "Contact: " + "9854558585" + " *"*35+"\n")
        returning_bill.write("\n")
        returning_bill.write("*" * 35+ "Email: technoprop@gmail.com" + " *"*35+"\n")
        returning_bill.write("\n")
        returning_bill.write("Returning Bill" + "\n")
        returning_bill.write("*" * 160 + "\n\n")
        returning_bill.write("User Details:" + "\n")
        returning_bill.write("**************************************************" + "\n")
        returning_bill.write("Name: " + name_1 + "\n")
        returning_bill.write("Contact Number: " + phone_number_1 + "\n")
        returning_bill.write("\n")
        returning_bill.write("Land Details:" + "\n")
        returning_bill.write("*****************************************" + "\n")

        returning_bill.write("Land Kitta Number: " + bill[0] + "\n")
        returning_bill.write("Direction: " + str(bill[2]) + "\n")
        returning_bill.write("Area of Land: " + str(bill[3]) + " anna\n")

        returning_bill.write("Return Details" + "\n")
        returning_bill.write("************************************************************" + "\n")
        returning_bill.write("Rent Date: " + str(datetime.now()) + "\n")  # Write the converted string

        total_amount = bill[-1]
        returning_bill.write("Total Amount: NPR " + str(total_amount) + "\n")
        print("\n\n")
       
