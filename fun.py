def digitsToUnderscore(input_str):
    #local variable
    display = ""
    for c in input_str:
        if c.isdigit():
            display += '_'
        else:
            display += c
    return display

# Get user input
entered = input("Enter a string with numerical digits: ")

# call digitsToUnderscore (function) and execute
ConvertedStr= digitsToUnderscore(entered)
print("Converted string:",ConvertedStr)
