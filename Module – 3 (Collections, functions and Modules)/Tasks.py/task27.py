#  Write a Python program to convert a list of tuples into a dictionary. 
li=[(102,"Piyu"),(103,"Dhanu"),(101,"Foram")]
dict={}
for a,b in li:
    dict.setdefault(a,b)
print(dict)
