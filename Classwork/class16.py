n=int(input("Enter number="))
ev=0
od=0
count=0
odcount=0
i=1
while (i<=n):
    if i%2==0:
        print(i,"is evevn number")
        ev+=i
        count+=1
    else:
        print(i,"is odd number")
        od+=i
        odcount+=1
    i+=1

print("Even number=",ev)
print("Odd number=",od)
print("Even number",count)
print("odd number",odcount)