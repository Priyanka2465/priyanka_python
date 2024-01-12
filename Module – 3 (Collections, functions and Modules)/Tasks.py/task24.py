# Write a Python program to find the repeated items of a tuple..
t=("P","r","i","y","a","n","k","a")
l=[]
j=[]
for i in t:
    if i not in l:
        l.append(i)
    else:
        j.append(i)
print(tuple(j))

