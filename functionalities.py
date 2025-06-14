from file_handler import save_contacts

def add_contact(contacts):
    try:
        name = input("Enter Name: ")
        if not name.replace(" ", "").isalpha():
            raise ValueError("Name must be letters only.")

        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")
        if not phone.isdigit():
            raise ValueError("Phone number must be digits only.")

        # duplicate phone numbers
        for contact in contacts:
            if contact["Phone"] == phone:
                print("Phone number already exists.")
                return contacts

        address = input("Enter Address: ")

        contact = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Address": address
        }

        contacts.append(contact)
        save_contacts(contacts)
        print("Contact added successfully.")

    except ValueError as e:
        print(e)
    return contacts


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\n Contact List:")

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['Name']}, Email: {contact['Email']}, "
              f"Phone: {contact['Phone']}, Address: {contact['Address']}")
        

def remove_contact(contacts):
    phone = input("Enter phone number of contact to remove: ")
    for contact in contacts:
        if contact["Phone"] == phone:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact removed.")
            return contacts
    print("No contact with that phone number found.")
    return contacts

def search_contacts(contacts):
    keyword = input("Enter name, email, or phone to search: ").lower()
    found = False
    for contact in contacts:
        if (keyword in contact["Name"].lower() or
            keyword in contact["Email"].lower() or
            keyword in contact["Phone"]):
            print(f"Found: {contact}")
            found = True
    if not found:
        print("No matching contact found.")
