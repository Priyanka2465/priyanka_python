#draw pattern....


for i in range(0,6):
    print("*"*i)

for i in range(0,6):
    print(" "*(6-i)," *"*i)

for i in range(0,6):
    for j in range(0,i):
        print("*",end=" ")
    print("")

for i in range(0,6):
    print("* "*i)