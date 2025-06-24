# with open(file='data.txt',mode='r') as file:
#     for line in file:
#         print(line)
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("===== All Contacts =====")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. Name : {contact['Name']}")
        print(f"   Phone : {contact['Phone']}")
        print(f"   Email : {contact['Email']}")
        print(f"   Address: {contact['Address']}\n")
