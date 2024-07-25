"""program that prompts for the name of a file,
then prints the first two lines and the last two lines of the file."""

fileSource = open (input ("Source File name:"))

lines = []
#lineNumbers = 0

for li in fileSource:
    lines.append (li)

print (lines [0].rstrip())
print (lines [1].rstrip())
print (lines [-2].rstrip())
print (lines [-1].rstrip())

fileSource.close()