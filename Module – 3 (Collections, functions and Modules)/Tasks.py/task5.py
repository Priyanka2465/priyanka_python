# Write a Python program to remove duplicates from a list
l=[1,2,3,3,4,5]
li=[]
for i in l:
    if i not in li:
        li.append(i)
print(li)