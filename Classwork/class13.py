#dict in-build function...

d={101:"Priyanka",102:"Dhanu"}
print(d)
print(d.get(101))
print(d.items())
print(d.keys())
d.popitem()
print(d)

# d.pop(102)
# print(d)

d.update({103:"Foram",104:"Avni"})
print(d)
print(d.values())



t=[1,2,3,4]
dict.fromkeys(t)
print(dict)

