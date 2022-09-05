###https://projecteuler.net/problem=4

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

result = []

for i in range(1,1000):
	for j in range(1,1000):
		b = i * j
		# check weather palindromic number is (121 == 121? 123 == 321??)
		if str(b) == str(b)[::-1]:
			result.append(b)

print(max(result))

