###https://projecteuler.net/problem=39

'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

'''

p = 4
solutions = 0
num = 0

while p < 1001:
	#set a range
	#initiate N
	n = 0
	for i in range(1,int(p/3)):
		# set b range
		for j in range(1,int(p/3*2)):
			a = i
			b = j
			c = p-a-b
			if a <= b < c:
				# is it right angle triangle?
				if a*a + b*b == c*c:
					n = n + 1
					print(a,b,c,n)

	#what is the max number 
	if solutions < n:
		solutions = n
		num = p

	p = p + 1

print(f'p == {num}, solutions = {solutions}')