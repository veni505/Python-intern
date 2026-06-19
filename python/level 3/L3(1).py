message=""
password=""
while True:
    print("\n1.Sender")
    print("\n2.Receiver")
    print("\n3.Exit")
    choice=input("\n Enter choice:")
    if choice=="1":
        message=input("\nEnter Your Message:")
        password=input("\nSet Password:")
        print("\n\nMessage Stored Sucessfully")
        print("\nEncrypted Message:********")
    elif choice=="2":
        entered_password=input("\n Enter Password:")
        if entered_password == password:
            print("\n\nAccess Granted")
            print("\nMessage::",message)
        else:
            print("\n\nACCESS DENIED! WRONG Password")
    elif choice=="3":
        print("Program Exited....")
        break
    else:
        print("Invalid Choice")
