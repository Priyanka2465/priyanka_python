# Write python program that user to enter only odd numbers, else will raise an exception.
try:
    a=int(input("Enter number="))
    while True:
        if a%2!=0:
            print("Thank you")
            break
        else:
            ValueError
            break
    
except:
    print("Enter Only Odd number")