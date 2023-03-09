def sum(a,b,c=None):
    if(c==None):
        return a+b
    else:
        return sum(sum(a,b),c)

def sub(a,b,c=None):
    if(c==None):
        return b-a  
    else:
        return sub(sub(a,b),c)

def multi(a,b,c=None):
    if(c==None):
        return float(a*b) 
    else:
        return multi(multi(a,b),c)

def divide(a,b,c=None):
    if(c==None):
        return float(a/b)
    else:
        return divide(divide(a,b),c)    

num1=15
num2=20

num3=7.667
num4=12.89
print(f"Sum: {sum(num1,num2)}")
print(f"Sub: {sub(num1,num2)}")
print(f"Multi: {multi(num1,num2)}")
print(f"Divide: {divide(num1,num2)}")

print(f"Sum: {sum(num3,num4,num1)}")
print(f"Sub: {sub(num3,num4,num2)}")
print(f"Multi: {multi(num3,num4,num1)}")
print(f"Divide: {divide(num3,num4,num2)}")



    