###https://projecteuler.net/problem=36

'''
The decimal number, 585 = 1001001001^2 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

result = []

# convert 10 to binary number
for a in range(1,10**6):
	a4 = str(a)
	#base 10 number is palindromic?
	if a4[0:]==a4[::-1]:
		x = 0
		a3 = a

		while a // 2**x > 1:
			x += 1  
		
		a1 = ''
		for i in range(x,-1,-1):
			a2 = 2**i
			if a - a2 >= 0:
				a = a-a2
				a1 = a1 + '1'
			else:
				a1 = a1 + '0'

		a5 = str(a1)
		#base 2 number is palindromic?
		if a5[0:]==a5[::-1]:
			#print(a3,a1)	
			result.append(a3)

print(f'sum = {sum(result)}')
