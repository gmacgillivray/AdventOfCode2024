# Advent of Code 2023 Puzzle 13a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle13Data.txt", "r")

# Read in all the lines of the file into a list of lines
temp_data = f.readlines()
data = []

# Close file
f.close()

def find_reflection_line(list_to_check, old):
    
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
                    if (i + 1) != old:
                        match = i + 1
            else:
                for ri in range(i, (2 * i - len(list_to_check)) + 1, -1):
                    mirror_check.append(list_to_check[ri])
                if check_list_two == mirror_check:
                    if (i + 1) != old:
                        match = i + 1

    return match

def transpose_list(list_to_transpose):

    return_array = []

    for j in (range(len(list_to_transpose[0]))):
        transpose_string = ""    
        for i in (range(len(list_to_transpose))):
            transpose_string += (list_to_transpose[i][j])
        return_array.append(transpose_string)

    return return_array

def scan_for_smudge(list_to_scan_smudge, old_reflection_line):
    
    match_internal = 0
    match_part_two = 0

    for i in range(len(list_to_scan_smudge)):
        for j in range(len(list_to_scan_smudge[0])):
            
            temp_array = []
            for line in list_to_scan_smudge:
                temp_array.append(line)
            
            if list_to_scan_smudge[i][j] == ".":
                if j != (len(list_to_scan_smudge[0]) - 1):
                    temp_array[i] = temp_array[i][:j] + "#" + temp_array[i][j+1:]
                else:
                    temp_array[i] = temp_array[i][:j] + "#"
            if list_to_scan_smudge[i][j] == "#":
                if j != (len(list_to_scan_smudge[0]) - 1):
                    temp_array[i] = temp_array[i][:j] + "." + temp_array[i][j+1:]
                else:
                    temp_array[i] = temp_array[i][:j] + "."
            
            match_internal = find_reflection_line(temp_array, old_reflection_line)

            if ((match_internal > match_part_two) and (match_internal != old_reflection_line)):
                match_part_two = match_internal

    return match_part_two

row_match = 0
col_match = 0
sum = 0
sum_part_two = 0
array_check = []
row_match_all = []
col_match_all = []
smudge_horizontal_pos = []
smudge_vertical_pos = []
temp_array = []
row_match_part_two_all = []
col_match_part_two_all = []
arrays = 0


for r in range(len(temp_data)):
 
    if temp_data[r] != "\n":
        array_check.append(temp_data[r].strip())
    else:
        arrays += 1
        row_match = find_reflection_line(array_check, 0)
        mirror_array = transpose_list(array_check)
        col_match = find_reflection_line(mirror_array, 0)
        
        sum += row_match * 100 + col_match
        row_match_all.append(row_match)
        col_match_all.append(col_match)

        row_match_part_two = scan_for_smudge(array_check, row_match)
        col_match_part_two = scan_for_smudge(mirror_array, col_match)
   
        sum_part_two += row_match_part_two * 100 + col_match_part_two
#        if row_match == row_match_part_two:
#            row_match_part_two = 0
#        if col_match == col_match_part_two:
#            col_match_part_two = 0
        
        row_match_part_two_all.append(row_match_part_two)
        col_match_part_two_all.append(col_match_part_two)
        
        array_check = []
        mirror_array = []
        print(arrays, row_match, col_match, row_match_part_two, col_match_part_two)

print("The total after summarizing all notes in part one is", sum)
print("The total after summarizing all notes in part two is", sum_part_two)

#for i in range(len(data)):
#    for j in range(len(data[i])):
#        print(data[i][j])

#for r in range(len(data)):
    #print(data[r], instructions[r], running_matches[r])