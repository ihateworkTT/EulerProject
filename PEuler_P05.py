###https://projecteuler.net/problem=5

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = 20
a = 1

#find Least common multiple of two numbers
for i in range(2,n+1):
	for j in range(2, a+1):
		if a % i !=0:
			if i % j == 0 and a % j ==0:
				a = j * (i/j) * (a/j)
				a = int(a)
				break
		else:
			a = a
			break
	else:
			a = i * a
print(a)

###https://eclipse360.tistory.com/23

import math

LCM = 1

for i in range(1, 21):
	GCD = math.gcd(i, LCM)
	LCM = int(i*LCM/GCD)
	print(i, LCM)