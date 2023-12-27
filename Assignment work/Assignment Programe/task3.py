n=int(input("Enter the number="))
n1=0
n2=1
count=2
if n==1:
    print(n1)
elif n==2:
    print(n1,n2)
else:
    print(n1,n2,end=" ")
    while count<n:
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end=' ')
        count+=1