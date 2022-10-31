###https://projecteuler.net/problem=37

'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

#make funtion, it is prime number?
def is_prime(x):
	if x == 0:
		return 0

	if x == 1:
		return 0

	if x == 2:
		return 1
	
	for i in range(2, int(x**0.5)+1):
		if x % i == 0:
			return 0

	return 1

result = []
i = 11
while len(result)<11:
	i_left = 0
	i_right = 0
	i = i+2
	# if i is prime number
	if is_prime(i) == 1:
		i1 = str(i)
		# is it truncatable prime???
		for j in range(1, len(i1)):
			#from left to right
			if is_prime(int(i1[j:])) == 0:
				break
			else:
				i_left += is_prime(int(i1[j:]))
			# from right to left
			if is_prime(int(i1[:-j])) == 0:
				break
			else:
				i_right += is_prime(int(i1[:-j]))

		# only peak both side truncatable prime number
		if i_left == i_right == len(i1)-1:
			result.append(i)

print(f'sum = {sum(result)}')