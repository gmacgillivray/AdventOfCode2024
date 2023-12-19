# Advent of Code 2023 Puzzle 13a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle13Data.txt", "r")

# Read in all the lines of the file into a list of lines
temp_data = f.readlines()
data = []

# Close file
f.close()

def find_reflection_line(list_to_check):
    
    match = 0

    for i in (range(len(list_to_check)-1)):
        if list_to_check[i] == list_to_check[i+1]:
            mirror_check =[]
            s = len(list_to_check) - (i + 1)
            check_list_one = list_to_check[:i+1]
            check_list_two = list_to_check[i+1:]
            if i < s:
                for ri in range(2 * i + 1, i, -1):
                    mirror_check.append(list_to_check[ri])
                if check_list_one == mirror_check:
                    match = i + 1
            else:
                for ri in range(i, (2 * i - len(list_to_check)) + 1, -1):
                    mirror_check.append(list_to_check[ri])
                if check_list_two == mirror_check:
                    match = i + 1

    return match

def transpose_list(list_to_transpose):

    return_array = []

    for j in (range(len(list_to_transpose[0])-1)):
        transpose_string = ""    
        for i in (range(len(list_to_transpose))):
            transpose_string += (list_to_transpose[i][j])
        return_array.append(transpose_string)

    return return_array

row_match = 0
col_match = 0
sum = 0
array_check = []

for r in range(len(temp_data)):

    if temp_data[r] != "\n":
        array_check.append(temp_data[r])
    else:
        row_match = find_reflection_line(array_check)
        mirror_array = transpose_list(array_check)
        col_match = find_reflection_line(mirror_array)
        print(row_match, col_match)
        sum += row_match * 100 + col_match
        array_check = []

print("The total after summarizing all notes is", sum)

#for i in range(len(data)):
#    for j in range(len(data[i])):
#        print(data[i][j])

#for r in range(len(data)):
    #print(data[r], instructions[r], running_matches[r])