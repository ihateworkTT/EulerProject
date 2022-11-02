###https://projecteuler.net/problem=53
## Combinatoric selections

#factorial
def fact(x):
	a = 1
	for i in range(1,x+1):
		a = a * i

	return a

result = []
limit = 100

for n in range(1,limit + 1):
	for r in range(1,limit + 1):

		#calculate combination
		com = fact(n)/(fact(r)*fact(n-r))

		# com is greater than 1m?
		if com > 10**6:
			result.append([n,r,com])
			print(f'n = {n}, r = {r}, value = {com}, how many = {len(result)}')