def sum(a,b):
    return a+b

def sub(a,b):
    return b-a

def multi(a,b):
    return float(a*b)

def divide(a,b):
    return float(a/b)

num1=15
num2=20

num3=7.667
num4=12.89
print("15 and 20")
print(f"Sum: {sum(num1,num2)}")
print(f"Sub: {sub(num1,num2)}")
print(f"Multi: {multi(num1,num2)}")
print(f"Divide: {divide(num1,num2)}")

print("7.667 and 12.89")
print(f"Sum: {sum(num3,num4)}")
print(f"Sub: {sub(num3,num4)}")
print(f"Multi: {multi(num3,num4)}")
print(f"Divide: {divide(num3,num4)}")

print(f"Multi: {multi(num1,num4)}")
print(f"Divide: {divide(num3,num2)}")


    