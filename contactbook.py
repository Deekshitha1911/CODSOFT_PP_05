# Contact Book Application

contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    print("Contact added successfully!")


def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts available.")
        return

    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")


def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone number to search: ")

    found = False
    for contact in contacts:
        if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break

    if not found:
        print("No matching contact found.")


def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\nEnter new details (leave blank to keep current value):")
            new_name = input(f"New Name ({contact['name']}): ") or contact["name"]
            new_phone = input(f"New Phone ({contact['phone']}): ") or contact["phone"]
            new_email = input(f"New Email ({contact['email']}): ") or contact["email"]
            new_address = input(f"New Address ({contact['address']}): ") or contact["address"]

            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email
            contact["address"] = new_address

            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


# Main Program Loop
while True:
    print("\n===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
