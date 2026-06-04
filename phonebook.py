import csv
import os

FILENAME = "phonebook.csv"

def add_contact(name, number):
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, number])
    print("Contact added successfully.")

def view_contacts():
    if not os.path.exists(FILENAME):
        print("No contacts found.")
        return

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        has_contacts = False
        for row in reader:
            print(f"Name: {row[0]}, Number: {row[1]}")
            has_contacts = True
        
        if not has_contacts:
            print("No contacts found.")

def edit_contact(target_name):
    if not os.path.exists(FILENAME):
        print("No contacts found.")
        return

    with open(FILENAME, "r") as file:
        rows = list(csv.reader(file))

    contact_found = False
    for row in rows:
        if row and row[0].lower() == target_name.lower():
            row[1] = input(f"Enter new number for {row[0]}: ")
            contact_found = True
            break

    if not contact_found:
        print("Contact not found.")
        return

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        
    print("Contact updated successfully.")

def search_contact(target_name):
    if not os.path.exists(FILENAME):
        print("No contacts found.")
        return

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0].lower().startswith(target_name.lower()) or row[0].split()[1].lower().startswith(target_name.lower()) or row[1].lower().startswith(target_name.lower()):
                print(f"Name: {row[0]}, Number: {row[1]}")

def delete_contact(target_name):
    if not os.path.exists(FILENAME):
        print("No contacts found.")
        return

    with open(FILENAME, "r") as file:
        rows = list(csv.reader(file))

    new_rows = [row for row in rows if row and row[0].lower() != target_name.lower()]

    if len(new_rows) == len(rows):
        print("Contact not found.")
        return

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)
        
    print("Contact deleted successfully.")


# Menu loop
while True:
    print("\n--- Phonebook (CSV Mode) ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Search Contact")
    print("5. Delete Contact")
    print("9. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_contact(input("Name: "), input("Number: "))
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        edit_contact(input("Enter name to edit: "))
    elif choice == "4":
        search_contact(input("Enter name to search: "))
    elif choice == "5":
        delete_contact(input("Enter name to delete: "))
    elif choice == "9":
        break