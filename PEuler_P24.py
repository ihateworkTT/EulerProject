###https://projecteuler.net/problem=24

#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def factorial(x):
	a = 1
	for i in range(x,1,-1):
		a = a*i
	return a

# 9..8..7.. -> found 1Mth!
a1 = [0,1,2,3,4,5,6,7,8,9]
a = 0
b = ''

for i in range(0,10):
	count = 0
	for j in range(0,10):
		if a < 10**6:
			a = a + factorial(9-i)
			count = count + 1
		else:
			a = a - factorial(9-i)
			count = count - 1
			break
	
	b = b + str(a1[count])
	a1.remove(a1[count])

print(b)