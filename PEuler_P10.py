###https://projecteuler.net/problem=10

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

i = 2
a = 1
b = [2]

#while a < (2000000-1): 
#	a = a + 2
#	b.append(a)
#	for i in b:
#		if a % i == 0 and a != i:
#			b.remove(a)
#			#print(a)
#			break
#b1  = 0
#for i in b:
#	b1 = b1 + i

#print(b1)


#more faster..(why???)
primes=[2]
for i in range(3,2000001,2):
    prime = True
    for prime in primes:
        if prime > i**0.5:
            break
        if i%prime==0:
            prime=False
            break
    if prime:
        primes.append(i)
sum = 0
for prime in primes:
    sum += prime

print(sum)