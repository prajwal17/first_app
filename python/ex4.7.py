input=float(raw_input('Enter score:'))

def comp():
	if (input > 0.9 and input< 10.0):
		print 'A'
	elif input>0.8 and input< 10.0:
		print 'B'
	elif input>0.7 and input< 10.0:
		print 'C'
	elif input>0.6 and input< 10.0:
		print 'D'
	elif input<=0.6:
		print 'F'
	else:
		print 'bad Score'

comp()
