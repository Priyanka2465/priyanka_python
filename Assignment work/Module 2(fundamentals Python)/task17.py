#Write a Python function that takes a list of words and returns the length of the longest one.
l=["java","php","python"]
le=[]
for i in l:
    le.append((len(i),i))
le.sort()
print(le[-1][0],le[-1][1])
