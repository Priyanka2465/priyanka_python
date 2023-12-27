#while loop logic program...
n=20
while True:
    choice=int(input("Enter number between 1 to 25 ="))
    
    if choice==n:
        print("You win")
        break

    elif choice<n:
        print("Your number is smaller than original number")

    elif choice>n:
        print("Your number is grater than original number")

    else:
        print("Invalid number")
    