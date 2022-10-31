###https://projecteuler.net/problem=40

'''
Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

#make Champerowne's constant
i = 0
cc = ''
while len(cc)<10**6:
	i += 1
	cc += str(i)

#found dn
ans = 1
for i in range(0,7):
	ans = ans * int(cc[10**i-1])
	print(int(cc[10**i-1]))

print(f'd1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000 = {ans}')