import add_cont

def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['Phone'] == phone:
            confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.pop(i)
                add_cont.save_contacts(contacts)
                print("Contact deleted successfully!")
                return
            else:
                print("Deletion cancelled.")
                return
    print("Contact not found.")
