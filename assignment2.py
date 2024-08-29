class Info:
    def phone(self):
        self.num_list = []
        while True:
            num = int(input("Enter the phone number: "))
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
            "Emails": self.emails }  
        print(Detail.book)                                               
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

