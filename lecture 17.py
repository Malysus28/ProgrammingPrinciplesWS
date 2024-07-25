#tuples

#using the constructor to make a list
my_list = list(range(1, 11))
print(my_list)

#how to make a literal list
my_list2 = [1, True, abs]
print(my_list2)

#how to modify a list using append
XS = [1,2,3]
XS.append (4)
print(XS)

my_list3 = [i *i for i in range (10)]
print(my_list3)
#prints 0x0 , 1x1, 2x2, 3x3, 4x4, 5x5, 6x6, ......

#indexing
#acessing elements of an array
t = ("Element 0", "element 1", 2)
print (t[0])
print (t[1])
print (t[2])

#indexing
#acessing a string
s="Hello"
print (s[1])
#prints e because the count starts from 0

#indexing
#negative indicies
#you can index from the end of a swequence, with negative indicies
#last statement is at index -1, second last is -2
N="123456"
print (N[-1])

#slicing a string, allows to snip out a subsequence from a sequence and get
#more than one element. where indexing allows 1 element
l = "abcdefghijklmnop"
print (l [3:7])
#slice from position 3 to 7
print (l [:7])  #everything before 7
print (l[3:])   #everything after 3
print (l[-5])   #accesses the last 5
print (l[:])    #prints everything
print (l [3:-3:2])  #start with third one, and steps of 2


#catenation : join sequences
c= (1,2) + (3,4)    #combining lists
print (c)

k = "hi " "" + "there"  #combining strings
print (k)

p = "pew " *10   #creates 10 repetition of the string
print (p)

#using operators in lists
b = 2 in [1,2,3]     #statement asking is 2 is in the list
print (b)

d = 90 not in range (100)   #asking if there is a 90 strating from the range of 100
print (d)

f = "ll" in "hello"     #is there ll in hello 
print (f)