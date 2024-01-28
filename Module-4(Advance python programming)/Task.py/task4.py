# Write a Python program to read last n lines of a file...
file=open("Que.Ans.txt","r")
f1=file.readlines()[-1] #read the last line of the file
print(f1)
file.close()