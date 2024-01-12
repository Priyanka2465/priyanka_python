# Write a Python program to print all unique values in a dictionary..
d={"hii":1,"Hey":2,"good":1}
di=[]
for i in d.values():
    if i not in di:
        di.append(i)
print(dict(zip(d,di)))



