#Write a Python program to count the occurrences of each word in a given sentence....

n=input("Enter the string=")
dicts=dict()
words = n.split()

for i in words:
    if i in dicts:
        dicts[i]+=1
    else:
        dicts[i]=1
print(dicts)