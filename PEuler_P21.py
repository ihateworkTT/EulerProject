###https://projecteuler.net/problem=21



#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

#make function
def d(x):
	result = []
	a = 0
	for i in range(1,x):
		if x % i == 0:
			result.append(i)
	for i in result:
		a = a + i
	return  a

#find amicable numbers under 10,000
a = 0
result = []

while a < 10000:
	a = a + 1
	b = d(a)

	if d(b) == a and a != b:
		print(a, b, d(b))
		result.append(a)
	else:
		pass

#sum of all amicable numbers
print(result)
a1 = 0
for a in result:
	a1 += a

print(a1)