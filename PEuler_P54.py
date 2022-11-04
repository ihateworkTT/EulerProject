###https://projecteuler.net/problem=54
##Poker hands

#open file
f = open('p054_poker.txt','r')
a1 = f.readlines()
f.close()


#make function sorting following card order
def srt(x):
	order = '23456789TJQKA'
	i1 = []
	i2 = ''
	i3 = ''
	for i in x:
		if i in order:
			i1.append(order.index(i))
	i1.sort()

	for i in i1:
		i2 = i2 + order[i] 

	i3 = x[1::2]

	return i2 + i3

#Let get score, if have poker pair and get hiest card value
def get_score(x):
	order = '23456789TJQKA23456'
	score = 0
	value = 0
	Highest = 0

	#Royal Flush
	if x[:5] == order[-5:] and x[5] == x[6] == x[7] == x[8] == x[9]:
		score = 9	
		return score, value, Highest

	#Straight Flush
	if x[:5] in order and x[5] == x[6] == x[7] == x[8] == x[9]:
		score = 8
		return score, value, Highest

	#Four of a Kind
	if x[0] == x[1] == x[2] == x[3] or x[1] == x[2] == x[3] == x[4]:
		score = 7
		if x[0] == x[1] == x[2] == x[3]:
			value = order.index(x[0]) + 1
			Highest = order.index(x[4]) + 1
		else:
			value = order.index(x[1]) + 1
			Highest = order.index(x[0]) + 1

		return score, value, Highest

	#Full House
	if x[0] == x[1] == x[2] and x[3]==x[4] or x[1] == x[2] == x[3] and x[0]==x[4] or x[2] == x[3] == x[4] and x[0]==x[1]:
		score = 6
		if x[0] == x[1] == x[2] and x[3]==x[4]:
			value = order.index(x[0]) + 1
			Highest = order.index(x[3]) + 1
		elif x[1] == x[2] == x[3] and x[0]==x[4]:
			value = order.index(x[1]) + 1
			Highest = order.index(x[0]) + 1
		else:
			value = order.index(x[2]) + 1
			Highest = order.index(x[0]) + 1

		return score, value, Highest
	
	#Flush
	if x[5] == x[6] == x[7] == x[8] == x[9]:
		score = 5
		value = order.index(x[4]) + 1

		return score, value, Highest

	#Straight
	if x[:5] in order:
		score = 4
		value = order.index(x[4]) + 1
		return score, value, Highest

	#Three of Kind
	if x[0] == x[1] == x[2] or x[1] == x[2] == x[3] or x[2] == x[3] == x[4]:
		score = 3
		if x[0] == x[1] == x[2]:
			value = order.index(x[0]) + 1
			Highest = order.index(x[4]) + 1
		elif x[1] == x[2] == x[3]:
			value = order.index(x[1]) + 1
			Highest = order.index(x[4]) + 1
		else:
			value = order.index(x[2]) + 1
			Highest = order.index(x[1]) +1

		return score, value, Highest

	#Two Pairs
	if x[1] == x[2] and x[3] == x[4] or x[0] == x[1] and x[3] == x[4] or x[0] == x[1] and x[2] == x[3]:
		score = 2
		if x[1] == x[2] and x[3] == x[4]:
			value = order.index(x[3]) + 1
			Highest = order.index(x[0]) + 1
		elif x[0] == x[1] and x[3] == x[4]:
			value = order.index(x[3]) + 1
			Highest = order.index(x[2]) + 1
		else:
			value = order.index(x[2]) + 1
			Highest = order.index(x[4]) + 1

		return score, value, Highest

	#One Pairs
	if x[0] == x[1] or x[1] == x[2] or x[2] == x[3] or x[3] == x[4]:
		score = 1

		if x[0] == x[1]:
			value = order.index(x[0]) + 1
			Highest = order.index(x[4]) + 1
		elif x[1] == x[2]:
			value = order.index(x[1]) + 1
			Highest = order.index(x[4]) + 1
		elif x[2] == x[3]:
			value = order.index(x[2]) + 1
			Highest = order.index(x[4]) + 1
		else:
			value = order.index(x[3]) + 1
			Highest = order.index(x[2]) + 1

		return score, value, Highest

	Highest = order.index(x[4]) + 1
	return score, value, Highest

#data cleaning, seperate by lines and remove blank and \n
poker = []
for line in a1:
	line = line.strip()
	line = line.replace(" ",'')
	poker.append(line)

p1_win = 0
p2_win = 0
count = 0

for a1 in poker:

	#seprate by players
	p1 = []
	for i in range(0,5):
		p1.append(a1[i*2:(i+1)*2])

	p2 = []
	for i in range(5,10):
		p2.append(a1[i*2:(i+1)*2])
	
	#str is more convenient?
	p1s = a1[:10]
	p2s = a1[10:]
	p1_score = get_score(srt(p1s))
	p2_score = get_score(srt(p2s))

	#compare P1 vs P2
	# compare ranks
	if p1_score[0] > p2_score[0]:
		p1_win += 1
	elif p1_score[0] < p2_score[0]:
		p2_win += 1

	#if have the same rank, compare the rank cards value
	elif p1_score[1] > p2_score[1]:
		p1_win += 1
	elif p1_score[1] < p2_score[1]:
		p2_win += 1

	#if have the same rank cards value, compare rest card value, which is the highest?
	elif p1_score[2] > p2_score[2]:
		p1_win += 1
	elif p1_score[2] < p2_score[2]:
		p2_win += 1
	else:
		print(f'P1 = {p1} = P2 = {p2}, {poker.index(a1)}')

print(p1_win + p2_win)
print(f'how many p1 win = {p1_win} // how many p2 win = {p2_win}')
