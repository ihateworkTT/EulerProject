###https://projecteuler.net/problem=32

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum
'''

limit=10**4

result=[]
for i in range(1,limit):
	i1 = str(i)
	a = set()
	for j in i1:
		a.add(j)

	if len(i1) == len(a) and '0' not in i1:
		result.append(i)

dupl_test = []
result2 = []

for i in result:
	for j in result:
		if i != j:
			a = str(i)+str(j)+str(i*j)
			a1 = set()
			a2 = int(i)
			a3 = int(j)
			a4 = a2 * a3
			for j in a:
				a1.add(j)

			if len(a) == len(a1) == 9 and '0' not in a and a4 not in dupl_test:
				print(a,a2,a3,a4)
				dupl_test.append(a4)
				result2.append(a)

print(sum(dupl_test))