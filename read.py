l_data = {}  # initialize empty dictionary
#Function to read land data from file 
def read_land_data():
    file = open("land.txt", "r")
    for line in file:
        line = line.replace("\n", "")#Removin newline character
        line = line.split(",")
        land_list = []
        for i in range(1, len(line)):
            land_list.append(line[i].replace("\n", ""))#Append land details to list
        l_data[line[0]] = land_list#Add land details to dictionary
    file.close()#Closing file 


#Function to print land data details that is stored in dictionart
def print_land_data():
    for key, value in l_data.items():
        print(key, end="\t\t\t")
        for item in value:
            print(item, end="\t\t\t")#Printing the each land detail
        print("\n")#Printing newline character





