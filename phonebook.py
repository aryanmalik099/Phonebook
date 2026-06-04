import json
import os

def add_contact(name, number):
    contact = {"name": name, "number": number}
    
    with open("phonebook.jsonl", "a") as file:
        file.write(json.dumps(contact) + "\n")
    
    print("Contact added successfully.")

def view_contacts():
    if not os.path.exists("phonebook.jsonl"):
        print("No contacts found.")
        return

    with open("phonebook.jsonl", "r") as file:
        for line in file:
            if line.strip():
                contact = json.loads(line)
                print(f"Name: {contact['name']}, Number: {contact['number']}")



#__main__
while True:
    print("Phonebook Application")
    print("1. Add Contact")
    print("2. View Contacts")
    print("9. Exit")
    choice = input("Enter your choice: ")

    choices = ["1", "2", "9"]

    if choice in choices:
        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contact(name, number)
        elif choice == "2":
            view_contacts()
        elif choice == "9":
            print("Exiting the application.")
            break

    else:
        print("Invalid choice. Please try again.")