# Write a Python program to copy the contents of a file to another file...
ffile=open("Que.Ans.txt","r")
sfile=open("test.txt","a")
for i in ffile:
    sfile.write(i)  # copy all contents in second file...