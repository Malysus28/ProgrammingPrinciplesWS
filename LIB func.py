#converting letters to hashes and leaving digits as is

m = str(input("Enter a string: (Letters = #, digits as is)"))

for char in m:
    if char.isalpha():
        print ('#', end = "")
    else:
        if char.isdigit():
            print (char, end='')
print ()



#modified string and original string

m = str(input("Enter a string:"))
modified_string = ""

for char in m:
    if char.isalpha():
        modified_string += '#'
    elif char.isdigit():
        modified_string += char

print("NOT Modified string:", m)
print(" Modified string:", modified_string)




#remove all spaces in an input string

i = str(input("Enter a string: "))
modified_string = ""

for ch in i:
    modified_string += ch.rstrip()

print("Original string:", i)
print("Modified string without trailing spaces:", modified_string)


ki = str(input("Enter a string: "))
k = ""

for char in ki:
    if char.isdigit():
        k += "@"
    elif char.isalpha():
        k += "!"
    elif char.isspace():
        k+= "_"
    else:
        k += char

print(k)






