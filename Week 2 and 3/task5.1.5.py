import math
list=[]
num=input("Insert a number : ")
for i in range(1,int(num)+1):
    list.append(int(math.pow(i,2)))
print(list)