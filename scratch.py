#an ATM, if withdraw limit is above 4000, invalid
#if withdraw limit is below 4000, valid
num = float(input("Enter the number"))

def invalid ():
    if num >= 4000:
        print ("Transaction cancelled  ")

def VALID():
    if num < 4000:
        print ("Transcation approved ")

if num >= 4000:
    invalid()
else :
    VALID ()

var = 1
x = int(5)
z = x + var
print (z)