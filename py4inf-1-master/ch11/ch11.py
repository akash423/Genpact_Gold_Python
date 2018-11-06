#!/usr/bin/python

import re

hand = open('mbox.txt')


for line in hand:
	line = line.rstrip()
	#if re.findall('^New Revision: ([0-9]*)', line) :
	x = re.findall('^New Revision: ([0-9]*)', line)

	if len(x) > 0 : 
		#print line
		print x
		
	
		




#New Revision: 39772

		
		