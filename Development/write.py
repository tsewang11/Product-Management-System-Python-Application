from operation import *
from datetime import datetime

def bill(name, phoneNumber, boughtItems,today_date_and_time, grandtotal):  
    """Takes name, phoneNumber, boughtItems,today_date_and_time and grandtotal and returns nothing"""
    print("\n")
    print("\t \t \t \t \t Norbu Rentals Rent Bill ")
    print("\n")
    print("\t \t \t Kamalpokhari, Kathmandu | Phone No: 9811112255 ")
    print("\n")
    print("--------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Customer Details are:")
    print("--------------------------------------------------------------------------------------------------------")
    print("Name of Customer:"+str(name))    #prints the name of customer
    print("Contact number: "+str(phoneNumber))  #prints the phonenumber of customer
    print("Date and time of purchase: "+str(today_date_and_time))   #prints the date and time of renting
    print("--------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Rent Detail are:")
    print("--------------------------------------------------------------------------------------------------------")
    print("Item Name \t\t Total Quantity \t\t Unit Price \t\t\tTotal")
    print("--------------------------------------------------------------------------------------------------------")
    for i in boughtItems:
        print(i[0],"\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
    print("--------------------------------------------------------------------------------------------------------")
    print("Grand Total: $"+str(grandtotal))     #prints the grand total
    print("Note: Fine cost will added to the grand total in case you exceed 5 days")    
    file= open(str(name)+str(phoneNumber)+".txt","w")   #creates a txt file on the basis of user's name and phone number
    file.write("\n")
    file.write("\n")
    file.write("\t \t \t \t \t Norbu Rentals Rent Bill ")
    file.write("\n")
    file.write("\t \t \t Kamalpokhari, Kathmandu | Phone No: 9811112255 ")
    file.write("\n")
    file.write("----------------------------------------------------------------------------")
    file.write("\n")
    file.write("Customer Details are:")
    file.write("\n")
    file.write("----------------------------------------------------------------------------")
    file.write("\n")
    file.write("Name of the Customer:"+str(name))
    file.write("\n")
    file.write("Contact number: "+str(phoneNumber))
    file.write("\n")
    file.write("Date and time of purchase: "+str(today_date_and_time))
    file.write("\n")
    file.write("----------------------------------------------------------------------------")
    file.write("\n")
    file.write("Rent Detail are:")
    file.write("\n")
    file.write("----------------------------------------------------------------------------")
    file.write("\n")
    file.write("Item Name \t\t\t\t Total Quantity \t\t Unit Price \t\tTotal")
    file.write("\n")
    file.write("----------------------------------------------------------------------------")
    file.write("\n")
    for i in boughtItems:
        file.write(str(i[0])+"\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t\t"+"$"+str(i[3]))
        file.write("\n")
    file.write("\n")
    file.write("----------------------------------------------------------------------------")
    file.write("\n")
    file.write("Grand Total: $"+str(grandtotal))
    file.write("\n")
    file.write("Note: Fine cost will added to the grand total in case you exceed 5 days")
    file.close()
    more=False

def returnBill(name, phoneNumber,boughtItems, today_date_and_time,grandtotal,fine, totalFine):
    """ Takes name, phoneNumber,boughtItems, today_date_and_time,grandtotal,fine and returns nothing"""
    print("\n")
    print("\t \t \t \t \t Norbu Rentals Return Bill ")
    print("\n")
    print("\t \t \t Kamalpokhari, Kathmandu | Phone No: 9811112255 ")
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Customer Details are:")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("Name of the Customer:"+str(name))                       #prints the name of customer 
    print("Contact number: "+str(phoneNumber))                     #prints the phone number of customer
    print("Date and time of return: "+str(today_date_and_time))    #prints the date and time of returning
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("Item Name \t\t\tTotal Quantity \t\t Unit Price \t\tTotal\t\tRented Days\tFine")
    print("-----------------------------------------------------------------------------------------------------------------------")
    for i in boughtItems:
        print(i[0],"\t",i[1],"\t\t\t",i[2],"\t\t","$",i[3],"\t\t",i[4],"\t\t$",i[5])
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("Fine: $"+str(totalFine))
    print("Grand Total: $"+str(grandtotal))

    file= open(str(name)+str(phoneNumber)+".txt","w")   #creates a txt file on the basis of user's name and phone number
    file.write("\n")
    file.write("\t \t \t \t \tNorbu Rentals Bill ")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("\t \t \tKamalpokhari, Kathmandu | Phone No: 9811112255 ")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Return Details are:")
    file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------\n")
    file.write("Name of the Customer:"+str(name))
    file.write("\n")
    file.write("Contact number: "+str(phoneNumber))
    file.write("\n")
    file.write("Date and time of return: "+str(today_date_and_time))
    file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Return Detail are:\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------\n")
    #file.write("Item Name \t\t\t\t Total Quantity \t\t\t Unit Price \tTotal\t\tRented Days \tFine")
    file.write("Item Name \t\t\t\t\t\tTotal Quantity \t\t Unit Price \t\tTotal\t\tRented Days\t\t\tFine")#
    file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    for i in boughtItems:
        #file.write(str(i[0])+"\t"+str(i[1])+"\t\t\t\t\t"+str(i[2])+"\t\t\t"+"$"+str(i[3])+"\t\t\t"+str(i[4])+"\t\t$"+str(i[5]))
        file.write(str(i[0])+"\t"+str(i[1])+"\t\t\t\t\t\t"+str(i[2])+"\t\t\t"+"$"+str(i[3])+"\t\t\t\t"+str(i[4])+"\t\t\t\t$"+str(i[5]))
        file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------\n")
    file.write("Total Fine: $"+str(totalFine))
    file.write("\n")
    file.write("Grand Total: $"+str(grandtotal))
    file.close()
    more=False


    
    
