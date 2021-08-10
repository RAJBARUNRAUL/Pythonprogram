import time,csv,datetime
class library:

    
    def admin_login(self):
        username = 'admin'
        password = 'password'

        userInput = input("ENTER YOUR ADMIN ID -")

        if userInput == username:
            a=input("ENTER YOUR ADMIN PASSWORD -")   
            if a == password:
                print("Welcome!")
                self.admin_menu()
            else:
                print("ADMIN PASSWORD DID NOT MATCH")
        else:
            print("ADMIN ID DID NOT MATCH")

    def admin_menu(self):
        print('Logging in...')
        time.sleep(1)
        print('Please select any item from the menu:')
        
        print('press 1 to ADD BOOK')
        time.sleep(1)
        print('press 2 to Update BOOK')
        time.sleep(1)
        print('press 3 to View BOOK')
        time.sleep(1)
        print('press 4 to Delete BOOK')

        action= int(input('your input: '))

    
       ################################################################    
        
        if action==3:
            
            time.sleep(1)

            print("please enter the details of the BOOK you want view")
            prod = input('Product ID:  ')
            
            with open('D:/PROGRAMMING DATASCIENCE/LMS/1/Product_details.csv','r') as f:
                file= csv.reader(f)
                for row in file:
                    if row[0] == str(prod):
                        print("Below are the details of BOOK you are looking for: \n")
                        time.sleep(1)
                        print("BOOK name:      ",row[1])
                        print("AUTHOR:      ",row[2])
                        print("TOTAL PAGE:     ",row[3])
                        print(" Quantity AVAILABLE:  ",row[4])
                        print(" ISBN - 13 digits number:  ",row[5])
                        print(" PUBLISH DATE AND YEAR:  ",row[6])
                        print(" PRICE:  ",row[7])
     



    ################################################################    
        if action==1:
            
            
            time.sleep(1)
            print("please enter the details of the BOOK you want to add")

            productname = input('enter BOOK name:  ')
            time.sleep(1)
            author =      input('enter AUTHOR name:  ')
            time.sleep(1)
            page =       input('enter TOTAL PAGE:  ')
            time.sleep(1)
            quantity=     input('enter quantity:  ')
            time.sleep(2)
            isbn=     input('enter ISBN - 13 digits number:  ')
            time.sleep(2)
            publish=     input('enter PUBLISH DATE AND YEAR:  ')
            time.sleep(2)
            price=     input('enter PRICE:  ')
            time.sleep(2)

            print("Congrats!   Successfully addded the BOOK")

            with open('D:/PROGRAMMING DATASCIENCE/LMS/1/Product_details.csv','a') as f:

                file= csv.writer(f)
                file.writerow(['PROD' ,productname , author , page , quantity, isbn , publish, price ])
            
    ################################################################            
        
        if action==4:
        
            time.sleep(1)

            print("please enter the details of the BOOK you want to delete")
            prod = input('BOOK  ID:  ')

            with open('D:/PROGRAMMING DATASCIENCE/LMS/1/Product_details.csv') as in_file, open('D:/PROGRAMMING DATASCIENCE/LMS/1/Product_details.csv', 'w',newline='') as out_file:
                reader = csv.reader(in_file)
                writer = csv.writer(out_file)
                for row in reader:
                    if row[0] != prod:

                        writer.writerow(row)

            time.sleep(1)
            print("You have successfully removed the product ")

        
        
    ################################################################    



        if action==2:

            UP2 =  {}
            time.sleep(1)

            print("please enter the ID of the BOOK you want to update")
            prod = input('BOOK ID:  ')


            time.sleep(1)
            print("press 2 to change AUTHOR")
            print("press 3 to change Price")
            print("press 4 to change Quantity")
            time.sleep(1)

            I = input('What property do you want to change/update? ')
            U = input('Please write the updated entry ')

            #UP2[str(I)] = I

            with open('D:/PROGRAMMING DATASCIENCE/LMS/1/Product_details.csv') as in_file, open('D:/PROGRAMMING DATASCIENCE/LMS/1/Product_details.csv', 'w',newline='') as out_file:
                reader = csv.reader(in_file)
                writer = csv.writer(out_file)
                for row in reader:
                    if row[0]==prod:
                        print('updating row for PROD_ID ', row[0]," and ", row[1])
                        row[int(I)]= U
                    writer.writerow(row)

            time.sleep(2)
            print('\nSuccessfully updated the BOOK DETAILS!')
        
        
    print('\nPlease visit again')    

    def userorreg(self):
        print(" loading please wait ........................ " )
        time.sleep(2)
        userinput = input(" ARE YOU A New User OR Existing User \n PRESS N FOR New User \n PRESS E FOR Existing User \n ")
        if userinput == 'N':
            time.sleep(2)
            print(" Hello Admin to Library Management System " )
            obj.user_reg()
        if userinput == 'E':
            time.sleep(2)
            print(" Hello User to Library Management System " )
            time.sleep(2)
            obj.user_login()

    def user_login(self):
        global user1
        #global passworduser
        user = input('User ID:  ')
        passworduser = input('User Password:  ')
        user1=user
        with open('D:/PROGRAMMING DATASCIENCE/LMS/1/user_details.csv','r') as f:
                file= csv.reader(f)
                for row in file:
                    #if row[0] == str(user):
                    if row[0] == str(user):
                        if row[5] == str(passworduser):
                            print("user login sucessfull ")
                            self.user_menu()
                           
                        else:
                            print("Username/Password [INCORRECT]")
                            self.user_login()                                   
      

    def user_reg(self):
        time.sleep(1)
        print("please enter the details of user")

        username = input('enter User Name :  ')
        time.sleep(1)
        contact =      input('enter your contact:  ')
        time.sleep(1)
        email =       input('enter Email id:  ')
        time.sleep(1)
        gender=     input('enter Gender:  ')
        time.sleep(2)
        address=     input('enter address:  ')
        time.sleep(2)
        password=     input('Set your password  ')
        time.sleep(2)
        book=     'None'
        time.sleep(2)
        issuedate=     'None'
        time.sleep(2)
        returndate=     'None'
        time.sleep(2)
        dues=     'None'
        time.sleep(2)
        print("uploading data to server.........")
        time.sleep(2)
        print("Congrats!  User Registration Successfully ")

        with open('D:/PROGRAMMING DATASCIENCE/LMS/1/user_details.csv','a') as f:
            file= csv.writer(f)
            file.writerow([username , contact , email , gender , address , password, book,issuedate,returndate,dues])
        self.user_login()

    def user_menu(self):
        print('Logging in...')
        time.sleep(1)
        print('Please select any item from the menu:')
        
        print('press 1 to Issue BOOK')
        time.sleep(1)
        print('press 2 to Return BOOK')
        time.sleep(1)
        print('press 3 to View BOOK')
        time.sleep(1)
        print('press 4 to View dues')

        action2 = int(input('your input: '))
        if action2==1:
            self.issue()
        elif action2==2:
            self.returnvalue()
        elif action2==3:
            self.search()
        elif action2==4:
            self.dues()
        else:
            print("invalid input")
            self.user_menu()
        
    
       ################################################################    
        
        
            
    def search(self):
        print("Welcome to book issue system")
        print("Search Book by -")
        booksearch = input(" 1.Press S To Search Book By Serial Number (lib1~50): \n 2.Press T To Search Book By  Name: \n 3.Press A To Search Book By Author Name: \n  4.Press I To Search Book By ISBN Number: \n 4.Press 0 To Return back main menu: \n Please Enter your Choice In Upper Case Character")
        if booksearch == 'S' :
            self.searchbyserialno()
        elif booksearch == 'T' :
            self.searchbytitle()
        elif booksearch == 'A' :
            self.searchbyauthor()
        elif booksearch == 'I' :
            self.searchbyisbn()
        elif booksearch == '0' :
            self.suser_menu()
        else:
            print("Error input")
            self.search()
            
            
             
        

    def searchbyserialno(self):
        prod = input('Please Enter The serial number Of Book (lib1~50) :  ')
        time.sleep(1)
        print("Please wait searching.........")
        time.sleep(1)   
        with open('D:/PROGRAMMING DATASCIENCE/LMS/1/Product_details.csv','r') as f:
                file= csv.reader(f)
                for row in file:
                    if row[0] == str(prod):
                        print("Below are the details of BOOK you are looking for: \n")
                        time.sleep(1)
                        print("Serial Number:      ",row[0])
                        print("BOOK name:      ",row[1])
                        print("AUTHOR:      ",row[2])
                        print("TOTAL PAGE:     ",row[3])
                        print(" Quantity AVAILABLE:  ",row[4])
                        print(" ISBN - 13 digits number:  ",row[5])
                        print(" PUBLISH DATE AND YEAR:  ",row[6])
                        print(" PRICE:  ",row[7])
        self.user_menu()          
        
    def searchbytitle(self):
        prod = input('Please Enter The details Of Book  :  ')
        time.sleep(1)
        print("Please wait searching.........")
        time.sleep(1)   
        with open('D:/PROGRAMMING DATASCIENCE/LMS/1/Product_details.csv','r') as f:
                file= csv.reader(f)
                for row in file:
                    if row[1] == str(prod):
                        print("Below are the details of BOOK you are looking for: \n")
                        time.sleep(1)
                        print("Serial Number:      ",row[0])
                        print("Serial Number:      ",row[1])
                        print("AUTHOR:      ",row[2])
                        print("TOTAL PAGE:     ",row[3])
                        print(" Quantity AVAILABLE:  ",row[4])
                        print(" ISBN - 13 digits number:  ",row[5])
                        print(" PUBLISH DATE AND YEAR:  ",row[6])
                        print(" PRICE:  ",row[7])
        self.user_menu()                        
    def searchbyauthor(self):
        prod = input('Please Enter The details Of Book  :  ')
        time.sleep(1)
        print("Please wait searching.........")
        time.sleep(1)   
        with open('D:/PROGRAMMING DATASCIENCE/LMS/1/Product_details.csv','r') as f:
                file= csv.reader(f)
                for row in file:
                    if row[2] == str(prod):
                        print("Below are the details of BOOK you are looking for: \n")
                        time.sleep(1)
                        print("Serial Number:      ",row[0])
                        print("Serial Number:      ",row[1])
                        print("AUTHOR:      ",row[2])
                        print("TOTAL PAGE:     ",row[3])
                        print(" Quantity AVAILABLE:  ",row[4])
                        print(" ISBN - 13 digits number:  ",row[5])
                        print(" PUBLISH DATE AND YEAR:  ",row[6])
                        print(" PRICE:  ",row[7])
        self.user_menu()
       
    def searchbyisbn(self):
        prod = input('Please Enter The details Of Book  :  ')
        time.sleep(1)
        print("Please wait searching.........")
        time.sleep(1)   
        with open('D:/PROGRAMMING DATASCIENCE/LMS/1/Product_details.csv','r') as f:
                file= csv.reader(f)
                for row in file:
                   if row[5] == str(prod):
                        print("Below are the details of BOOK you are looking for: \n")
                        time.sleep(1)
                        print("Serial Number:      ",row[0])
                        print("Book Name:      ",row[1])
                        print("AUTHOR:      ",row[2])
                        print("TOTAL PAGE:     ",row[3])
                        print(" Quantity AVAILABLE:  ",row[4])
                        print(" ISBN - 13 digits number:  ",row[5])
                        print(" PUBLISH DATE AND YEAR:  ",row[6])
                        print(" PRICE:  ",row[7])
        self.user_menu()  

    def issue(self):
        print("Please wait searching.........")
        time.sleep(1)   
        with open('D:/PROGRAMMING DATASCIENCE/LMS/1/user_details1.csv','r') as f:
                file= csv.reader(f)
                for row in file:
                    if row[0] == str(user1):
                        if row[6] == ('None') :
                            print(" User is elegible to book issue")
                            self.issueprocess()
                        else:
                            print("Return the previous book first")
        self.user_menu()
        
    def issueprocess(self):
        global carryvalue
        global carryprice
        global carryqnty
        prod = input('Please Enter The serial number Of Book (lib1~50) :  ')
        time.sleep(1)
        print("Please wait searching.........")
        time.sleep(1)   
        with open('D:/PROGRAMMING DATASCIENCE/LMS/1/Product_details.csv','r') as f:
                file= csv.reader(f)
                for row in file:
                    if row[0] == str(prod):
                        print("Below are the details of BOOK you are looking for: \n")
                        time.sleep(1)
                        print("Serial Number:      ",row[0])
                        print("BOOK name:      ",row[1])
                        print("AUTHOR:      ",row[2])
                        print("TOTAL PAGE:     ",row[3])
                        print(" Quantity AVAILABLE:  ",row[4])
                        print(" ISBN - 13 digits number:  ",row[5])
                        print(" PUBLISH DATE AND YEAR:  ",row[6])
                        print(" PRICE:  ",row[7])
                        carryvalue = row[1]
                        carryqnty = row[4]
                        carryprice = row[7]
        print(carryvalue)
        print(carryprice)
        self.issueprocess2()

    def issueprocess2(self):
        
        with open('D:/PROGRAMMING DATASCIENCE/LMS/1/user_details.csv') as in_file, open('D:/PROGRAMMING DATASCIENCE/LMS/1/user_details1.csv', 'w',newline='') as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)
            for row in reader:
                if row[0]==user1:
                    row[6]= carryvalue
                    row[9]= carryprice
                writer.writerow(row)

        time.sleep(2)
        print('book issue')                          
   
    def dues(self):
        with open('D:/PROGRAMMING DATASCIENCE/LMS/1/user_details1.csv','r') as f:
                file= csv.reader(f)
                for row in file:
                    if row[0] == str(user):
                        print("Your account details : \n")
                        time.sleep(1)
                        print(" dues:  ",row[9])

    def returnvalue(self):
        print("Please wait searching.........")
        time.sleep(1)   
        with open('D:/PROGRAMMING DATASCIENCE/LMS/1/user_details1.csv','r') as f:
                file= csv.reader(f)
                for row in file:
                    if row[0] == str(user1):
                        if row[6] != ('None') :
                       
                            self.returnprocess()
                        else:
                            print("NO BOOK ISSUE YET")
        self.user_menu()
        
    def returnprocess(self):
                
        with open('D:/PROGRAMMING DATASCIENCE/LMS/1/user_details.csv') as in_file, open('D:/PROGRAMMING DATASCIENCE/LMS/1/user_details1.csv', 'w',newline='') as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)
            for row in reader:
                if row[0]==user1:
                    row[6]= "None"
                    row[9]= "None"
                writer.writerow(row)

        time.sleep(2)
        print('Book return') 
                        
print("WELCOME TO LIBRARY MANAGEMENT SYSTEM")

obj = library()

print(" Welcome to Library Management System " )
visitor = input(" ARE YOU ADMIN OR USER \n PRESS A FOR ADMIN \n PRESS U FOR USER \n ")
if visitor == 'A':
    time.sleep(2)
    print(" Hello Admin to Library Management System " )
    obj.admin_login()
if visitor == 'U':
    time.sleep(2)
    print(" Hello User to Library Management System " )

    time.sleep(2)
    obj.userorreg()


