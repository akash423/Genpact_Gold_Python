#!/usr/bin/python


def PayOut(h, r):
	try:
		if float(h) > 40.0:
			ot = float(h) - 40.0
			otRate = float(r) * 1.5
			otPay = ot * otRate
			pay = (float(r) * 40.0) + otPay
			return pay
		elif float(h) < 40.0:	
			x = (float(h) * float(r))
			return x
	except:
		print ("invalid input")
		
h = input('Enter Hours ')
r = input('Enter Rate ')


pay = PayOut(h, r)

print (str(pay))

