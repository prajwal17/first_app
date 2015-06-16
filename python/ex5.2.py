def calc():
	maxi=0
	mini=100
	while True:
		n=raw_input("Enter an number:")
		if n=='done':
			print maxi,mini
			break
		else:
		
		  try:
	           	
		   	if n <=mini:
			 mini=n
		   	if n >maxi:
			 maxi=n
		   
		  except:
			print "Invalid number"
			continue
calc()
