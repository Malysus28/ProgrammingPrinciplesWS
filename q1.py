source_file_name = input("Source File name: ")
target_file_name = input("Target File name: ")


file_source = open(source_file_name, 'r')
file_target = open(target_file_name, 'w')

for line in file_source:
    if not line.startswith(':'):
        file_target.write(line)



file_source.close()
file_target.close()
