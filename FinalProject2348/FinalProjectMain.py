#Joseph Morris
#1840300

#import csv so I can work with reading/writing and opening files
import csv
#import the datetime module so I can find out todays date, and work with dates in my files
from datetime import datetime
from datetime import date
#Create a variable holding todays date in it
today_date = date.today()

#My function to open csvs
def open_csv(users_file):
    #Create a product details list so that I can append all rows from the csv file in it
    product_details_list = []
    #using 'with open' so after the file is read it will close
    with open(users_file, mode='r') as my_list:
        contents_of_my_list = csv.reader(my_list)
        #loop through the rows in the csv than append them to product_details_list
        for items in contents_of_my_list:
            product_details_list.append(items)
    #return the list so that I can work with the values in the future
    return product_details_list

#function to combine the manufacturer list, and price list
def combine_manufacturer_list_and_price_list(list_one, list_two):
    #For each list inside list one
    for i in range(len(list_one)):
        # print("outer loop:", i)
        #for each list inside list two
        for j in range(len(list_two)):
            # print("Inner loop:", j)
            #If the first index of the list one matches the first index of list two
            try:
                if list_one[i][0] == list_two[j][0]:
                #Take the value at index one of list two
                    element_to_add = list_two[j][1]
                #and insert it in index three of list one
                    list_one[i].insert(3, element_to_add)
                    # print(list_one)
                    # print(True)
                    # print(list_one[i][0], list_two[j][0], True)
                #else do nothing
                else:
                    pass
                    # print(False)
                #but except the error and state out of bounds
            except IndexError:
                print("Index was out of bounds so continue")
    #return list so I can work with values in future
    return list_one

#Now that manuf list and product list are combines I want to combine manufacturer and service dates list
def combine_mp_list_and_service_dates_list(list_one, list_two):
    #For each row in list one
    for i in range(len(list_one)):
        # print("outer loop:", i)
        #for each list in list two
        for j in range(len(list_two)):
            # print("Inner loop:", j)
            try:
                #If list one index zero matches list two index 0
                if list_one[i][0] == list_two[j][0]:
                    #add index 1 of list two
                    element_to_add = list_two[j][1]
                    #to the 4 index of list one
                    list_one[i].insert(4, element_to_add)
                    # print(list_one)
                    # print(True)
                    # print(list_one[i][0], list_two[j][0], True)
                else:
                    pass
                    # print(False)
            #except the error if the lists are of different sizes.
            except IndexError:
                print("Index was out of bounds so continue")
    #return the list so that I can use it in the future as a value
    return list_one

#Writing items to inventory based on the product type
def write_item_types_to_inventory_csv(users_file):
    #for each item in inventory
    for i in range(len(users_file)):
        #create a list to add the inventory into
        my_list = []
        #for each item in list two
        for j in range(len(users_file)):
            #if the item at index two is not empty and the value at index two matches the rest of index two in the same list
            if users_file[i][2] != '' and users_file[i][2] == users_file[j][2]:
                #with open the with the name being the value at index two
                 with open(users_file[i][2].capitalize() + 'Inventory.csv', 'w') as seperated_inventory:
                     #create a writer so I can write the files
                    create_type_of_inventory_list_csv = csv.writer(seperated_inventory)
                    #append to my_list
                    my_list.append(users_file[j])
                    #only want to write rows of matching types into the same file
                     #write the   rows of my list to their own individual csv based on the same types
                    create_type_of_inventory_list_csv.writerows(my_list)

#Create a past service date function using todays_date global variable to compare the service date to
def past_service_date_inventory(my_dates):
    #create a service date list
    service_date_list = []
    #create a past service date list
    past_service_date_full_inventory = []

    for i in range(len(my_dates)):
        #Take the value in index four of the list
        string = my_dates[i][4]
        #split them using / as the seperator
        split_string = string.split("/")
        #append them to the service date list (This will give me three values)
        service_date_list.append(split_string)
        #since the values are currently in string I need to typecast to int
        day = int(service_date_list[i][1])
        month = int(service_date_list[i][0])
        year = int(service_date_list[i][2])
        #Once typecasted to int type I need to input in a DATE object so I can compare with the todays_date object
        service_date = date(year, month, day)
        #If service date is before todays date
        if service_date < today_date:
            #Append to past service date full inventory list
            past_service_date_full_inventory.append(my_dates[i])
            with open('PastServiceDateList.csv', 'w') as past_service_dates:
                create_full_inventory_csv = csv.writer(past_service_dates)
                #Once all values are in past service date list then write that list to a csv file called Past service date list
                create_full_inventory_csv.writerows(past_service_date_full_inventory)
            #print("Service {} has expired because todays date {}".format(service_date, today_date))
            #Return the value so that I am able to use it in the future
    return past_service_date_full_inventory

#Find damaged inventory and sort by most expensive function
def sort_inventory_by_most_expensive(user_file):
    #Create damaged list
    damaged_list = []
    #Iterate through the list and convert in all lists the value at index 3 to an int since it is a string
    for i in range(len(user_file)):
        #Type cast to int
        converting_price = int(user_file[i][3])
        #Take the new int value and place back into index 3
        user_file[i][3] = converting_price
        #Using a lambda function sort by index 3
    user_file.sort(key=lambda user_file: user_file[3])
    #since sorting sort from lowest to highest I reverse the list to sort from highest to lowest
    user_file.reverse()
    #Iterate through the list
    for i in range(len(user_file)):
        #print("the row is {} ".format(user_file[i]))
        #If there is a value in index five then append to damaged list
        if user_file[i][5] != "":
            damaged_list.append(user_file[i])
            with open('DamagedInventory.csv', 'w') as damaged_inventory:
                create_full_inventory_csv = csv.writer(damaged_inventory)
                #Write all rows in damaged list to a csv called Damaged inventory
                create_full_inventory_csv.writerows(damaged_list)
    #Return the list for future use
    return damaged_list

#Find inventory based on inventory list, and a sentence from the user
def finding_inventory(inventory_list, what_user_wants):
    #create is in inventory list
    is_in_inventory = []
    #split up the sentence of what the user wants into a list
    user_item = what_user_wants.split()
    #iterate through the list
    for i in range(len(inventory_list)):
        #Set a count variable to 0
        count = 0
        #iterate through the sentence the user stated
        for j in user_item:
            #if any of the words are in the inventory list
            if j in inventory_list[i]:
                # print("The word {} is found in list: {} ".format(j, full_inventory_list[i]))
                #increment count
                count += 1
                #if count equals two
                if count == 2:
                    #I want to append that inventory value in the list to is_in_inventory list
                    #print(inventory_list[i])
                    is_in_inventory.append(inventory_list[i])
    #Return list so I can manipulate it later
    return is_in_inventory

#
# def test_function(user_file):
#     service_date_new_list = []
#     for i in range(len(user_file)):
#         string = user_file[i][4]
#         split_string = string.split("/")
#         service_date_new_list.append(split_string)
#         day = int(service_date_new_list[i][1])
#         month = int(service_date_new_list[i][0])
#         year = int(service_date_new_list[i][2])
#         service_date = date(year, month, day)
#
#     if len(user_file) == 0:
#         print("There is no such item in inventory")
#     else:
#         for i in range(len(user_file)):
#             if user_file[i][5] != "" or service_date < today_date:
#                 print("Item is damaged or past service date", user_file)
#             else:
#                 for i in range(len(user_file)):
#                     converting_price = int(user_file[i][3])
#                     user_file[i][3] = converting_price
#                 user_file.sort(key=lambda user_file: user_file[3])
#                 # is_inventory_available.reverse()
#
#                 for i in range(len(user_file)):
#                     str_value = str(user_file[i][3])
#                     user_file[i].insert(3, str_value)
#                     user_file[i].remove(user_file[i][4])
#                     string = convert_list_to_string("", str(user_file))
#         print("Your item is: ", " ".join(user_file[i][0:4]))

#Convert list to string function
def convert_list_to_string(seperator, input):
    #input a list and a seperator
    #Example " ".join([my_list])
    return seperator.join(input)


if __name__ == '__main__':

    #Place manufacturers list in a variable
    starting_manufactures_list = open_csv("ManufacturerList.csv")
    # Place Price list in a variable
    starting_price_list = open_csv("PriceList.csv")
    # Place service dates list in a variable
    starting_service_dates_list = open_csv("ServiceDatesList.csv")

    #combine both the manufacturer_list_and_price_list
    manufacturer_and_price_list = combine_manufacturer_list_and_price_list(starting_manufactures_list, starting_price_list)

    #combine both the combine_mp_list_and_service_dates_list
    #once this two are combined the 3 files will now be in a list with all three csv files called full inventory list
    full_inventory_list = combine_mp_list_and_service_dates_list(
        manufacturer_and_price_list, starting_service_dates_list)

#1
    #sory the full inventory based on manufacturer name which is in the first index
    full_inventory_list.sort(key=lambda full_inventory_list: full_inventory_list[1])
    # create FullInventory.csv file  sorted by manufacturer
    #write all rows in full inventory to a csv called full inventory
    with open('FullInventory.csv', 'w') as full_inventory:
        create_full_inventory_csv = csv.writer(full_inventory)
        create_full_inventory_csv.writerows(full_inventory_list)

#2
    #Sort list by item id
    full_inventory_list.sort(key=lambda full_inventory_list: full_inventory_list[0])
    # write item types to each seperate csv based on their manufacturer name
    write_item_types_to_inventory_csv(full_inventory_list)

#3
    #I had to strip time to get the date and then I sorted from oldest to newest service dates
    full_inventory_list.sort(key=lambda full_inventory_list: datetime.strptime(full_inventory_list[4], "%m/%d/%Y"))
    past_service = past_service_date_inventory(full_inventory_list)
    past_service

#4
    #I used sort_inventory_by_most_expensive which takes in my full inventory
    #sorts by most expensive and then creates a damaged csv if anything is in index 5 of the full inventory list
    sort_inventory_by_most_expensive_and_create_damaged_csv = sort_inventory_by_most_expensive(full_inventory_list)
    sort_inventory_by_most_expensive_and_create_damaged_csv
#Test

#1B
#initialize the user input to a blank string
what_user_wants = ''
#If user inputs 'q' the while loop will quit
while what_user_wants != 'q':
    #Ask the user what item they would like to look for and give them some examples
    what_user_wants = input("\nPlease write a sentence telling me the manufacturer and item type you\n"
            "would like to check for in our inventory:\n\n"
            "When you are finish searching for an item please enter 'q' for quit.\n\n")
    # "\nThe manufacturing companies to choose from are: \n1. Apple \n2. Dell \n3. Lenova \n4. Samsung\n\n"
    # "The item types in inventory are: \n1. phone\n2. laptop\n3. tower  \n")
    #If the user inputs 'q' break out of the while loop and do not ask if the user would like to search for anything else
    if what_user_wants == 'q':
        break
    else:
        #Else find what the user asked for and compare it to our list of invetory
        #place this in is_inventory_available variable
        is_inventory_available = finding_inventory(full_inventory_list,
                                                       what_user_wants)

        #create a service date list
        service_date_new_list = []
        #iterate through the is inventory available list
        for i in range(len(is_inventory_available)):
            #add the value in the fourth index to a variable called string
            string = is_inventory_available[i][4]
            #split at /
            split_string = string.split("/")
            #append those values into service date new list
            service_date_new_list.append(split_string)
            #type cast those values into int
            day = int(service_date_new_list[i][1])
            month = int(service_date_new_list[i][0])
            year = int(service_date_new_list[i][2])
            #create a date object so I can compare with todays_date object
            service_date = date(year, month, day)
        #Create available inventory list
        available_inventory = []
        #iterate through the is in inventory list
        for i in range(len(is_inventory_available)):
            #if there is a value in index 5 or service date is before todays date
            if is_inventory_available[i][5] != "" or service_date < today_date:
                #then the item is either damaged or past its service date and should not be shown
                #print("Item is damaged or past service date", is_inventory_available)
                break
                #if the item is not damaged or past service date then append it to available inventory list
            else:
                available_inventory.append(is_inventory_available[i])
        #If len of available inventory list is 0 than the item they were looking for is not in inventory
        if len(available_inventory) == 0:
            print("The item you search for is not in inventory")
        #else sort by price and reverse to have the most expensive be in the first index of the list of lists
        else:
            #sort by price
            available_inventory.sort(key=lambda available_inventory: available_inventory[3])
            #reverse the sort so that the most expensive item is on top
            available_inventory.reverse()
            #print(available_inventory)
            #After it is sorted by most expensive
            #Convert that value back to a string
            str_value = str(available_inventory[0][3])
            #Insert the string value in at postion 3 of the first list[0][3]
            available_inventory[0].insert(3, str_value)
            #Remove the integer value
            available_inventory[0].remove(available_inventory[0][4])
            #Convert my list to a string so that I can input everything in list 0 from 0-4 index as a string
            string = convert_list_to_string("", str(available_inventory))
            #print out your item is (user reponse)
            print("Your item is: ", " ".join(available_inventory[0][0:4]))

