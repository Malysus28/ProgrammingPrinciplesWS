SourceFileName = input ("Source file name: ")

FileSource = open (SourceFileName, "r")

countFile = 0

for line in FileSource:
    if 'file' in line:
        countFile += 1


FileSource.close()

print (countFile)

