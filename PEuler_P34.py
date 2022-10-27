###https://projecteuler.net/problem=34

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

#factorial (!)
def fact(x):
	a = 1
	for i in range(1,x+1):
		a = a*i
	return a

x = 3
result = []

#let's find the number
while len(result) < 2:
	a1 = 0
	for i in str(x):
		a1 += fact(int(i))

	if x == a1:
		print(x)
		result.append(x)

	x = x+1

print(f'sum = {sum(result)}')