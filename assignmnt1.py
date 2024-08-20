#create a phonebook

dict={}
while True:
    a=int(input(" \n1.Add \n2.View \n3.Add/Update \n4.Delete \n5.Exit \n Enter the choice:"))
    if a==1:
        print("Add")
        b={}
        name=input("Enter the name:")
        if name in dict:
          print("This contact already exists.")
          continue
   
        address=input("Enter the address:")
    
        num=int(input("How many numbers do you want to add as phone number:"))
        list=[]
        for i in range(num):
          phone=input("Enter the phone number:")
          list.append(phone)
        
        email=int(input("How many emails do you want to add:"))
        list1=[]
        for i in range(email):
          mail=input("Enter the email:")
          list1.append(mail)

        
        b["name"]=name
        b["address"]=address
        b["phone"]=list
        b["email"]=list1
        dict[name]=b
        
        f=open("phonebook.txt","w")
        f.write(str(dict))
        f.close()



    elif a==2:
     print(dict)
    elif a==3:
       name=input("enter the name you want to update:")
       if name in dict:
        print("\n1. Update address \n2.Update name \n3.  Update phone number \n4. Update email  ")
        choice = int(input("Enter the choice: "))

        if choice == 1:
            new_address = input("Enter the new address: ")
            dict[name]["address"] = new_address
        elif choice==2:
            new_name = input("Enter the new name: ")
            dict[name]["name"] = new_name 
            

        elif choice == 3:
            print("\n1.Add phone number \n2.Update phone number")
            choice1=int(input("Enter your choice:"))
            if choice1==1:
                num = int(input("How many phone numbers do you want to add: "))
                new_phones = dict[name]["phone"]
                for i in range(num):
                    phone = input("Enter the new phone number: ")
                    new_phones.append(phone)
                dict[name]["phone"] = new_phones
            elif choice1==2:
               position=int(input("Enter the position:"))
               updnum=int(input("Enter the number:"))
               dict[name]["phone"][position] =updnum
                
        elif choice == 4:
            print("\n1.Add Email \n2.Update Email")
            choice1=int(input("Enter your choice:"))
            if choice1==1:
                email = int(input("How many emails do you want to add: "))
                new_emails = dict[name]["email"]
                for i in range(email):
                    email = input("Enter the new email: ")
                    new_emails.append(email)
                dict[name]["email"] = new_emails
            elif choice1==2:
               position=int(input("Enter the position:"))
               updemail=input("Enter the email:")
               dict[name]["email"][position] =updemail

    elif a==4:
        name = input("Enter the name  to delete: ")
        if name in dict:
            del dict[name]
        else:
           print("name not found")
    
    elif a == 5:
        print("Exit")
        break
