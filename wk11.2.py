from DNSChild import *

dns_table = DNSC()  # Instantiate DNSC instead of DNS

command = input("? ")

while command != "q":
    wordList = command.split()
    if len(wordList) == 3 and wordList[0] == "u":
        dns_table.update(wordList[1], wordList[2])

    elif len(wordList) == 2 and wordList[0] == "b":
        dns_table.blacklist(wordList[1])

    elif len(wordList) == 2 and wordList[0] == "l":
        print (dns_table.lookup (wordList[1]))


    else:
        print("Bad command")
    command = input("? ")
