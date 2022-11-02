###https://projecteuler.net/problem=50
##Consecutive prime sum

#is prime number?
def is_prime(x):
	if x == 2:
		return 1

	for i in range(2, int(x**0.5)+1):
		if x % i == 0:
			return 0

	return 1

## found prime numbers below 1m
result = []
for i in range(2,10**6):
	if is_prime(i) == 1:
		result.append(i)

a = 2
a1 = []

#let's find sum of the most consecutive primes
while True:
	for i in range(0,len(result)-a):
		a2 = result[i:i+a]
		a3 = sum(a2)
		if is_prime(a3) == 1 and len(a2) >= len(a1) and a3 < 10**6:
			a1 = a2
			print(f'{i+1} out of {len(result)} //  contain {len(a2)} terms, sum = {a3}')
		elif a3 > 10**6:
			break
		else:
			pass

	a = a + 1
	if a > len(result)-1:
		break

print(a1, len(a1), sum(a1))

