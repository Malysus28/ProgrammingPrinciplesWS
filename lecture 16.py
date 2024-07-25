# defining functions


#defining a function and calling it
#with no arguments or return value

def printBoo():
    print("Boo!")
printBoo()
printBoo()
printBoo()


# Declare and call a function:
#  with an argument, but no return value
def printVertical(x):
    """"Print vertically, this can be any sentence to define function"""
    for c in str(x):
        print(c)

printVertical("Boo!")
printVertical(42)

#multiple arguments and defining them in a sentence to make it clear for the reader
def finalBalance(p, r, n):
    """Returns a final balance with compound interest.

       p in the principle (initial balance)
       r is the interest rate per term
       n is the number of terms"""
    return p * (1.0 + r) ** n


initBal = float(input("Initial balance: "))
annRatePct = float(input("Annual interest rate (%): "))
months = int(input("Number on months: "))
finalBal = finalBalance(initBal,
                        annRatePct / 100.0 / 12.0, months)
print("Final balance = ${:.2f}".format(finalBal))


#local variable
#variables defined in function only
# exists inside the function
def f():
    #define x in function
    x = 2
    print("a x =", x)

y = 1
#calling the function
f()
print("b y =", y)
print("c x =", x)

#global variable
#y is a global variable
def func():
    x = 2
    print("d x =", x)
    print("e k =", k)

k = 1
func()
print("f k =", k)
