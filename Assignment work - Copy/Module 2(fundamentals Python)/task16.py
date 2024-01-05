#  Write a Python program to find the first appearance of the substring
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string

s=input("Enter string=")
s1=s.find("not")
s2=s.find("poor")
print(s)
print(s1)
print(s2)
if s[s1+4]==s[s2]:
    s3=s.replace("not poor","good")
    print(s3)
    