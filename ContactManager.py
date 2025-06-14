from file_handler import load_contacts
from functionalities import (
    add_contact,
    view_contacts,
    remove_contact,
    search_contacts
)


contacts = load_contacts()

while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            contacts = add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            contacts = remove_contact(contacts)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

