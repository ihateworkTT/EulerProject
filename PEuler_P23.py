###https://projecteuler.net/problem=23



#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

#search divisors (제곱이면 약수가 중복되서 들어갔었음)
def dvs(x):
	result = [1]
	limit = int(x**0.5)+1
	for i in range(2,limit):
		if x % i == 0:
			result.append(i)
			result.append(x/i)

	a = sum(set(result))
	return a


#find abundant number under 28123
limit = 28123
abd_num_list = []
for i in range(12, limit+1):
	if dvs(i) > i:
		abd_num_list.append(i)

#make list sum of abd nums
sum_abn = []
for i in abd_num_list:
	for j in abd_num_list:
		if i + j < limit + 1:
			sum_abn.append(i+j)
#remove same number
sum_abn = list(set(sum_abn))

#Remove sum of abd nums
a = list(range(1,limit+1))
for i in sum_abn:
	a.remove(i)

print(sum(a))