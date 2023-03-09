original_list = [2, 5, 7, 4 , 99, 20, 11, 3]
new_list=[]
def is_odd(num):
    if (int(num)%2==0):
        return False
    else:
        return True
    
for elements in original_list:
    if(is_odd(elements)==False):
        new_list.append(elements)
print(original_list)
print(new_list)