# Write a Python program to replace last value of tuples in a list...
li=[(1,2,3,4),(2,6,9,1)]
for t in li:
    print(t[:-1]+(100,))