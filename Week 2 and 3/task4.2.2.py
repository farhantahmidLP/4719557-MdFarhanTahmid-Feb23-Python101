import math
def is_prime(num):
    for i in range(2,int(num)):
        if (int(num)%i==0):
            return False
    return True
        
print(is_prime(7))
print(is_prime(4))
print(is_prime(21))
print(is_prime(59))