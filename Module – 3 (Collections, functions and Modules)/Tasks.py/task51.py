# Write a Python program to returns sum of all divisors of a number..
number=12
divisors = []
for i in range(1, number):
    if (number % i)==0:
        divisors.append(i)
print(divisors)
print(sum(divisors))