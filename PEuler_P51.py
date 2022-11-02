###https://projecteuler.net/problem=51
##Prime digit replacement

from itertools import permutations, combinations

#is prime number?
def is_prime(x):
	if x == 2:
		return 1

	for i in range(2, int(x**0.5)+1):
		if x % i == 0:
			return 0

	return 1

#pick prime numbers
result = []
for i in range(55981,120385,2):
	if is_prime(i) == 1:
		result.append(i)

for i in result:
	i1 = str(i)
	i2 = list(range(0,len(i1)))
	for j in range(1,len(i2)):
		#make combinations
		for k in combinations(i2,j):
			count = 0
			i5 = []
			for l in range(0,10):
				i3 = []
				for m in i2:
					if m in k:
						#repeat ** -> 00,11,22,.....
						i3.append(str(l))

					else:
						i3.append(i1[m])
				i4 = int("".join(i3))

				#it is also prime?
				if i4 > 10000 and is_prime(i4) == 1:
					i5.append(i4)
					print(i5)

				#8 prime value family??
				if len(i5) > 7:
					print(i1,k,i5,len(i5))
					break

