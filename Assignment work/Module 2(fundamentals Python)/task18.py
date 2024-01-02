#Write a Python function to reverses a string if its length is a multiple of 4.
i=input("Enter the string=")
if len(i)%4==0:
    print(''.join(reversed(i)))
else:
    print(i)
    