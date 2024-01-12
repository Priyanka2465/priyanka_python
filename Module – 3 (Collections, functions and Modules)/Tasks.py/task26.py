# Write a Python program to unzip a list of tuples into individual lists...
li=[(1,2),(3,4),(5,6)]
r=list(zip(*li))
print(r)