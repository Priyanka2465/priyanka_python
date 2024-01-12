# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
# list of strings.

li=[1,2,3,4,5]
if len(li)>=2 or li[1]==li[-1]:
    print(len(li))
else:
    print(li)