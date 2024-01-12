# Write a Python function to check whether a number is perfect or not...
def myfun(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    print(sum==n)

myfun(6)