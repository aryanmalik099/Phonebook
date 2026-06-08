import csv

FILENAME = "phonebook.csv"

def add_contact(name, number):
    try:
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, number])
        print("Contact added successfully.")
    except Exception as error:
        print(f"Error adding contact: {error}")

def view_contacts():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            has_contacts = False
            for row in reader:
                if len(row) >= 2:
                    print(f"Name: {row[0]}, Number: {row[1]}")
                    has_contacts = True

            if not has_contacts:
                print("No contacts found.")
    except FileNotFoundError:
        print("No contacts found.")
    except Exception as error:
        print(f"Error reading contacts: {error}")

def edit_contact(target_name):
    try:
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
    except FileNotFoundError:
        print("No contacts found.")
    except Exception as error:
        print(f"Error updating contact: {error}")

def search_contact(target_name):
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) < 2:
                    continue

                name_parts = row[0].split()
                second_part_matches = len(name_parts) > 1 and name_parts[1].lower().startswith(target_name.lower())

                if row[0].lower().startswith(target_name.lower()) or second_part_matches or row[1].lower().startswith(target_name.lower()):
                    print(f"Name: {row[0]}, Number: {row[1]}")
    except FileNotFoundError:
        print("No contacts found.")
    except Exception as error:
        print(f"Error searching contacts: {error}")

def delete_contact(target_name):
    try:
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
    except FileNotFoundError:
        print("No contacts found.")
    except Exception as error:
        print(f"Error deleting contact: {error}")


# Menu loop
while True:
    print("\n--- Phonebook ---")
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
    else:
        print("Invalid choice. Please try again.")