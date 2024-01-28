# Write a python program to find the longest word....
file=open("Que.Ans.txt","r")
f1=file.read().split() #convert str into list
s=len(max(f1,key=len)) #find longest word
for i in f1:
    if len(i)==s:
        print(i)