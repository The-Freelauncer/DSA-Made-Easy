# Contact List Saver

def update(): # Updation of Contact Number
    n=0
    n=int(input("Enter the number of contacts you want to save : "))
    x=0
    if n==0:
        exit   
    if len(a)!=0: 
        x=1

    if x==1:
        phno=int(input("Enter the Contact Number : ")) # Number stored for checking
        for i in range (len(a)):
            if a[i]==phno: # Checking the Existing Database for Duplicate Entry 
                duplicate()
                break
            else:
                y=int(input("Confirm your Input \n 1.Everything is Ok,I want to Continue Saving the Number \n 2.Its not Ok,I want to edit the Contact \n Enter your choice : "))
                if y==1:
                    a.append(phno)
                    b.append(input("Enter the Name of the Contact : "))
                elif y==2:
                    z=int(input("Enter the New Edited Contact Number : "))
                    m=input("Enter the New Edited Contact Name : ")
                    a.append(z)
                    b.append(m)
    if x==0 : # Condition for Append
        for i in range (n):
            y=int(input("Confirm your Input \n 1.Everything is Ok,I want to Continue Saving the Number \n 2.Its not Ok,I want to edit the Contact \n Enter your choice : "))
            if y==1:
                a.append(int(input("Enter the Contact Number : ")))
                b.append(input("Enter the Name of the Contact : "))
            elif y==2:
                z=int(input("Enter the New Edited Contact Number : "))
                m=input("Enter the New Edited Contact Name : ")
                a.append(z)
                b.append(m)
            else:
                print("Wrong Input !!!! \n Redirecting you to the HOME page |n Please try Hence forth ")
                exit
        print("Contact Saved Successfully \n")

def duplicate(): # Prevents Duplicate Entry 
    # If Existing Contact Found (Duplicate Entry)          
    print("This Number Already Exists in your Contact list \n Try Saving Another Number ")
    print("We are Redirecting you to the Home Page \n Please Ty Again Later !!!")
    q=int(input("Do you want to Try Again Adding New Contact \n 1.Yes \n 2.No \n Enter Your Choice : "))
    if q==1:
        update() # A Chance Given For Updation of the Contact List
    elif q==2:
        print("Redirecting to you to HOME page")
        exit
    else:
        print("Wrong Input !!! \n Redirecting to you to HOME page")
        exit    

def search(): # Search Any Contact 
    if len(a)==0:
        error()
    elif len(a)!=0:
        key=input("Enter the Name of the Contact : ")
        for i in range (len(a)):
            if (b[i]==key):  # Disables if key is not found 
                c=1
            else:
                c=0

        if c==1:
            print("Contact Sucessfully Found : ")
            print("The Name of the Contact is : ",key,"\n The Contact Number is : ",a[i])

        else:
            v=input("The Entered Contact name is not saved \n Do you want to save \n 1.Yes \n 2.No \n Enter your Choice : ")
            if v==1:
                update() # Pass back to updation center

            elif v==2:
                print("Contact Not Found \n Thankyou for Using this Application \n Have a good Day")

def error(): # If Searched In Empty Contact List 
    print("You Have not Saved any Contacts yet \n Your Contact list is Empty ")
    t=int(input("Do you Want to Add new Contacts \n 1.Yes \n 2.No "))
    if t==1: 
        update()
    elif t==2:  
        print("You are being Redirected to the Home Page \n Please Continue From Hence Forth ")
        exit
    else:
        print("Invalid Input \n You are being Redirected to the Home Page \n Please Continue From Hence Forth ")
        exit

def delete(): # Deletion from Existing Contacts 
    if len(a)!=0: # If there is no element present then Disables
        key=input("Enter the Name of the Contact : ")
        for i in range (len(a)):
            if (b[i]==key):  # Checking Condition of the key to be present 
                c=1
                k=i
        if c==1:
            print("Contact Sucessfully Found ")
            print("The Name of the Contact is : ",key,"\n The Contact Number is : ",a[i])
            print("Contact Successfully Deleted")
            print("The updated Contact list is : ")
            for i in range (len(a)):
                print("Contact Name : ",a[i])
                print("Contact Number : ",b[i])
                print("\n")

        else:  # Disabled condition of the code
            print("Entered Contact Does not Exists !!!")
        a.pop(k)
        b.pop(k)

    elif len(a)==0:  # A Chance to update the Contact List
        print("You Have not Saved any Contacts yet \n Your Contact list is Empty ")
        t=int(input("Do you Want to Add new Contacts \n 1.Yes \n 2.No \n Enter Your Choice "))
        if t==1:
            update()

        elif t==2:  
            print("You are being Redirected to the Home Page \n Please Continue From Hence Forth ")

        else:
            print("Invalid Input \n You are being Redirected to the Home Page \n Please Continue From Hence Forth ")

def display():  # Displaying condition of the Contact List
    if len(a)==0:
        print("There is no Saved Contacts Present ")
        v=int(input("Do you want to save new Contacts \n 1.Yes \n 2.No \n Enter your choice : "))
        if v==1:
            update()
        
        elif v==2:
            print("Redirecting you to the HOME Page Please Continue from Hence ")
            exit

        elif v!=1 or v!=0 or v!=2:  # Passing Condition for the process
            print("Invalid Input \n Redirecting you to the HOME Page")

    elif len(a)==1:
        print("The Saved Contact is : \n")
        for i in range(len(a)):
            print (i+1,"---> Contact Name : ",a[i],"Contact Number : ",b[i])
            print("\n")
    elif len(a)!=0 or len(a)!=1:
        print("The Saved Contacts are : \n")
        for i in range(len(a)):
            print (i+1,"---> Contact Name : ",a[i],"Contact Number : ",b[i])
            print("\n")
def edit(): # Editing Section of the Program 
    if len(a)==0:
        empty()
    elif len(a)!=0:
        key=input("Enter the Name of the Contact : ")
        for i in range (len(a)):
            if (b[i]==key):
                c=1
                k=i

        if c==1: # Condition for finding the contact to be Edited
            print("Contact Sucessfully Found ")
            print("The Name of the Contact is : ",key,"\n The Contact Number is : ",a[i])
            v=int(input("What do You want to Edit \n 1.Contact Name \n 2.Contact Number \n 3.Both \n Enter your Choice: "))
            if v==1: # New Contact Input
                b.pop(k)
                m=input("Enter the new Contact Name : ")
                b.insert(k,m)

            elif v==2: 
                a.remove(k)
                m=int(input("Enter the New Contact Number : "))
                a.insert(k,m)

            elif v==3:
                a.pop(k)
                b.pop(k)
                m=int(input("Enter the New Contact Number : "))
                n=input("Enter the New Contact Name : ")
                a.insert(k,m) # Inserting the new contact Number 
                b.insert(k,n) # Inserting the new contact Name 
            print("Contact Details Edited Successfully ")
            print("New Contact Details are : ")
            for i in range(len(a)):
                print("Contact Name : ",b[k])
                print("Contact Number : ",a[k])

        else :  # Searching contition of the contact number to edit 
            print("Contact Not Found !!! ")
            o=int (input("Do you want To Try Again \n 1.Yes \n 2.No "))
            if o==1:
                edit() # A chance given to Repeat the function 

            elif o==2:
                print("Redirecting you to the HOME page")
            # Redirection to the HOME page 
            else:
                print("Invalid Input \n Redirecting you to the HOME page")

def empty(): # Prevents Error Encountered Upon Empty Contact List 
    print("You Have not Saved any Contacts yet \n Your Contact list is Empty ")
    t=int(input("Do you Want to Add new Contacts \n 1.Yes \n 2.No "))
    if t==1:
        update()
    elif t==2:  
        print("You are being Redirected to the Home Page \n Please Continue From Hence Forth ")
        exit
    else:
        print("Invalid Input \n You are being Redirected to the Home Page \n Please Continue From Hence Forth ")
        exit    

#main
a=[]
b=[]
print("CONTACT LIST SAVER \n\n\n\n ")
print(" CAUTION !!!!! \n Please be Careful this Software Takes Integer Input Mostly So try to Maintain the Streak of Integers Input to Avoid Problematic Situations while using this Application ")
while True: # Loop Running Infinitely
    ch=int(input("HOME PAGE \n\n 1.Add New Contact \n 2.Search Any Contact \n 3.Delete a Contact from Existing Contact \n 4.Display the Existing Contact \n 5.Edit the Existing Contact \n 6.Exit \n Enter your Choice : "))
    if ch==1:
        update()

    elif ch==2:
        search()

    elif ch==3:
        delete()

    elif ch==4:
        display()

    elif ch==5:
        edit()

    elif ch==6:
        print("Thankyou For Using This Application \n Have a Good Day !! ")
        break

    else:
        print("Invalid Input !!! ")