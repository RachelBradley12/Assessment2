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
          "Enter 3 To search your contacts\n"+
          "Enter 4 To Quit\n**********************")
    choice = input("Enter your choice: ")
    if choice == "1":
        displayContacts()
    elif choice == "2":
        addContact()
    elif choice == "3":
        search_existing()



def displayContacts():
    contactsfile = open("contactList.txt", "r+")
    file_contents = contactsfile.read()
    if len(file_contents) == 0:
        print("Phone Book is empty")
    else:
        print(file_contents)
    input("Press Enter to return to Main Menu ...")
    show_main_menu()



def addContact():
    # This function writes the user inputs for each contact detail and write it into the text file
    readContacts = open("contactList.txt", "r+")
    list_of_contacts = []
    for line in readContacts:
        list_of_contacts.append(line)

    print("Please enter the following details below:")
    Name = input("Full Name: ")
    Address = input("Address: ")
    Number = input("Phone Number: ")
    Birthday = input("Birthday (DD/MM/YYYY): ")

    list_of_contacts.append(Name + ", " + Address + ", " + Number + ", " + Birthday + "\n")

    with open("contactList.txt", "w+") as f:
        for line in list_of_contacts:
            f.write("".join(line))

    addAnother()


def addAnother():
    # This function asks the user if they would like to add another contact
    another = input("\nWould you like to add another contact? (Y or N) ")
    if another == 'Y':
        addContact()
    elif another == 'N':
        show_main_menu()




def search_existing():
    # This function searches for an existing contact and displays the result
    choice = int(input("Enter search criteria\n\n\
Name: 1\nAddress: 2\nPhone Number: 3\nBirthday: 4\n\n\
Please enter: "))
    # We're doing so just to ensure that the user experiences a customized search result

    if choice == 1:
        # This will execute for searches based on contact name
        searched_name = str(input("Please enter the name of the contact you wish to search: "))
        contactsfile = open("contactList.txt", "r+")

        # setting flag to 0
        flag = 0

        # Loop through the file line by line
        for line in contactsfile:

            # checking string is present in line or not
            if searched_name in line:
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
        searched_address = str(input("Please enter the address of the contact you wish to search: "))
        contactsfile = open("contactList.txt", "r+")

        # setting flag to 0
        flag = 0

        # Loop through the file line by line
        for line in contactsfile:

            # checking string is present in line or not
            if searched_address in line:
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

            # checking string is present in line or not
            if searched_number in line:
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

            # checking string is present in line or not
            if searched_birthday in line:
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

    input("Press Enter to return to Main Menu ...")
    show_main_menu()



show_main_menu()
