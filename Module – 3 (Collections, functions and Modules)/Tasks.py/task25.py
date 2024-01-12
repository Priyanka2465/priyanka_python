# Write a Python program to remove an empty tuple(s) from a list of tuples.
li=[(),(1,2),(3,4),()]
li=[t for t in li if t]
print(li)
