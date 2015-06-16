def calc():
 total=0
 count=0
 while True:
	num=raw_input("Enter a number:")
	if num=="done":
		print total,count,(total/count) 
		break
	else:
	     try:
		total+=float(num)
	     except:
		print "invalid input"

	count+=1
calc()
