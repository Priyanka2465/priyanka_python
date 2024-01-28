# Write a Python program to read a file line by line and store it into a list...
file=open("hello.txt","r")
f1=file.readlines()
l=[]
for i in f1:
    l.append(i) #store line by line content in the list

print(l)