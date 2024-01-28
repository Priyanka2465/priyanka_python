# Write a Python program to count the frequency of words in a file...
file=open("hello.txt","r")
f1=file.read().split()
d={}
for i in f1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)