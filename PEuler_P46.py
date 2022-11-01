###https://projecteuler.net/problem=46
###Goldbach's other conjecture

#make funtion, it is prime number?
def is_prime(x):
	if x == 2:
		return 1
	
	for i in range(2, int(x**0.5)+1):
		if x % i == 0:
			return 0

	return 1


Gold_right = []
Gold_wrong = []

#check all odd number
for i in range(9,10000 ,2):
	# i is NOT prime number
	if is_prime(i) == 0:
		for j in range(i,1, -1):
			gold = ((i - j) / 2)**0.5
			# Goldbach conjecture is right?
			if is_prime(j) == 1 and gold % 1 == 0:
				print(f'{i} = {j} + 2 * {gold}^2')
				Gold_right.append(i)
				break
		# Goldbach conjecture is wrong?
		if i not in Gold_right:
			Gold_wrong.append(i)
	#if found wrong number, break the loop
	if len(Gold_wrong) > 0:
		break

print(Gold_wrong)