###https://projecteuler.net/problem=59
##XOR decryption

from itertools import product

#open file
f = open('p059_cipher.txt','r')
a1 = f.readlines()
f.close()

for a in a1:
	cipher = a.split(',')

#make all possible keys
p = 'abcdefghijklmnopqrstuvwxyz'
p4 = []
for p1 in p:
	for p2 in p:
		for p3 in p:
			p4.append([p1,p2,p3])


#Encryption
result = []
for j in p4:
	ans = ''
	for i in range(0,len(cipher)):
		if i % 3 == 0:
			#XOR
			xor = int(cipher[i])^ord(j[i%3])
			#XOR -> character ASCII
			ans += chr(xor)
		elif i % 3 == 1:
			xor = int(cipher[i])^ord(j[i%3])
			ans += chr(xor)
		else:
			xor = int(cipher[i])^ord(j[i%3])
			ans += chr(xor)

	result.append([j,ans])

	if 'the' in ans and '*' not in ans and '=' not in ans:
		print(f'key = {j[0]+j[1]+j[2]}, message = {ans} \n')
		m1 = ans


#let sum ASCII valuse in the original text

sum_m = []
for m in m1:
	sum_m.append(ord(m))

print(f'sum = {sum(sum_m)}')	

