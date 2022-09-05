###https://projecteuler.net/problem=1

a = 600851475143
n = 2

while a > 1:
	if a % n == 0:
		a /= n
	elif a == 1:
		break
	else:
		n += 1

print(n)

