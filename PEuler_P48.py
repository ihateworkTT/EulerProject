###https://projecteuler.net/problem=48

##Self powers

a = 0
for i in range(1,1001):
	a += (i**i)

print(str(a)[-10:])
