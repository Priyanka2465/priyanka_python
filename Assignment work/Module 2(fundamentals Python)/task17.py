#Write a Python function that takes a list of words and returns the length of the longest one.
l=["java","php","python"]
l_len=[]
for i in l:
    l_len.append((len(i),i))
l_len.sort()
print(l_len[-1][0],l_len[-1][1])
