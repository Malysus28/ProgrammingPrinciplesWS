
x= str(input("Enter a string:"))
def PrintVertical ():              #define function
    """ Print x vertically"""       #comment
    for char in str (x):
        print (char)

PrintVertical ()                    #calling the function

def sort (xs):
    """sort list xs in place into ascending order """
    for i in range (0, len (xs)-1):
        for j in range (i +1, len (xs)):
            if xs [j] < xs [i]:
                xs[j], xs[i]= xs[i], xs[j]

ys = [2, 3, 1, 0]

sort(ys)    #sort it
print (ys)  #print it

