def check_difference(d, num_list):


    # Iterate through the list, comparing adjacent elements
    for i in range(len(num_list) - 1):
        # Calculate the difference between adjacent elements
        current_difference = num_list[i + 1] - num_list[i]

        # Check if the difference between adjacent elements is less than d
        if current_difference < d:
            return False  # If found, return False

    return True  # If no such pair is found, return True

# Example usage:
d_value = 3
my_list = [4, 500, 1, 6, 30]

# Call the function and store the result in the 'result' variable
result = check_difference(d_value, my_list)

# Print the result
print(result)
