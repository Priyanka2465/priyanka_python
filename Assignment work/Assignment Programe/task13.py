#Write a Python program to count the occurrences of each word in a given sentence....

n=input("Enter the string=")
dict={}
words = n.split()

for words in n:
    if words in dict:
        dict[words]+=1
    else:
        dict[words]=1
print(dict)#left........