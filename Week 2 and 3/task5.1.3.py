names=[]
name=None
while(name!=""):
    name=input("Enter a name : ")
    if(name!=""):
        names.append(name)
print(names)
names.reverse()
print(names)