# Contact Management System - Intermediate Simple Version

contacts = []  # List to store all contact dictionaries


# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contact = {"name": name, "phone": phone}
    contacts.append(contact)

    print("Contact added successfully!\n")


# Search a contact by name
def search_contact():
    name = input("Enter name to search: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\nContact Found:")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"], "\n")
            return

    print("Contact not found.\n")


# Display all saved contacts
def display_contacts():
    if not contacts:
        print("No contacts available.\n")
        return

    print("\n===== Contact List =====")
    for contact in contacts:
        print("Name :", contact["name"])
        print("Phone:", contact["phone"])
        print("------------------------")
    print()


# Main program loop
def main():
    while True:
        print("=== Contact Management System ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            display_contacts()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


# Run the program
main()
