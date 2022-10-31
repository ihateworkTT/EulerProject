###https://projecteuler.net/problem=41

'''
Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

#make funtion, it is prime number?
def is_prime(x):
	if x == 0:
		return 0

	if x == 1:
		return 0

	if x == 2:
		return 1
	
	for i in range(2, int(x**0.5)+1):
		if x % i == 0:
			return 0

	return 1

#get all combination n-digit

from itertools import permutations

i1 = ''
i2 = []
ans = 0
for i in range(1,10):
	i1 = i1 + str(i)
	i2 = list(map(''.join, permutations(i1)))
	for j in i2:
		j1 = int(j)
		#is it prime number?
		if is_prime(j1) == 1:
			#is it largest?
			if ans < j1:
				ans = j1

print(f'the largest n-digit pandigital prime that exists is {ans}')