from operation import *         #imports from operation
def read():
    """ Accepts no parameter and returns myDictionary"""
     
    ''' read function reads lines from 'item.txt'and stores the data in myDictionary. 
        Each line is split by commas, and the resulting values are stored in myDictionary using a unique key.
        The function returns myDictionary containing the processed data from the 'item.txt' file. '''
    file=open('item.txt','r')       #openes items.txt in read mode
    myDictionary={}                 #Intializes the dictionary
    item_id=1                       #Initalizes the item_id

    for line in file:
     line=line.replace('\n','')
     myDictionary[item_id]=line.split(',')
     item_id=item_id+1

    file.close()
    return myDictionary 

