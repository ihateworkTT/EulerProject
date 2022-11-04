###https://projecteuler.net/problem=56
##Powerful digit sum

limit = 100
ans = 0
for i in range(1,limit):
	for j in range(1,limit):
		a2 = str(i**j)
		po_sum = 0
		for a1 in a2:
			po_sum += int(a1)

		if ans < po_sum:
			ans = po_sum
			a = i
			b = j

print(a,b,a**b, ans)
