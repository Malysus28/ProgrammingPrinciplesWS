
#nested loops

for y in range (3):     #loop gets executed 3 times(outter loop)
    for x in range (1,10):      #inner loop
        print (x, end = '|')    #prints 1 to 9
    print ('')      #after you exit the for loop, print new line

row = int (input("Enter num of rows"))
cols= int (input("enter the num of colums"))

for r in range (row):
    for c in range (cols):
        print ("@", end ='')
    print ()
#https://www.youtube.com/watch?v=APWy6Pc83gE&t=233s

#count digits in a string

count = 0
s = str (input("Enter a string: with numbers"))
for char in s:                  #for charecters in string
    if '0' <= char <= '9':      #if includes letters from 0 to 9
        count +=1               #increase count by 1
print ("num of digits=", count)     #exit loop and print

#count digits in a string with isdigit func

cnt =0
st = str(input("Enter a string(with numbers)"))
for ch in st:
    if ch.isdigit():
        cnt +=1
print ("Num of digits=", cnt )

cunt = 0
sf = str (input ("Enter A STRING "))

for chart in sf:
    if chart.isalpha():
        cunt +=1
print ("num of letters", cunt)

