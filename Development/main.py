from operation import *     #importing from operation
from read import *          #importing from read
from write import*          #importing from write

print("\n")
print("\t \t Welcome to Norbu Rentals")
print("\n")
print("\t Address: Kamalpokhari | Contact: 9823456723")

loop=True
while (loop==True):         #loop terminates unitl the user enters 3.
    print("\n")
    print("-------------------------------------------------------------------------")
    print("Choose the option you want to continue:")
    print("Press 1 to rent")
    print("Press 2 to return")
    print("Press 3 to exit")
    print("-------------------------------------------------------------------------")
    print("\n")

    userInput= (input("Please enter the operation you want to continue: "))          #takes the input for operation to continue
    if userInput=="1":

        name, phoneNumber, boughtItems, today_date_and_time, grandtotal = rent()    #stores all data returned by rent()
        bill(name, phoneNumber, boughtItems,today_date_and_time, grandtotal)        #calls the bill funtion
        print("\n")
        print("Thank you for rentinig🙏")

    elif userInput=="2":
        name, phoneNumber,boughtItems, today_date_and_time,grandtotal,fine,totalFine=returning()   #stores all data returned by returning()
        returnBill(name, phoneNumber,boughtItems, today_date_and_time,grandtotal,fine,totalFine)   #calls the returnBill funtion
        print("\n")
        print("Thank you for returning🙏")

    elif userInput=="3":    #ends the loop
        print("Thank you for using our system🙏")
        loop=False      

    else:
        print("invaid operation")
                
    
    
