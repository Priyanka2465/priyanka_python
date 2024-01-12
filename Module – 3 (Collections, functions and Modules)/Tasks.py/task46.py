# Write a Python program to read a random line from a file..
import random

file=open("test.txt","r")
lines = file.read().splitlines()
print(random.choice(lines))
file.close()