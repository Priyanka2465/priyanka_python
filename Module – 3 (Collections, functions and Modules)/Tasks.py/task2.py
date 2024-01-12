#Write a Python function to get the largest number, smallest num and sum of all from a list. 

li=[1,3,12,4,31,10]
print(max(li))
print(min(li))
sum=0
for i in li:
    sum=sum+i
print(sum)