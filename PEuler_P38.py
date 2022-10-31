###https://projecteuler.net/problem=38
'''


Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''


n = []
for j in range(1,10000):
	a1 = ''
	for i in range(1,9):
		#make concatenated product
		a1 = a1 + str(j*i)

		if len(a1) > 9:
			break

		#check it is pandigital
		elif len(a1) == 9:
			a2 = ''.join(sorted(a1))
			if a2 == '123456789' and i > 1:
				print(j, a1, a2)
				n.append(int(a1))
				break

		else:
			pass



print(f'{max(n)} of {j} and (1, ... {i})')