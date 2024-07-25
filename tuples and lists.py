# list () and [] are the same thing

FirstList = list (range (10))
print (FirstList)


secList = [1, True, abs]
print (secList)

#make a list of strings, and print the first element
ThirdList = ['apple' , 'banana', 'orange']
print (ThirdList[0])

ThirdList1 = ['apple' , 'banana', 'orange']
print (ThirdList1[-1])             #using negative indicies, -1 is the last one

ThirdList2 = ['apple' , 'banana', 'orange']
print (ThirdList2[-2])             #using negative indicies, -1 is the last one

FourthList = [1, 2, 3,]
FourthList.append (4)       #use append to change something, in this case add four
print (FourthList)

#slicing with a string
slice1 = 'ABCDEFGHIJK'
print (slice1 [3:7])        #gets the values from location 3 to 7, starts with 0 dont forget
print (slice1 [:7])         #gets all the values before 7
print (slice1 [7:])         #gets all the values after 7
print (slice1 [-5:])        #gets the last 5
print (slice1 [:])          #gets everything
print (slice1 [3: -3 :2])   #works like range, start at 3, ends at -3, count in steps of 2

#catenations
fifthList = (1,2) + (3,4)   #joining sequences tuples
print (fifthList)

sixthList = ['hi ' + 'there']   #joining lists
print (sixthList)

seventhList = 'pew' * 10        #multiplying a string
print (seventhList)