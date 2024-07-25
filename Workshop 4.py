#write a program that reads whole numbers typed by the user
# until a zero is entered, then pritnts the number of positive numbers
#that were entered


# problem 1
posCount= 0
num= int(input("Enter a whole number (enter 0 to stop): "))

#note to self syntax when entering NOT != pay attention to spaces
#pay attention to sentinel patterns
# when num is not = to 0 the loop will continue
#dont forget that indentation is important

while num != 0:
    #if mark is greater than 0 it is counted as a posCount and incremented by 1
    if num > 0:
        posCount += 1
    num =int(input("Enter a whole number (enter 0 to stop): "))

print( posCount, "positive numbers were entered")

#problem 2

#use three numbers to get the rest of the numbers
#Fibonacci number is the sum of the two preceding ones, starting from 0 and 1
#That is, F1 = 0, F2 = 1, F3 = 1, F4 = 2, ..., Fn = F(n-1) + F(n-2)
#Write a program that given an input n, outputs the first n Fibonacci numbers.
# The format of output is that at most 4 numbers can be displayed in a row. Sample run:

#for loop
n = int (input("Enter a positive number: "))

if n <=2:
    print ("Enter in a number higher than 2, Please enter a number again")
f0 = 0
f1=1
f3_temp = 0

print (f0, f1, end = ' ')

row = 2

for i in range (2 , n):
    f3_temp  = f0+ f1
    print (f3_temp , end = ' ')
    row += 1
    f0 = f1
    f1 = f3_temp

    #when the numbers displayed per row is above 4 digits, start on a new line
    if row % 4 == 0:
        print (end='\n')



#problem 3

n = int(input("Enter a number:"))



#method 2

n = int(input("Enter a number: "))

# Upper triangle
for w in range(1,n + 1):
    spaces =' ' * (n -w)
    Xs ='X' *(2* w -1)
    print(spaces +Xs)

# Lower half of triangle
for w in range(n - 1,0, -1):
    spaces =' ' * (n -w)
    Xs ='X' *(2* w -1)
    print(spaces +Xs)


#4

n = (input("Enter a positive number"))

copy_n = n
result_n = 0

while n % 10 !=0:
    r = n % 10
    result_n = result_n*10 + r
    n=n//10

if result_n == copy_n:
    print(result_n, "is a palidrome")
else:
    print(result_n, "not a palindrome")


