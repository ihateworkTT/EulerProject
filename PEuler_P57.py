###https://projecteuler.net/problem=57
##Square root convergents

#sqrt 2 -> infinite fraction...
num = 1
den = 1
count = 0

#found rule!
for i in range(0,1000):
	a = den*2 + num
	b = den + num

	num = a
	den = b
	#num has more digit, count
	if len(str(num)) > len(str(den)):
		count += 1
		print(f'{a}/{b}\nhow many = {count}')
	