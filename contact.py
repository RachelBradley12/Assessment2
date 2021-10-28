class Contact:

     def __innit__(self, name, address, number, birthday):
         self.name = name
         self.address = address
         self.number = number
         self.birthday = birthday

def addContact():
    Name = input("Name: ")
    Address = input("Address: ")
    Number = input("Number: ")
    Birthday = input("Birthday: ")
    with open("contacts.txt", 'w+') as contacts:
        contacts.write('{}, {}, {}, {}'.format(Name, Address, Number, Birthday))

addContact()





