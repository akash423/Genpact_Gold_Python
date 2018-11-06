#!/usr/bin/python

try:
	hours = input('Enter Hours ')
	rate = input('Enter Rate ')
	h = float(hours)
	r = float(rate)
	if h > 40.0 :
		ot = h - 40.0
		otRate = r * 1.5
		print ("OT Hours: ", ot)
		print ("OT Rate: ", otRate)
		otPay = ot * otRate
		pay = (40.0 * r) + otPay
		print ("OT Pay: ", otPay)
		print ("Total Pay: ", pay)
	else:
		pay = h * r
		print (pay)
except:
	print ("Enter valid numeric input")