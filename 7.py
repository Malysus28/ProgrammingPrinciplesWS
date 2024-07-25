FileOne = open (input("Enter the file to read"))
FileTwo = open (input("Enter the file to write") , mode = 'w')

line = FileOne.readline()
while line != "":
    FileTwo.write(line)
    line = FileOne.readline()
FileOne.close()
FileTwo.close()