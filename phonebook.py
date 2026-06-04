import json

def add_contact(name, number):
    contact = {"name": name, "number": number}
    contact_json = json.dumps(contact)
    pbook.write(contact_json + "\n")
    print("Contact added successfully.")

def view_contacts():
    for line in pbook:
        contact = json.loads(line.strip())
        print(f"Name: {contact['name']}, Number: {contact['number']}")



#__main__
while True:
    print("Phonebook Application")
    print("1. Add Contact")
    print("2. Exit")
    choice = input("Enter your choice: ")

    choices = ["1", "2", "3"]
    if choice in choices:
        pbook = open("phonebook.txt", "a")
        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contact(name, number)
        elif choice == "3":
            view_contacts()
        elif choice not in :
            print("Exiting the application.")
            break
        pbook.close()

    else:
        print("Invalid choice. Please try again.")