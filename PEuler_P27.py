###https://projecteuler.net/problem=27
'''
Euler discovered the remarkable quadratic formula:

It turns out that the formula will produce 40 primes for the consecutive integer values . However, when is divisible by 41, and certainly when

is clearly divisible by 41.

The incredible formula
was discovered, which produces 80 primes for the consecutive values

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

, where and

where
is the modulus/absolute value of
e.g. and

Find the product of the coefficients,
and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with . '''

#if it is prime = 1, not = 0
def is_prime(x):
	result = []
	limit = int(x**0.5 + 1)
	if x == 2 or x == 3:
		return 1
	elif x == 0 or x == 1:
		return 0
	else:
		for i in range(2,limit):
			if x % i == 0:
				result.append(i)
		if len(result) == 0:
			return 1
		else:
			return 0	



n = 0
a1 = 0
b1 = 0
for a in range(-999,1000):
	for b in range(-1000,1001):
		x = 0
		
		while x < 100 :
			num = x*x + a*x + b
			x = x + 1
			if is_prime(abs(num)) == 0:
				print(f'x2 + {a}x + {b}x -> x = {x-1}')
				if n < x-2:
					n = x-2
					a1 = a
					b1 = b
				break
			else:
				pass
				

print(f'x2 + {a1}x + {b1}x -> n = {n}')
print(f'coefficients = {a1 * b1}')