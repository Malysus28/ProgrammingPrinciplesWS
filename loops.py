

#indefenite loops use while

#loop to print the numbers from 10 to 1
i = 10
while i >= 1:
   print(i, end = " ")
   i = i - 1
print()

#loop to print from 1 to 10
i = 1
while i <= 10:
   print(i, end = " ")
   i = i + 1
print()

#exercise from lecture 12

# read marks for a test until a negative number is entered
#(qhich can be a valid mark), print the number of marks entered
#the average (arithmetic mean) of the marks, and the lowest and highest
#marks

n= 0
total = 0.0
#highest = 0
#lowest = 999
#this method works but if the test is marked over 999 there will be an error
mark = float (input("Enter a Marks :"))
highest = mark
lowest = mark

while mark >= 0.0:
    n+= 1
    total += mark

    if mark > highest :
        highest= mark
    if mark < lowest:
        lowest = mark

    mark = float(input("Enter a Marks :"))

print ("The number of marks:", n )
print ("The average mark is:", total/n)
if n > 0:
    print ("The average mark is:", total / n )
    print ("the lowest mark is", lowest)
    print ("the highest mark is", highest)

