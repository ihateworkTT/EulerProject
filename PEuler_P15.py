###https://projecteuler.net/problem=15

#40C20
a =  1
#n!
for i in range(40,1,-1):
	a  = a *i

#r!
a1 = 1
for i in range(20,1,-1):
	a1 = a1 * i

#n-r = 20! =  a1

print(a/(a1*a1))

##### I  don't understand 
def binom(n, m):
     b = [0] * (n + 1)
     b[0] = 1
     for i in range(1, n+1):
             b[i] = 1
             j = i - 1
             while j > 0:
                     b[j] += b[j-1]
                     j -= 1
     return b[m]

print(binom(40,20))