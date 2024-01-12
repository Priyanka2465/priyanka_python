# Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30. 
li=[1,2,3,4,5,6,7,8,9,10,11]
li1=[]
for i in li:
    li1.append(i**2)
print(li1[:5]+li1[-5:])
