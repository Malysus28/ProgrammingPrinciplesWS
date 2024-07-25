#write a program that reads whole numbers typed by the user
# until a zero is entered, then pritnts the number of positive numbers
#that were entered
cnt= 0
num= int(input("Enter a whole number (enter 0 to stop): "))

while num !=0:      #while num is not 0 continue loop
    if num > 0:     #while num is greater than 1
        cnt +=1     #increment pos  count by 1
        num = int(input("Enter a whole number (enter 0 to stop): "))
        #continue asking for input
print (cnt)


#print 1 to 10

i = 0
while i<=10:                #while i is equal to or less than 10 continue loop
    print (i, end= ".")     #print i
    i = i + 1               #increment i by 1 and the sequence keeps going till 10
print ()

#print 10 to  1
i = 10
while i >= 0:               #while i is equal to or greater than 1, continue loop
    print (i, end = "/")    #how to print
    i= i -1                 #itteration runs and each time decreases it by 1 and runs till the while loop is done
print ()

#number guessing game
print ("you win if you guess the number")
n=int (input("Enter a number:"))        #first input

while n != 3:             #keep going while n it NOT 3
    if  n <3:
        print ('try a higher number')
    elif n==7:
        print ('some people think so not me')
    elif n>3:
        print ('try a lower number')
    else:
        print ('sorry better luck next time')
    n=int (input("Enter a number:"))    #this is in the if box
print("You win!")        #this is in the while box, while its 3 print whatever

#prompt for and read marks for a test until a negative number is entered
mark = float (input("Enter a Mark:"))
n=0
total=0.0
while mark >= 0.0:
    n= n+1
    total= total + mark
    mark = float (input("Enter a Mark;"))
print ("The number of Marks:", n)
if n > 0:
    print ("The average mark is:", total/n)



n = int (input("Guessing game, guess a number"))

while n != 5:
    if n ==6:
        print ("so  close")
    elif n > 5:
        print ("try a lower number")
    else:
        if n < 5:
            print ("try a higher number")
    n = int(input(" guess a number"))
print ("You win")





