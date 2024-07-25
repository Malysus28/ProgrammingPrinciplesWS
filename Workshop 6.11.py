STR1 = input("Enter a string: ")
while STR1 != '':       #continue as long as string is not empty
    wlist = STR1.lower().split()     #split into words
    wlist.sort(reverse=True)    #sort in decending order
    for word in wlist:
        print(word, end=' ')    #seperate words with a delim of space
    print()
    STR1 = input("Enter a string: ")