import csv
import os

FILENAME = "contacts.csv"
FIELDNAMES = ["Name", "Email", "Phone", "Address"]

def load_contacts():
    contacts = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                contacts.append(row)
    return contacts

def save_contacts(contacts):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(contacts)
