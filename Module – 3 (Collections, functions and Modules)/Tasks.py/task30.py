# Write a Python script to concatenate following dictionaries to create a new one...
di1={1:2,4:3}
di2={2:3,5:1}
di={}

for i in di1,di2:
    di.update(i)
print(di)