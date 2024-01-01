#Write a Python program to count the number of characters (character frequency) in a string...


n=input("Enter the character=")
dict={}
for i in n:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)