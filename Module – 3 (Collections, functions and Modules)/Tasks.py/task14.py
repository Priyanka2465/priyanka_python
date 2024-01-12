# Write a Python program to check whether a list contains a sub list...
li1 = [9, 4, 5, 8, 10]
li2 = [5]
flag=0
for x in li1:
    if x in li2:
        flag=1
if (flag):
    print("Yes")
else:
    print("Not")


