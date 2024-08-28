
class Info:
    def __init__(self):
        self.num_list = []
        self.mail_list = []

    def phone(self):
        self.num=int(input("How many phone numbers u want to add:" ))
        # self.num_list=[ ]
        for i in range(self.num):
            a=int(input("Enter the phone number:"))
            self.num_list.append(a)
        print(  self.num_list)
    def  email(self):
        self.mail=int(input("How many emails u want to add:" ))
        # self.mail_list=[ ]
        for i in range(self.mail):
            b=input("Enter the email address:")
            self.mail_list.append(b)
        print(self.mail_list)
# f=Info()
# f.phone()
# f.email()
class Detail:
    def name(self):
        self.nam =input("Enter the name:")
        self.address =input("Enter the address:")

    def view(self,info):
        print("name", self.nam)
        print("address",  self.address )
        print("phone number", info.num_list)
        print("Email",info.mail_list) 
f=Info()
f.phone()
f.email()
ff=Detail()
ff.name()  
print("details:")
ff.view(f)

