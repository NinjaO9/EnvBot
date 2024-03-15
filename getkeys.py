# Initalize Variables
file = open('keys.txt', 'r')
key_list = []
temp_list = []
content = file.readlines()

for line in content:
    key = ''
    line_index = 0
    content_index = 0
    while list(line)[0] == "#" or list(line)[0] == "\n":
        content_index += 1
        line = content[content_index]
    while line[line_index] != "=":
        line_index = line_index + 1
    for char in list(line)[line_index + 1:]:
        if char == "\n":
            break
        key = key + char
    temp_list.append(key.replace(" ", ""))
    for i in temp_list: # Makes the key_list, removing any duplicates in the temp_list
        if i not in key_list:
            key_list.append(i)
