###https://projecteuler.net/problem=22


#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?

#open file
f = open('p022_names.txt','r')
a = f.read()
f.close()

#remove '"' and split ',' and return to list
a = a.replace('"','')
a = a.split(',')
#sorting 
a = sorted(a)

dic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

score = 0
name_score = []
for i in range(0,len(a)):
	score = 0
	for j in range(0,len(a[i])):
		for k in range(0,26):
			if a[i][j] == dic[k]:
				score = score+k+1
	name_score.append((i+1)*score)

#sum
a1 = 0
for i in name_score:
	a1 = a1 + i
print(a1)