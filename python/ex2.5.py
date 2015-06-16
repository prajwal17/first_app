input=float(raw_input('Enter the temperature in celcius\n'))
try :
m=(input * 1.80) + 32.00
print ('%0.1f degree celcius is equal to %0.1f fahrenheit ' %(input,m))
print m
except :
print 'Enter the valid value'
