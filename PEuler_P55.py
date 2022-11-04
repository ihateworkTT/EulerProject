###https://projecteuler.net/problem=55
##Lychrel numbers

for i in range(1,10001):
	i = i

#is it Lycherl number?
def lyc_num(x):
	i = x
	n = 0
	while n < 50:
		n += 1

		x1 = str(x)
		x2 = x1[::-1]
		x3 = int(x1) + int(x2)

		if str(x3) == str(x3)[::-1]:
			break
		else:
			x = x3

	#if not lycherl number, return 0
	if n < 50:
		return 0

	#if so, return 1
	return 1


#Let'find how many Lycherl number
a = 0
for i in range(1,10001):
	a += lyc_num(i)

print(a) 