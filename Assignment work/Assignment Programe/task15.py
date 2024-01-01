i=input("Enter string=")
le=0
if i > 2:
    if i[-3:]=="ing":
        le+="ly"
    else:
        le+="ing"
print(le)#left....
