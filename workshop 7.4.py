"""Write your own version of wc that prompts for the name
of the file to read, then prints the counts.
Assume a word may contain letters, digits,
symbols and their mixture, but not space. Hyphenated words, e.g.
large-scale, shall be considered as one word."""


fileSource = open (input ("Source File name:"))

charCount = 0
wordCount = 0
lineCount = 0

for line in fileSource:
    charCount += len (line)
    wordCount += len (line.split())
    lineCount += 1

fileSource.close()

print ("Charecter count:", charCount, "word Count:", wordCount,
       "line count:", lineCount)