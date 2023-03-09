import math
def is_prime(num):
    for i in range(2,int(num)):
        if (int(num)%i==0):
            return False
    return True

number=input("How many numbers do you want to check? : ")

for i in range(2,int(number)+1):
    if(is_prime(i)):
        print(i)