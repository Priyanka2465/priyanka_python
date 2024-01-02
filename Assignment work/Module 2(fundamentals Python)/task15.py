# Write a Python program to add 'ing' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then add
# 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

i=input("Enter string=")
if len(i) >= 2:
    if i[-3:]=="ing":
        print(i+"ly")
    else:
        print(i+"ing")
else:
    print(i)
