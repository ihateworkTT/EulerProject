###https://projecteuler.net/problem=17

#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


dic = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven',  12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17: 'seventeen', 18:'eighteen', 19:'nineteen', 20: 'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'onethousand'}
a = 0

for i in range(1,101): #1-100
	if i in dic:
		a = a + len(dic[i])
	else:
		a = a + len(dic[i-i%10]+dic[i%10])

for i in range(101,1000): #101-999
	if i % 100 == 0: #200,300,400...
		a = a + len(dic[i//100] + dic[100])
	elif i%100 in dic:
		a = a + len(dic[i//100]+dic[100]+dic[i%100]) + 3
	else:
		a = a + len(dic[i//100] + dic[100] + dic[(i-i//100*100)//10*10]+dic[i%10])+  3

a = a + len(dic[1000]) #1,000
	
print('answer = ',a +  len(dic[1]))
