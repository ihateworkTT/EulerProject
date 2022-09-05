###https://projecteuler.net/problem=2

f1 = 1
f2 = 1
result = []
f3 = f1 + f2

while f3 < 4*10**6:
	f3 = f1 + f2
	if f3 % 2 == 0:
		result.append(f3)
	
	f1 = f2
	f2 = f3

print(sum(result))

