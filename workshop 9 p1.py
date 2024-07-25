def do_input(dit_vars, var):
    temp = input("enter a value for "+ var + ": ").rstrip()
    if temp.isdigit():
        dit_vars[var]= int (temp)
    else:
        print("syntax error, you must input an integer")

def do_print (dit_vars, val):
    if val.isdigit():
        print(val)
    elif val.isalpha():
        if val in dit_vars:
            print (val, "equals to ", dit_vars[val])
        else:
            print(val, "is not defined yet")


def do_gets(dit_vars, var, val):
    if val.isdigit():
        dit_vars [var] = int (val)
    elif val.isalpha():
        if val in dit_vars:
            dit_vars[vars] = dit_vars [val]
        else:
            print (val, "is not defined")


def do_adds(dit_vars, val, var):
    if var not in dit_vars:
        print ("Syntax Error")
        if val.isdigit():
            dit_vars[vars] = dit_vars [var] + int (val)
        elif val.isalpha():
            if val in dit_vars:
                dit_vars [var] = dit_vars [var] + dit_vars[val]
            elif val not in dit_vars:
                print (val, "is undefined")




dict_vars = dict()
print("Welcome to the Adder REPL")
commands = input("???").strip()

while commands != "quit":
    wordList = commands.split()

    if len(wordList) == 2 and wordList[0] == 'input':
        print()
        do_input(dict_vars, wordList[1])

    elif len(wordList) == 2 and wordList[0] == 'print':
        print()
        do_input(dict_vars, wordList[1])

    elif len(wordList) == 3 and wordList[1] == 'gets':
        print()
        do_gets(dict_vars, wordList[0], wordList[2])

    elif len(wordList) == 3 and wordList[1] == 'adds':
        do_gets(dict_vars, wordList[0], wordList[2])
        print()

    else:
        print ("the command can be only: input x, print x, x gets y, a adds y")

    commands = input("???").strip()
print ("goodbye")