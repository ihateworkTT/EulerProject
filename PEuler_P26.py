###https://projecteuler.net/problem=26
'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.'''

def check_cycle(d):
	remain_list = list()
	dividend = 1
	n = 0

	while True:
		remain = dividend % d #나머지?

		if remain in remain_list:
			return n - remain_list.index(remain)
		else:
			remain_list.append(remain)
			dividend = remain * 10
			n += 1


a = 0
result = []
for i in range(1, 1001):
	
	if a < check_cycle(i):
		a = check_cycle(i)
		d = i
		result.append([i,a,1/i])

print(a,d)
