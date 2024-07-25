
filename = 'name_of_file.txt'  # Replace 'name_of_file.txt' with the actual file name
with open(filename, 'r') as f:
    for line in f:
        line = line.rstrip()
        if not line.startswith('From:'):
            # Do something with the line if it doesn't start with 'From:'
            print(line)
