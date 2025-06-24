import os

def load_contacts():
    contacts = []
    if os.path.exists('data.txt'):
        with open('data.txt', mode ='r') as file:
            for line in file:
                name, phone , email, address = line.strip().split('|')
                contacts.append({
                    'Name':name,
                    'Phone':phone,
                    'Email':email,
                    'Address':address
                })
    return contacts

