"""Phonebook Application with a menu-driven interface. The user can add, remove, 
search, and display contacts."""
phonebook = []
while True:
    print("Menu" \
    "\n1. Add a contact" \
    "\n2. Remove a contact" \
    "\n3. Search for a contact" \
    "\n4. Display all contacts" \
    "\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email address: ")
        contact = {"name": name, "phone": phone, "email": email}
        phonebook.append(contact)
        print("Contact added successfully.")
    elif choice == "2":
        name = input("Enter the name of the contact to remove: ")
        for contact in phonebook:
            if contact["name"] == name:
                phonebook.remove(contact)
                print("Contact removed successfully.")
                break
        else:
            print("Contact not found.")
    elif choice == "3":
        name = input("Enter the name of the contact to search for: ")
        for contact in phonebook:
            if contact["name"] == name:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                break
        else:
            print("Contact not found.")
    elif choice == "4":
        if phonebook:
            print("All Contacts:")
            for contact in phonebook:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("Phonebook is empty.")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")