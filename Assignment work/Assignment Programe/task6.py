#without temp variable
a=12
b=13
a=a+b
b=a-b
a=a-b
print(a,b)

#with temp variable...
a=12 
b=13
temp=a
a=b
b=temp
print(a,b)