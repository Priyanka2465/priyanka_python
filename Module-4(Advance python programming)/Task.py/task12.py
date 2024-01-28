# How Do You Handle Exceptions With Try/Except/Finally In Python?Explain with coding snippets.
try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print(c)

except ZeroDivisionError as e: # if user divide by 0 than execute
    print(e)

except : # all user error include
    print("Error")

finally: # always execute
    print("Thank you")