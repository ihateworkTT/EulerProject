###https://projecteuler.net/problem=49
##prime permutations

from itertools import permutations 
from itertools import combinations

#is prime number?
def is_prime(x):
	if x == 2:
		return 1

	for i in range(2, int(x**0.5)+1):
		if x % i == 0:
			return 0

	return 1

#found 4 digit prime numbers
result = []
for i in range(1000,10000):
	if is_prime(i) == 1:
		result.append(i)

#make group 4-digit permutations, consist of prime number
result2=[]
for i in result:
	i1 = ''.join(sorted(str(i)))
	result1=[i]
	for j in result:
		j1 = ''.join(sorted(str(j)))
		if i < j and i1 == j1:
			result1.append(j)

	result2.append(result1)

#check the sequence, remove less than 2 permuations prime numbers
result1 = []
for i in range(0,len(result2)):
	if len(result2[i]) > 2:
		result1.append(result2[i])

#let's find both satisfactory (prime number & sequence)
for i in result1:
	i1 = combinations(i,3)
	for i2 in i1:
		if i2[0]-i2[1] == i2[1]-i2[2]:
			print(i2)

