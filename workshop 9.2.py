def do_input(dict_vars, var):
    temp = input(f"Enter a value for {var}: ").rstrip()
    if temp.isdigit():
        dict_vars[var] = int(temp)
    else:
        print("Syntax error, you must input an integer")

def do_print(dict_vars, val):
    if val.isdigit():
        print(val)
    elif val.isalpha():
        if val in dict_vars:
            print(val, "equals to", dict_vars[val])
        else:
            print(val, "is not defined yet")

def do_gets(dict_vars, var, val):
    if val.isdigit():
        dict_vars[var] = int(val)
    elif val.isalpha():
        if val in dict_vars:
            dict_vars[var] = dict_vars[val]
        else:
            print(val, "is not defined")

def do_adds(dict_vars, var, val):
    if var not in dict_vars:
        print(var, "not defined ")
    else:
        if val.isdigit():
            dict_vars[var] += int(val)
        elif val.isalpha():
            if val in dict_vars:
                dict_vars[var] += dict_vars[val]
            else:
                print(val, "is undefined")

dict_vars = dict()
scriptfh = open (input ("script file name and folder: "))

commands = scriptfh.readline().rstrip ()


while commands != "quit":
    wordList = commands.split()

    if len(wordList) == 2 and wordList[0] == 'input':
        do_input(dict_vars, wordList[1])
    elif len(wordList) == 2 and wordList[0] == 'print':
        do_print(dict_vars, wordList[1])
    elif len(wordList) == 3 and wordList[1] == 'gets':
        do_gets(dict_vars, wordList[0], wordList[2])
    elif len(wordList) == 3 and wordList[1] == 'adds':
        do_adds(dict_vars, wordList[0], wordList[2])
    else:
        print("probably the file containds wrong scripts")
        exit()
    commands = scriptfh.readline().rstrip ()

scriptfh.close()