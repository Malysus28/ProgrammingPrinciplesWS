#prints attempt 2 times
for number in range (3):
    print ("Attempt (1 Arg)")

#create two arguments
for number in range (5):
    print ("Attempt (2 arg)", number)
#first arg is printing attempt 5 times
#sec arg is printing the number of itterations in the range

#create two arguments, making it more readable
for number in range (5):
    print ("Attempt (2 arg readable)", number+1)

# the itteration in range (5) goes like 0,1,2,3,4
#when you add +1 it adds one value to the interation numbers
#makes it 0+1, 1+1, 2+1, 3+1, 4+1 making it (1,2,3,4,5)

#creating three arguments
for number in range (5):
    print ("Attempt (3 arg )", number+1, (number+1) * ".")
# the (number +1) * "." the number gets multiplied by a string char of .

sucessful = True
for number in range (3):
    print ()

#drawing a triangle

n = int(input("Enter a number: "))

# Upper triangle
for num in range(1,n + 1):  #range 1 to input +1
    spaces =' ' * (n -num)
    Xs ='X' *(2* num -1)
    print(spaces + Xs)

for character in "String":
    print (character)

for numb in range (2,10,+2):
    print (numb)



