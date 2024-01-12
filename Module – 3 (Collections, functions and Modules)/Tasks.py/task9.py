# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
li=[1,2,3,3,3,4,4,5]
li1=[]
for i in li:
    if i not in li1:
        li1.append(i)
print(li1)