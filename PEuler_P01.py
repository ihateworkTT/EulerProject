###https://projecteuler.net/problem=1

n = 0
result = 0

while n < 999:
	n += 1
	if n % 3 == 0 or n % 5 == 0:
		result += n

print(result)