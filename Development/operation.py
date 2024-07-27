from read import*               #imports from read
from datetime import datetime   #imports from datetime

def rent():
    """Accepts no parameter returns name, phoneNumber, boughtItems, today_date_and_time, grandtotal."""

    myDictionary=read()     #Initializes the dictionary
    boughtItems=[]          #Initializes the list
    today_date_and_time = None  #initailizes datetime to none

    print("------------------------------------------------------------------------------------")
    print("You will have to enter your details first: ")
    print("------------------------------------------------------------------------------------")
    print("\n")
    name=input("Enter your name: ")
    print("\n")
    
    while True:
        try:
            phoneNumber=int(input("Enter your phone number: "))
            if isinstance(phoneNumber, str)or phoneNumber<=0:        #if phoneNumber is string, ValueError is raised
                raise ValueError 
            else:
                break
        except ValueError:                          #excepts ValueError and displays message
            print("Phone number is invalid!!!\n")
            
    print("\n")
    print("\t \t \t\t Norbu Rentals")
    print("------------------------------------------------------------------------------------")
    print("S.N. \tItem Name \t\t\tCompany Name\t\t Price\t Quantity")
    print("------------------------------------------------------------------------------------")

    file=open("item.txt","r")
    sn=1
    for line in file:
        print(sn,"\t"+line.replace(",","\t"))
        sn=sn+1
    print("------------------------------------------------------------------------------------")
    file.close()
    print("\n")

    more=True
    while more:
        while True:
            try:
                valid_id= int(input("Please provide the ID of the item you want to rent:"))         #takes id
                print("\n")
                if (valid_id<=0 or valid_id>len(myDictionary)):     #validates the id
                    raise ValueError        
                else:
                    while True:
                        try:
                            user_quantity= int(input("Please provide the number of quantity of the item you want to rent:"))#takes quantity of item
                            print("\n")
                            get_quantity_of_selected_item= myDictionary[valid_id][3]

                            if user_quantity<=0 or user_quantity > int(get_quantity_of_selected_item):  #validates the quantity
                                raise ValueError
                            else:
                                myDictionary[valid_id][3]= int (myDictionary[valid_id][3])-int(user_quantity)
                                file=open("item.txt","w")

                                for values in myDictionary.values():
                                    file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
                                    file.write("\n")

                                file.close()

                                my_input_exit= input("Dear user do you want to borrow any more item? If yes press, 'Y' else press 'Enter' key.").upper()
                                
                                if my_input_exit=="Y":
                                    more=True
                                else:
                                    more=False

                                #getting user purchased items
                                productName=myDictionary[valid_id][0]                           #gets the name of product from the dictionary
                                userSelectedQuantity= user_quantity                             #gets the quantity from the dicitonary
                                priceOfItem= myDictionary[valid_id][2]                          #gets the price from the dicitonary
                                priceOfSelectedItem= myDictionary[valid_id][2].replace("$",'')  #gets the price from the dicitonary
                                totalPrice=int(priceOfSelectedItem)*int(userSelectedQuantity)   #calculates totalPrice
                                boughtItems.append([productName, userSelectedQuantity, priceOfItem, totalPrice]) #adds to the list
                                print("\n")

                                #calculation of grand total
                                grandtotal=0
                                if my_input_exit=="Y":      #if user wants to rent more items, loop is continued
                                    more=True
                                else:                       #if user wants to rent more items, calculation is done
                                    total=0
                                    for i in boughtItems:
                                        total=total+int(i[3])
                                    grandtotal= total
                                    today_date_and_time = datetime.now()        #datetime.now() is the current time
                            break   
                          
                        except ValueError:          #excepts ValueError and displays message
                            print("Please enter valid quantity. You can check the quantity that is available.\n")
                break 

            except ValueError:          #excepts ValueError and displays message
                print("Enter valid id!!!\n")
       
    return name, phoneNumber, boughtItems, today_date_and_time, grandtotal    #returns the values where the funtion is called

def returning():
    """Accepts no parameter and returns name, phoneNumber, boughtItems, today_date_and_time, grandtotal, fine and totalFine"""
    myDictionary=read()         #Initializes the dictionary
    boughtItems=[]              #Initializes the list
    today_date_and_time = None  #Initializes the datetime to none
    rentDays=0                  #Initializing
    phoneNumber=None            #Initializing
    fine=0                      #Initializing
    grandtotal=0                #Initializing
    totalFine=0                 #Initializing

    print("------------------------------------------------------------------------------------")
    print("\n")
    name=input("Enter your name: ")
    print("\n")
    while True:
        try:
            phoneNumber=int(input("Enter your phone number: "))
            if isinstance(phoneNumber, str):        #raises ValueError if string is entered in phoneNumber
                raise ValueError 
            else:
                break
        except ValueError:
            print("Phone number is invalid!!!\n")
            
    print("\n")
    print("\t \t \t\t Norbu Rentals")
    print("------------------------------------------------------------------------------------")
    print("S.N. \tItem Name \t\t\tCompany Name\t\t Price\t Quantity")
    print("------------------------------------------------------------------------------------")
            
    file= open(str(name)+str(phoneNumber)+".txt","w")
    file=open("item.txt","r")
    sn=1
    for line in file:
        print(sn,"\t"+line.replace(",","\t"))
        sn=sn+1
    print("------------------------------------------------------------------------------------")
    file.close()
    print("\n")

    more=True
    while more:
        while True:
            try:
                valid_id= int(input("Please provide the id of the item you want to return: "))
                print("\n")
                if valid_id<=0 or valid_id>len(myDictionary):   #validates id
                    raise ValueError
                else:
                    while True:
                        try:
                            user_quantity= int(input("Please provide the number of quantity of the item you want to reuturn: "))
                            print("\n")
                            if user_quantity<=0 or user_quantity > 100:     #validates quantity
                                raise ValueError  
                            else:                                            
                                myDictionary[valid_id][3]= int (myDictionary[valid_id][3])+int(user_quantity)
                                file=open("item.txt","w")
                                for values in myDictionary.values():
                                    file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
                                    file.write("\n")
                                file.close()
                                
                                #getting user purchased items
                                productName=myDictionary[valid_id][0]                           #gets the name of product from the dictionary
                                userSelectedQuantity= user_quantity                             #gets the quantity from the dicitonary
                                priceOfItem= myDictionary[valid_id][2]                          #gets the price from the dicitonary
                                priceOfSelectedItem= myDictionary[valid_id][2].replace("$",'')  #gets the price from the dicitonary
                                totalPrice=int(priceOfSelectedItem)*int(userSelectedQuantity)   #calculates totalPrice
                                priceOfItemInt=int(priceOfItem.replace("$",''))                 #stores the priceOfItem in integer
                            
                                while True:
                                    try:
                                        rentDays=int(input("Enter the number of days you rented: "))
                                        if rentDays<1:                               #rent days can't be less than 1
                                            raise ValueError
                                        else:
                                            if rentDays<=5:                          #user is not fined if rent days is within 5 days
                                                fine=0
                                            elif rentDays%5!=0:                      #fine is calculated for rentdays not multiple of 5
                                                fineday=(((int(rentDays//5)+1)*5)-5)*user_quantity
                                                fine=int((fineday/5))*int(priceOfItemInt)  
                                            else:                                    #fine is calculated for rentdays multiple of 5
                                                fine=(rentDays-5)*int(priceOfItemInt)
                                            totalFine=totalFine+fine
                                            boughtItems.append([productName, userSelectedQuantity, priceOfItem, totalPrice,rentDays,fine,totalFine])#adds to the list
                                            print("\n")
                                            my_input_exit= input("Dear user do you want to return any more item? If yes press, 'Y' else press 'Enter' key.").upper()
                                            
                                            if my_input_exit=="Y":
                                                print("\n")
                                                more=True
                                            else:
                                                more=False

                                            grandtotal=0
                                            if my_input_exit=="Y":          #if user wants to return more, loop is continued
                                                more=True
                                            else:                           #if user is done returning, total is calculated including fine
                                                total=0
                                                for i in boughtItems:
                                                    total=total+int(i[3])
                                                grandtotal= total+totalFine
                                                today_date_and_time = datetime.now()        #datetime.now() is the current time
                                            break
                                    except ValueError:
                                        print("Invalid days!!!")  
                                        print("\n")
                            break    
                        except ValueError:
                            print("Invalid quantity!!! Quantity cannot be less than 1 and more than 100.")
                            print("\n")
                break        
            except ValueError:
                print("Enter valid id!!") 

    return name, phoneNumber, boughtItems, today_date_and_time, grandtotal, fine,totalFine     #returns the values where the funtion is called

        
        
    
