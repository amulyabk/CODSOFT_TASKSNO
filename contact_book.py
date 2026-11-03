
contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\n===== CONTACT LIST =====")
            for i, contact in enumerate(contacts, 1):
                print(f"\nContact {i}")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])

    elif choice == "3":
        search = input("Enter name or phone number: ").lower()

        found = False

        for contact in contacts:
            if (search in contact["name"].lower()
                or search in contact["phone"]):

                print("\nContact Found!")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "4":
        search = input("Enter name to update: ").lower()
        found = False

        for contact in contacts:
            if contact["name"].lower() == search:
                print("Enter new details:")

                contact["name"] = input("New name: ")
                contact["phone"] = input("New phone: ")
                contact["email"] = input("New email: ")
                contact["address"] = input("New address: ")

                print("Contact updated successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "5":
        search = input("Enter name to delete: ").lower()
        found = False

        for contact in contacts:
            if contact["name"].lower() == search:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Try again.")
