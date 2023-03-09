num=0
while(str(num)!='Q' or str(num)!='q'):
    num=input("Enter a number or press 'Q' to quit : ") 
    if(num=='q' or num=='Q'):
        break
    elif(int(num)<0):
        print("Its a negative number")
    elif(int(num)>=0):
        print("Its a positive number")
