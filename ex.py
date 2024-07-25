myInput = input("Enter a string: ")
longest = myInput

while myInput != "":
    if len(myInput) > len(longest):
        longest = myInput
    myInput = input("Enter a string: ")

print("Longest Was:", longest)
