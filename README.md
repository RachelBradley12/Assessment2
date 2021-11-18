# Assessment2
### Overview:
This application was made with the purpose of storing names, addresses, phone numbers and birthdays of contacts in
the form of a contacts book. I have created my system as a Command Line Interface (CLI), the computer will display a
prompt, and the user will key in the command and presses enter or return. The user will be able to view a full list of
contacts stored in the contacts book, add a new contact, search for the details of an existing contact, make changes to
contacts and remove any chosen contact.

### Assumptions made:
1. Firstly, when deciding on the details which should be stored in my contacts book, I decided to store each contact's
full name as one string, instead of storing first name and last name as separate strings. This choice was made off the
assumption that when searching for contacts there is a possibility that two contacts could have the same first name or
the same first name. This would cause confusion in the system. However, it is very unlikely that two people in a
persons contacts book will have the exact same full name. 

2. When inputting contact details such as name and address, it must be assumed that the user will be careless with
case sensitivity. To solve this issue, I have included the function .title() after every name and address input.

3. Furthermore, when adding a new contact, I must again assume user carelessness. I have made my system so that whenever
the user inputs a new contacts birthday, it performs a validation process to ensure that the contact's DOB is a valid
date, insuring data integrity.

4. 
