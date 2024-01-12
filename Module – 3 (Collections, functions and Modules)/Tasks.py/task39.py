# Write a Python program to find the highest 3 values in a dictionary...
d={"a":1,"b":2,"c":3,"d":4}
di=sorted(d,key=d.get,reverse=True)
print(di[:3])