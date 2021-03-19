inputName = input()
nameComp = inputName.split(" ")  
if(len(nameComp) == 3):
   print(nameComp[2] + ", " + nameComp[0][:1] + "." + nameComp[1][:1] + '.')
elif(len(nameComp) == 2):
   print(nameComp[1] + ", " + nameComp[0][:1] + '.')
else:
   print("Invalid name")
input()