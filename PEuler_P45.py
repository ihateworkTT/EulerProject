###https://projecteuler.net/problem=45
#Triangular, pentagonal, and hexagonal

limit = 55385

#make triangular 
tri = []
for i in range(1,limit+1):
	t = i * (i+1) / 2
	tri.append(t)

#make pentagonal
pen = []
for i in range(1,limit+1):
	p = i * (3*i-1) / 2
	pen.append(p)

#make hexagonal
hexa = []
for i in range(1,limit+1):
	h = i * (2*i-1)
	hexa.append(h)


#triange + penta + hexa?
for i in tri:
	if i in pen and i in hexa and i > 40755:
			print('pen & hexa', i)
			print(tri.index(i),pen.index(i),hexa.index(i))
			break