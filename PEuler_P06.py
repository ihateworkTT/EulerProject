###https://projecteuler.net/problem=6

#The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
# (1+2+3...+10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n=100
a1 = 0
a2 = 0
for i in range(1,n+1):
	a1 = a1 + i
	a2 = a2 + (i*i)
	result = a1*a1 - a2

print(result)