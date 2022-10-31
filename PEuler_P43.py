###https://projecteuler.net/problem=43

#Sub-string divisibility

#make pandigital number from 0 to 9
from itertools import permutations

i1 = '0123456789'
i2 = []
i2 = list(map(''.join, permutations(i1)))

# NOT start with 0
i3 = []
for i in i2:
	if i[0] != '0':
		i3.append(i)

#check divisibility
result = set()
a4 = [2,3,5,7,11,13,17]

for a1 in i3:
	a3 = 0
	for i in range(1,len(a1)-3+1):
		a2 = int(a1[i:i+3])
		a3 += a2%a4[i-1]
		
		if a3 > 0:
			break

	if a3 == 0:
		result.add(int(a1))

print(sum(result))
