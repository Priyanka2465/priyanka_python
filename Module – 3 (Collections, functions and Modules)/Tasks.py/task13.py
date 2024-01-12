# Write a Python program to get unique values from a list...
li=[1,2,2,3,3,3,4,5,5]
li1=[]
for i in li:
    if i not in li1:
        li1.append(i)
print(li1)



