###https://projecteuler.net/problem=19



#You are given the following information, but you may prefer to do some research for yourself.

#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

year = 1900
month = 1
date = 0
day = 0
DayOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


count = 0

while year < 2001 :
	date = date + 1
	day = day + 1
	#count if 1st day is sunday from 1901
	if year > 1900 and day % 7 == 0 and date ==1 : 
		count = count + 1
		print(year, month, date, 'sunday', count)

	if DayOfMonth[month-1] == date and month !=12:
		month = month + 1
		date = 0
	elif month == 12 and date == 31:
		year = year + 1
		#leap year
		if year % 4 == 0:
			DayOfMonth[1] = 29
		else:
			DayOfMonth[1] = 28
		month = 1
		date = 0
	else:
		pass



