import os
print("------------------------------------------------------------------------------------")
print("\n")
name=input("Enter your name:")
print("\n")
phoneNumber=int(input("Enter your phone number"))
print("\n")
#file= open(str(name)+str(phoneNumber)+".txt","w")
#filePath="C:\Users\kargo\OneDrive\Documents\Islington\FOC\course work materail\coursework practice\"+str(name)+str(phoneNumber)+".txt"
fileName=str(name)+str(phoneNumber)+".txt"
print(fileName)
searchFile = "C:/Users/kargo/Documents/Islington/FOC/course work material/coursework practice"
found=False
   
for directory in searchFile:
    filePath = os.path.join(directory, fileName)
    if os.path.exists(filePath):
        found = True
        break 
if found==False:
    print("Please provide the correct name and phone number which you provied while renting")
else:
    print("Your file is found")