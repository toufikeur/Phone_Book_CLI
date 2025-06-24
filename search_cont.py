def search_contact(contacts):
    term = input("Enter search term (name/email/phone): ").lower()
    found = False
    for contact in contacts:
        if term in contact['Name'].lower() or term in contact['Email'].lower() or term in contact['Phone']:
            print("Search Result:")
            print(f"Name : {contact['Name']}")
            print(f"Phone : {contact['Phone']}")
            print(f"Email : {contact['Email']}")
            print(f"Address: {contact['Address']}")
            found = True
    if not found:
        print("No matching contact found.")
