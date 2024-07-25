# Get starting and ending years from the user
StartYear = int(input("Enter the starting year: "))
EndYear = int(input("Enter the ending year: "))

# Initialize variables (global)
NumOfDaysInYear = 365
LeapYearDay = 1


# Calculate total days between starting and ending years
def CalculateYear():
    TotalDays = 0  # local variable
    for y in range(StartYear, EndYear + 1):
        # Check if divisible by 4
        # Check if the year is NOT divisible by 100
        # Check if the year is divisible by 400 (if divisible by 400 = leap year)
        # If the year is divisible by 100 and not 400, it is not a leap year
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            TotalDays+= NumOfDaysInYear + LeapYearDay
        else:
            TotalDays+= NumOfDaysInYear

    return TotalDays

# Print the result
print(f"Number of days:",CalculateYear())
