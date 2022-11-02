###https://projecteuler.net/problem=52
##Permuted multiples

a = 1

while True:
	#make x,2x,3x,4x,5x,6x
	x = []
	for i in range(1,7):
		x.append(a*i)
	#sorting
	x1 = []
	for i in x:
		x1.append(''.join(sorted(str(i))))
	#contain the same digits???
	count = 0
	for i in range(1,len(x1)):
		if x1[0] == x1[i]:
			count += 1
	#if so, break
	if count == len(x1)-1:
		print(x,x1)
		break

	a += 1