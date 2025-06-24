def save_contacts(contacts):
    with open('data.txt', mode='w') as file:
        for contact in contacts:
            line = f"{contact['Name']}|{contact['Phone']}|{contact['Email']}|{contact['Address']}\n"
            file.write(line)

def add_contact(contacts):
    name = input("Enter Name: ")
    if name.strip() == '' or name.isdigit():
        print("Error: The contact’s name must be a non-numeric string.")
        return
    phone = input("Enter Phone Number: ")
    if not phone.isdigit() or len(phone)!=11 :
        print("Error: The phone number must be an integer and 11 digit.")
        return
    email = input("Enter Email: ")
    if '@' not in email or '.' not in email:
        print("Error: The email must contain '@' and domain name like '.com'.")
        return
    
    address = input("Enter Address: ")
    if address.strip() == '':
        print("Error: Address cannot be empty.")
        return

    for contact in contacts:
        if contact['Phone'] == phone:
            print("Error: Phone number already exists for another contact.")
            return
        elif contact['Email'] == email:
            print("Error: This already exists for another contact.")
            return

    contacts.append({
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address
    })
    save_contacts(contacts)
    print("Contact added successfully!")