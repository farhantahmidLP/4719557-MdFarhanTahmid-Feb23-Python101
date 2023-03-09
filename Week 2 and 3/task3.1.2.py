inp = input("Enter a character : ")
if(inp.islower()):
    inp=inp.upper()
elif(inp.isupper()):
    inp=inp.lower()
print(inp)