import add_cont,load_cont,remove_cont,search_cont,view_cont
def main():
    print("WElcome to the contact BOOK cli")
    print ("Loading contacts form the consts ")
    contacts = load_cont.load_contacts()    
    print("Done!")
contacts = load_cont.load_contacts()

while(True):
    print("\n--------- Main Menu ---------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    choice= input("Enter your choice :")
    
    if(choice =='1'):
        add_cont.add_contact(contacts)
    elif(choice =='2'):
        view_cont.view_contacts(contacts)
    elif(choice =='3'):
        search_cont.search_contact(contacts)
    elif(choice=='4'):
        remove_cont.remove_contact(contacts)
    elif(choice =='5'):
        print("Thanks for usign the Contact Book CLI system !")
        break
    else:
        print("Enter valid input between 1 to 5")