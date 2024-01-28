# Write a Python program to write a list to a file....
l=["\nPriyanka","Piyu","Hello"]
file=open("test.txt","a")
file.writelines(l)
file.close()