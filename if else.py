#Refreshing simple If else condition.This is not a nested if else condition.

num = int(input("Enter a valid number (above 10 ):"))

if num > 10 :
    print ('This is valid ')
else:
    print ('This is invalid(num is below 10 )')


#nested if else

marks = int (input ("Enter your marks "))

if marks >= 90:
    grade = ("A")
else :
    if marks >= 80:
        grade = ("B")
    else:
        if marks >= 70:
           grade = ("C")
        else:
            if marks >= 60:
                grade = ("D")

print (grade)

#elif... u can use elif to nest if else and shorten it.

m = int (input ("Enter marks "))
if m >= 90:
    grade = ('A')
elif m >= 80:
    grade = ('B')
elif m >= 70:
    grade = ("C")
print (grade)

i =  5
x=3.4
x+1
print (x)