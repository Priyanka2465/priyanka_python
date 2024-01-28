od=0
ev=0
sumod=0
sumev=0
n=int(input("Enter number="))
for i in range(1,11):
  
    if n%2==0:
        print("Even")
        ev=ev+1
        sumev=sumev+i
    else:
        print("Odd")
        od=od+1
        sumod=sumod+i
print(ev,"number")
print(od,"number")
print("odd number sum=",sumod)
print("Even number sum=",sumev)