#pt 1

# Start with an empty string for the longest input
longest = ""

# loop till a is entered
while True:
    MYinput = input("Enter a word (or type a word starting with 'A' to stop): ")

   #[0] access the first charecter of int
    #.lower converts capital A to 'a' (negate case sensitivity)
    if MYinput[0].lower() == 'a':
        break  # Exit the loop

    # empty strings not accepted// checking if its empty
    if MYinput:
        # finding longest string using len
        if len(MYinput) > len(longest):
            longest = MYinput


print("The longest word you entered is:", longest)

#pt1.2 code sent in, it has case sensitivity issues

MYinput = input ("Enter a String(Enter A to stop)")
longest = MYinput

while MYinput.startswith('A')== False:

    #determining the longest string
    if len (MYinput) > len (longest):
        longest = MYinput
    MYinput = input ("Enter a String(Enter A to stop): ")

    #determine if the entered string with A is the longest string
    if (MYinput.startswith('A')== True) and len (MYinput) > len (longest):
        longest = MYinput

print ("Longest was:", longest )



#pt2

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
