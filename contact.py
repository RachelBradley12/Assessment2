import re
import datetime

class Contact:

    def __innit__(self, name, address, number, birthday):
         self.name = name
         self.address = address
         self.number = number
         self.birthday = birthday


def show_main_menu():
    ''' Show main menu for Phone Book Program '''
    print("\n*** Phone Book Menu ***\n"+

          "------------------------------------------\n"+
          "Enter 1,2,3, or 4:\n"+
          "Enter 1 To Display Your Contacts Records\n" +
          "Enter 2 To Add a New Contact Record\n"+
          "Enter 3 To Search your Contacts\n"+
          "Enter 4 To Make Changes to your Contacts\n"+
          "Enter 5 To Remove a Contact\n**********************")
    choice = input("Enter your choice: ")
    if choice == "1":
        display_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        search_existing()
    elif choice == "4":
        change_details()
    elif choice == "5":
        remove_contact()
    else:
        print("Error!\nPlease enter either numbers 1, 2, 3, 4, or 5")
        show_main_menu()



def display_contacts():
    contactsfile = open("contactList.txt", "r+")
    file_contents = contactsfile.read()
    if len(file_contents) == 0:
        print("Phone Book is empty")
    else:
        print("Name:, Address:, Number:, Birthday:")
        print(file_contents)
    input("Press Enter to return to Main Menu ...")
    show_main_menu()


def add_contact():
    # This function writes the user inputs for each contact detail and write it into the text file
    readContacts = open("contactList.txt", "r+")
    list_of_contacts = []
    for line in readContacts:
        list_of_contacts.append(line)

    print("Please enter the following details below:")
    Name = input("Full Name: ").title()
    Address = input("Address: ").title()
    Number = input("Phone Number: ")
    Birthday = input("Birthday (DD/MM/YYYY): ")

    day, month, year = Birthday.split('/')

    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False

    if (isValidDate == True):

        if Name != "" and Address != "" and Number != "" and Birthday != "":
            list_of_contacts.append(Name + ", " + Address + ", " + Number + ", " + Birthday + "\n")
            with open("contactList.txt", "w+") as f:
                for line in list_of_contacts:
                    f.write("".join(line))
        elif Name == "":
            empty_error()
        elif any(char.isdigit() for char in Name):
            print("\nError! Names cannot contain digits!")
            input("Please press Enter to try again...")
        elif Address == "":
            empty_error()
        elif Number == "":
            empty_error()
        elif Birthday == "":
            empty_error()
    else:
        print("\nError! Input date is not valid..")

    add_another()

def empty_error():
    print("\nError! You cannot leave a field empty")
    input("Please press Enter to try again...")

def add_another():
    # This function asks the user if they would like to add another contact
    another = input("\nWould you like to add another contact? (Y or N) ")
    if another == 'Y':
        add_contact()
    elif another == 'N':
        show_main_menu()
    else:
        print("\nInvalid input!")
        input("Please press Enter to return to the Main Menu and try again...")



def search_existing():
    # This function searches for an existing contact and displays the result
    choice = int(input("Enter search criteria\n\n\
Name: 1\nAddress: 2\nPhone Number: 3\nBirthday: 4\n\n\
Please enter: "))
    # We're doing so just to ensure that the user experiences a customized search result

    if choice == 1:
        # This will execute for searches based on contact name
        searched_name = str(input("Please enter the name of the contact you wish to search: ")).title()
        contactsfile = open("contactList.txt", "r+")

        # setting flag to 0
        flag = 0

        # Loop through the file line by line
        for line in contactsfile:

            # checking exact string is present in line or not
            if re.search(r"\b{}\b".format(searched_name),line):
                flag = 1
                break

        # checking condition for string found or not
        if flag == 0:
            print("Contact Name, ", searched_name, ", Not Found in Contacts Book")
        else:
            print("Contact Name, ", searched_name, ", Found!")
            print(line)
        # closing text file
        contactsfile.close()


    elif choice == 2:
        # This will execute for searches based on contact address
        searched_address = str(input("Please enter the address of the contact you wish to search: ")).title()
        contactsfile = open("contactList.txt", "r+")

        # setting flag to 0
        flag = 0

        # Loop through the file line by line
        for line in contactsfile:

            # checking exact string is present in line or not
            if re.search(r"\b{}\b".format(searched_address),line):
                flag = 1
                break

        # checking condition for string found or not
        if flag == 0:
            print("Contact Address, ", searched_address, ", Not Found in Contacts Book")
        else:
            print("Contact Address, ", searched_address, ", Found!")
            print(line)
        # closing text file
        contactsfile.close()


    elif choice == 3:
        # This will execute for searches based on contact phone number
        searched_number = str(input("Please enter the phone number of the contact you wish to search: "))
        contactsfile = open("contactList.txt", "r+")

        # setting flag to 0
        flag = 0

        # Loop through the file line by line
        for line in contactsfile:

            # checking exact string is present in line or not
            if re.search(r"\b{}\b".format(searched_number),line):
                flag = 1
                break

        # checking condition for string found or not
        if flag == 0:
            print("Contact Phone Number, ", searched_number, ", Not Found in Contacts Book")
        else:
            print("Contact Phone Number, ", searched_number, ", Found!")
            print(line)
        # closing text file
        contactsfile.close()

    elif choice == 4:
        # This will execute for searches based on contact phone number
        searched_birthday = str(input("Please enter the birthday of the contact you wish to search: "))
        contactsfile = open("contactList.txt", "r+")

        # setting flag to 0
        flag = 0

        # Loop through the file line by line
        for line in contactsfile:

            # checking exact string is present in line or not
            if re.search(r"\b{}\b".format(searched_birthday),line):
                flag = 1
                break

        # checking condition for string found or not
        if flag == 0:
            print("Contact with Birthday, ", searched_birthday, ", Not Found in Contacts Book")
        else:
            print("Contact with Birthday, ", searched_birthday, ", Found!")
            print(line)
        # closing text file
        contactsfile.close()

    else:
        print("Error!\nPlease enter either numbers 1, 2, 3, or 4\nPlease Return to Main Menu and Try Again. . . . .")
        show_main_menu()

    input("Press Enter to return to Main Menu ...")
    show_main_menu()


def change_details():
    with open('contactList.txt') as f:
        contact_data = f.read().splitlines()
        searched_name = str(input("Enter the Name of the Contact whose details you wish to change: ")).title()

        iterate_list = []
        for contact in contact_data:
            contact = contact.split(", ")
            iterate_list.append(contact)

        for contact in iterate_list:
            if searched_name in contact:
                detail_to_change = input("\nWhat details  do you wish to change of this contact?\n\nName: 1\nAddress: 2\nPhone Number: 3\nBirthday (DD/MM/YYYY): 4\n\nPlease enter: ")

                print(contact)

                if detail_to_change == "1":
                    contact[0] = input("\nChange " + contact[0] + " to what?:  ").title()
                elif detail_to_change == "2":
                    contact[1] = input("\nChange " + contact[1] + " to what?:  ").title()
                elif detail_to_change == "3":
                    contact[2] = input("\nChange " + contact[2] + " to what?:  ")
                elif detail_to_change == "4":
                    contact[3] = input("\nChange " + contact[3] + " to what?:  ")


        for x in iterate_list:
            print(*x)

    with open("contactList.txt", "w+") as f:
        for list in iterate_list:
            f.write(str(", ".join(list)) + '\n')


    input("\nChange made successfully ...\nPress Enter to return to Main Menu ...")
    show_main_menu()



def remove_contact():
    with open("contactList.txt", "r") as f:
        lines = f.readlines()
        print(lines)
        name_to_remove = input("Please enter the name of the contact who you wish to remove: ").title()

    contactsfile = open("contactList.txt", "r+")

    # setting flag to 0
    flag = 0

    # Loop through the file line by line
    for line in contactsfile:

        # checking exact string is present in line or not
        if re.search(r"\b{}\b".format(name_to_remove), line):
            flag = 1
            break

    # checking condition for string found or not
    if flag == 0:
        print("Contact, ", name_to_remove, ", Not Found in Contacts Book")
        input("\nPress Enter to return to Main Menu ...")
        show_main_menu()
    else:
        print("Contact, ", name_to_remove, ", Found!")
        with open("contactList.txt", "w") as f:
            for line in lines:
                if (line.split(",")[0])!= name_to_remove:
                    f.write(line)
                    print("\nContact removed successfully! ...\nPress Enter to return to Main Menu ...")

    # closing text file
    contactsfile.close()
    show_main_menu()


show_main_menu()
