#LECTURE 13

# definite loops use for

# print a string vertically
s = "abc"
for c in s :
    print (c)

# testing ranges

for i in range (5):
    print (i, end = " ")    #5 is  excluded the count starts from 0 to
print ()

for q in range (1, 5):
    print (q, end = " ")    #0 is  excluded the count starts from 1 to 5
print ()

# print the numbers from 0 to 9 in steps of 3
for w in range (0, 10, 3 ):
    print (w, end = " ")
print ()

# print the numbers from 10 to 1 in one line
for x in range (10, 0, -1 ):
    print (x, end = " ")
print ()

#lecture 13.2 in class example
#print a line of hashes
n = int (input ("Enter a number:"))
for i in range (n):
    #the end in this instance is making the program stop printing on a new line
    print ("#", end="")
print ()

#creating a rectangle
rows = int (input("Enter value for rows "))
cols = int (input ("Enter value for the colums "))

for i in range (rows):
    for j in range (cols):
        print ("O", end="")
        #first arg in print is to print "O", connected to rows
        #sec arg is end="" connected to cols move to a next line
        #and keeps printing
    print ()        #move to next line

#read a string, print the number of charecters in the string that are decimal digits

n=0
s = input ("Enter a STRING")
for c in s :
    if '0'<=c <= '9':   #if there is a num between 0 or 9, count it += 1
        n += 1
print ("Number of digits=",n)

