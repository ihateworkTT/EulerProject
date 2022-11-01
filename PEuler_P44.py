###https://projecteuler.net/problem=44
## Pentagon numbers

limit = 2500

pn_list = []
#make pentagon numbers
for i in range(1,limit+1):
	p = i*(3*i - 1)/2
	pn_list.append(p)

#sum or diffence is pen??
#sum
for i in pn_list[1000:]:
	for j in pn_list[2100:]:
		psum = i + j
		pdif = j - i
		#sum is pentagon number?
		if i <= j and psum in pn_list and pdif in pn_list:
			print(f'sum = {psum} \n diff = {pdif}')
			break

			
