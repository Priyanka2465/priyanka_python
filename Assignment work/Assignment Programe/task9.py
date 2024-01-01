# Write a python program to sum of the first n positive integers.

# n=int(input("Enter number="))
# sum=sum(range(n+1))
# print(sum)

n=int(input("Enter the number="))
sum=0
for i in range(0,n+1):
    sum=sum+i
print(sum)