
#ABS allows to call a function in this case it is K and print it
k = 90
print (abs(k))

#it has dropped the minus sign here slight issues
l = -80
print (abs(l))

#you can print the range using this function
for m in range (1,3): print (m)

#this adds a seperator of a comma and the end function
#finishes with a fullstop and start a new line
print (1,2,3, sep = ', ', end = '.\n')

#removes the white spaces
print ('    spacious   '.strip())

#checks is the line has digits and returns true
print ("123". isdigit())

#counts the number of letters and spaces
print (len ("this is a sentence"))

#learning formatting
#when printed the ans is 3.3333333
dollar = 10.0 / 3
print (dollar)

#format it into two decimal places
#this formats the decimal place and addes the dollar sign
dollars = 10.0 / 3
print ("dollars = ${:.2f}".format (dollars))

#call a variable and i to print
for i in range (1,5): print (i)

#not working because of args
"{2} {1} {0}".format(10, 20, 30)
"{2:d} {1:d} {0:d} ".format (10,20,30)


#imports the library prog before starting
import math

x = 10 / 3
print("x = {:.4f}".format(x))
#ceiling of x always rounds things to positive infinity
#{:.4f} meaning four decimal places
print("ceil(x) = {:.4f}".format(math.ceil(x)))
#floor rounds things up to negative infinity
print("floor(x) = {:.4f}".format(math.floor(x)))

#import selective things from lib
from math import ceil, floor

x = 10 / 3
print("x = {:.4f}".format(x))
print("ceil(x) = {:.4f}".format(ceil(x)))
print("floor(x) = {:.4f}".format(floor(x)))
