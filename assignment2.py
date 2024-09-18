class Info:
    def phone(self):
        self.num_list = []
        while True:
            num = input("Enter the phone number: ")
            self.num_list.append(num)
            cho = input("Add another phone number? Type 'Y' or 'N': ").lower()
            if cho == 'n':
                break
        return self.num_list
    
    def email(self):
        self.mail_list = []
        while True:
            mail = input("Enter the Email address: ")
            self.mail_list.append(mail)
            cho = input("Add another Email address? Type 'Y' or 'N': ").lower()
            if cho == 'n':
                break
        return self.mail_list
    

class Detail:
    book = {}
    
    def __init__(self, name, address, mail_list, num_list):
        self.name = name
        self.address = address
        self.emails = mail_list
        self.numbers = num_list
        Detail.book[self.name] = {
            "Name": self.name,
            "Address": self.address,
            "Phone Numbers": self.numbers,
            "Emails": self.emails
        }
       
    
    def update(self):
        v = input("Enter the name you want to update: ")
        if v in Detail.book:
            ch = int(input("\n1. Update name\n2. Update address\n3. Update phone number\n4. Update email address\nEnter your choice: "))
            if ch == 1:
                new_name = input("Enter the new name: ")
                Detail.book[new_name] = Detail.book.pop(v)  
                Detail.book[new_name]["Name"] = new_name  
                print(f"Contact updated to new name: {Detail.book[new_name]}")
            elif ch == 2:
                new_address = input("Enter the new address: ")
                Detail.book[v]["Address"] = new_address
                print(f"Address updated: {Detail.book[v]}")
            elif ch == 3:
                print("\n1. Add phone number\n2. Update phone number")
                choice1 = int(input("Enter your choice: "))
                if choice1 == 1:
                    new_phone = input("Enter the new phone number: ")
                    Detail.book[v]["Phone Numbers"].append(new_phone)
                    print(f"Phone number added: {Detail.book[v]}")
                elif choice1 == 2:
                    position = int(input("Enter the position to update : "))
                    if 0 <= position < len(Detail.book[v]["Phone Numbers"]):
                        updnum = input("Enter the new number: ")
                        Detail.book[v]["Phone Numbers"][position] = updnum
                        print(f"Phone number updated: {Detail.book[v]}")
                    else:
                        print("Invalid position.")
            elif ch == 4:
                new_email = input("Enter the new email address: ")
                Detail.book[v]["Emails"].append(new_email)
                print(f"Email added: {Detail.book[v]}")
        else:
            print("Contact not found.")

    def delete(self):
        name = input("Enter the name of the contact to delete: ")
        if name in Detail.book:
            del Detail.book[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print("Contact not found.")

    def view_contact(self):
        name = input("Enter the name to view contact details: ")
        if name in Detail.book:
            print(Detail.book[name])
        else:
            print("Contact not found.")

    def view_all_contacts(self):
        if Detail.book:
            for contact in Detail.book.values():
                print(contact)
        else:
            print("No contacts available.")


while True:
    choice = int(input("\n1. Create a contact\n2. Update a contact\n3. Delete a contact\n4. View a contact\n5. View all contacts\n6. Exit\nEnter your choice: "))
    
    if choice == 1:
        name = input("Enter the name: ")
        address = input("Enter the address: ")
        f = Info()
        numbers = f.phone()
        emails = f.email()
        contact = Detail(name, address, emails, numbers)
        print("Contact created successfully.")

    elif choice == 2:
        detail = Detail("", "", [], [])  
        detail.update()

    elif choice == 3:
        detail = Detail("", "", [], [])  
        detail.delete()

    elif choice == 4:
        detail = Detail("", "", [], [])  
        detail.view_contact()

    elif choice == 5:
        detail = Detail("", "", [], [])  
        detail.view_all_contacts()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
