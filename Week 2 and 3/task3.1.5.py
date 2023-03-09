i=0
num=1
sum=0
minimum=float('inf')
maximum=float('-inf')
average=None
while (float(num)!=0):
    num=input("Enter any number or 0 to quit : ")
    if(float(num)!=0):
        sum+=float(num)
        minimum=min(float(minimum),float(num))
        maximum=max(float(maximum),float(num))
        i+=1
if(int(i)>0):
    average=float(sum)/int(i)
print(f"The sum is {sum} and the average is {average} and the minimum is {minimum} and the maximum is {maximum}")
