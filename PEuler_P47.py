###https://projecteuler.net/problem=47
##Distinct primes factors

#it is prime?
def is_prime(x):
	if x == 2:
		return 1
	for i in range(2, int(x**0.5)+1):
		if x % i == 0:
			return 0
	return 1

result1 = []
i = 3

while True:
	i = i + 1
	result = []
	a = i

	#소인수 분해
	for j in range(2,i+1):
		if is_prime(j) == 1 and a % j == 0:
			while a > 1:
				result.append(j)
				a = a/j
				if a % j !=0:
					break
	result1.append([i,result,len(set(result))])

	#4 consecutive numbers have 4 distinct prime factors?
	if i > 10 and len(str(i)) == len(str(i-3)) and result1[i-4][2] == result1[i-5][2] == result1[i-6][2] == result1[i-7][2] == 4:
		print(result1[i-7], result1[i-6], result1[i-5], result1[i-4])
		break

	print(len(result1))
