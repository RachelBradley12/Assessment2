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
        contactsfile = open("contactlist.csv", "w+")
        file_contents = contactsfile.read()
        if len(file_contents) == 0:
            print("Phone Book is empty")
        else:
            print(file_contents)
        #contactsfile.close
        end = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "2":
        addContact()
    elif choice == "3":
        search_existing()




def addContact():

    readContacts = open("contactlist.csv", "r+")
    list_of_contacts = []
    for line in readContacts:
        stripped_line = line.strip()
        line_list = stripped_line.split(', ')
        list_of_contacts.append(line_list)

    Name = input("Name: ")
    Address = input("Address: ")
    Number = input("Number: ")
    Birthday = input("Birthday: ")

    list_of_contacts.append(Name + ", " + Address + ", " + Number + ", " + Birthday)

    with open("contactlist.csv", "w+") as f:
        for item in list_of_contacts:
            f.write("%s\n" % item)

    addAnother()


def addAnother():
    another = input("\nWould you like to add another contact? (Y or N) ")
    if another == 'Y':
        addContact()
    elif another == 'N':
        show_main_menu()




def search_existing():
    # This function searches for an existing contact and displays the result
    choice = int(input("Enter search criteria\n\n\
1. Name\n2. Address\n3. Number\n4. Birthday\n\n\
Please enter: "))
    # We're doing so just to ensure that the user experiences a customized search result

    if choice == 1:
        search_name = str(input("Please enter the name of the contact you wish to search: "))
        rem_name = str(choice[1:])
        first_char = choice[0]
        search_name = first_char.upper() + rem_name
        contactsfile = open("contactlist.csv", 'r+')
        file_contents = contactsfile.readlines()

        found = False
        for line in file_contents:
            if search_name in line:
                print("Your Required Contact Record is:" + search_name)
                print(line)
                found = True
                break
        if found == False:
            print("There's no contact Record in Phone Book with name = " + search_name)



show_main_menu()
