# Write a Python function that takes two lists and returns true if they have
# at least one common member.
li=[1,2,3,4]
li1=[8,3,6]
result=False
for i in li:
    for j in li1:
        if i==j:
            result=True
            print(result)
            
       



