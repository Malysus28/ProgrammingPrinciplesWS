"""Prompt for a name of a file to read and target file to
 write and copy the content of the source file. But with all
 the empty lines removed. Then output the number of lines removed."""

fileSource = open (input ("Source File name:"))
fileTarget = open (input ("Target File name:"), mode = "w")

countSpaces = 0

for line in fileSource:
    if line == '\n':
        countSpaces +=1
    else:
        fileTarget.write (line)
fileSource.close()
fileTarget.close ()

print (countSpaces)

