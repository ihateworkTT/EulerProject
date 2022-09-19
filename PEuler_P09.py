###https://projecteuler.net/problem=9


#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

a = 1
b = 2
c = 3

import math

while a + b + c != 1000:
#while b < 1000:
	for a in range(1, b):
		c  = a*a + b*b
		c1 =  math.sqrt(c)
		
		if c1.is_integer():
			if  a + b + c1 == 1000:
				print('a=',a,'b =',b,'c =',c1)
				print('answer =',a*b*c1)
				break
	b = b + 1


