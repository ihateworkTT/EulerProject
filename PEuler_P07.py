###https://projecteuler.net/problem=7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

i = 2
a = 2
b = [2]

while len(b) < 10001:
	a = a + 1 
	b.append(a)
	for i in b:
		if i > 1 and a % i == 0 and a != i:
			b.remove(a)
			break

print(b[10000])

 