###https://projecteuler.net/problem=35

'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
from math import sqrt

#check the number is prime or not (1 = prime, 0 = not)
def is_prime(x):
	if x == 2:
		return 1
	
	for i in range(2, int(sqrt(x))+1):
		if x % i == 0:
			return 0

	return 1


result = set()

#find cicuralar prime number!
for i in range(2,10**6):
	#it is prime?
	if is_prime(i) == 1 and i not in result:
		# if so, make rotational numbers (caution, not every combination)
		i1 = str(i)
		a = []
		for c in range(0,len(i1)):
			i2 = int(i1[1:]+i1[0])
			i1 = i1[1:]+i1[0]
			a.append(i2)

		#all rotation numbers is prime?
		count = 0
		for j in a:
			if is_prime(j) == 1:
				count += 1
			else:
				break

		if count == len(i1):
			print(f'{i}, {a}')
			#if so!
			for k in a:
				result.add(k)

print(f'haw many? = {len(result)}')
