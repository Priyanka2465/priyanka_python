# Write a Python program to read a file line by line store it into a variable...
file=open("hello.txt","r")
str=""
for i in range(1,100):
    str=str+file.read(i) #store file contant line by line in the variable

print(str)