###https://projecteuler.net/problem=20

#n! means n × (n − 1) × ... × 3 × 2 × 1

#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!


n = 100
a = 1
for i in range(1,n+1):
	a = a * i

a2 = 0
for a1 in range(0,len(str(a))):
	a2 = a2 + int(str(a)[a1])

print(a, a2)