print ("you win if you guess the magic number ")
n= int(input("Enter a number:"))
if n == 3:
    print ("you guessed it right")
    print ("It's the first odd prime. YAY")
    #the indententation makes it an else, i they didnt guess it then the indentation line comes into play
print ("If you didnt win, better luck next time ")

#another way of doing it is using if and else (using 2 conditions )

print ("Guess the number ")
n = int (input("Enter a number: "))

if n == 4:
    print ("You guessed it right")
else :
    print ("sorry better luck next time ")

#using three conditions

print("Guess the number again ")
n = int (input("Enter a number: "))
if n == 3:
    print ("You guessed it right")
elif n == 7 :
    print ("you are almost right")
else:
    print ("Sorry try again next time")

#nested
print("Guess the number again ")
n = int (input("Enter a number: "))
if n == 3:
    print ("you guessed it right")
else:
    if n == 7:
        print ("you are close but not quiet right")
    print ("Better luck next time ")
    if n <3:
        print ("Try higher number ")
    else:
        print ("Try lower ")