
class Info:
    def phone(self):
        self.num=int(input("How many phone numbers u want to add:" ))
        self.num_list=[ ]
        for i in range(self.num):
            a=int(input("Enter the phone number:"))
            self.num_list.append(a)
        print(  self.num_list)
    def  email(self):
        self.mail=int(input("How many emails u want to add:" ))
        self.mail_list=[ ]
        for i in range(self.mail):
            b=input("Enter the email address:")
            self.mail_list.append(b)
        print(self.mail_list)
f=Info()
f.phone()
f.email()
