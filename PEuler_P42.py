###https://projecteuler.net/problem=42

#Coded triagle numbers

#get trianlge numbers (how many? 100?)
tri_num = []
for i in range(0,100):
	t = 1/2*i*(i+1)
	tri_num.append(t)

#open file
f = open('p042_words.txt','r')
a = f.read()
f.close()

#remove '"' and split ',' and return to list
a = a.replace('"','')
a = a.split(',')

#the word list is ready!

#word -> word value

count = 0
for i in a:
	a1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	wv = 0
	for j in i:
		wv += a1.index(j)+1

	#wv is the triangle number?
	if wv in tri_num:
		count = count + 1

print(f'how many are trangle word? {count}')
