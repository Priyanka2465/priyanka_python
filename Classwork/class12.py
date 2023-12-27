#duplicate value delete in list and add another list....

l1=[1,2,3,4,1,2]
l2=[]
l3=[]
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        l3.append(i)
print(l2)
print(l3)