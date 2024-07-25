
#global variables
#y is a global variable because it esists outside of
#the function. y exists before the function call
#thats why it works
def f():
    x = 2
    print("a x =", x)
    print("b y =", y)


y = 1
f()
print("c y =", y)



#parameters and passing A BIT OF A BLUR

def f(x):
    print("b x =", x)
    #because x+= 1 is written after the B, c is getting the new value which is 1 + 1
    x += 1
    print("c x =", x)


y = 1
print("a y =", y)
f(y)
print("d y =", y)



#Eclipsing globals
#there is a global and local var called x
def f():
    x = 2
    print("2 x =", x)


x = 1
#takes the global var
print("1 x =", x)
#function f is called
f()
#takes the global var
print("3 x =", x)

