###https://projecteuler.net/problem=58
##Spiral primes
#is prime number?
def is_prime(x):
	if x == 2:
		return 1

	for i in range(2, int(x**0.5)+1):
		if x % i == 0:
			return 0

	return 1

a = 0
i = 2
a1 = 4

while True:
	diag = []

	for j in range(0,4):
		j1 = ((i+1)**2) - (i*j)
		diag.append(j1)
	
	for d in diag:
		a += is_prime(d)

	if a / a1 *100 < 10:
		print(f'{a}/{a1} = {a/a1*100}%')
		print(f'side length = {i- 1}')
		break
	
	print(i, a/a1*100, '%')
	i += 2
	a1 += 4

