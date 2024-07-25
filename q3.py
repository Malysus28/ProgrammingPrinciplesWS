def check_difference(d, num_list):
     # Sort the list to make it easier to compare adjacent elements

    for i in range(len(num_list) - 1):
        if num_list[i + 1] - num_list[i] < d:
            return False

    return True

# Example usage:
d_value = 3
my_list = [4, 500, 1, 6, 30]

result = check_difference(d_value, my_list)
print(result)
