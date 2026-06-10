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
    