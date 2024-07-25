#read a file and print in ascending order

fileSource = open (input ("Enter file name "))
unique= set()

for line in fileSource:
    words = line.split()
    for word in words:
        unique.add(word)



fileSource.close ()
for word in sorted (unique):
    print (word)