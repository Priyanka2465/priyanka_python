# Write a Python script to sort (ascending and descending) a dictionary by value.
import operator
di={1:2,7:9,4:8}
sort=dict(sorted(di.items(),key=operator.itemgetter(1)))
print(sort)

descend=dict(sorted(di.items(),key=operator.itemgetter(1),reverse=True))
print(descend)
