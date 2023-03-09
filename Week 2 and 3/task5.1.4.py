list=[1,2,2,2,3,1,4,2,3,6,7,9,7,3]
print(list)
new_list=[]
for element in range(0,len(list)):
    if list[element] not in new_list:
        new_list.append(list[element])
print(new_list)