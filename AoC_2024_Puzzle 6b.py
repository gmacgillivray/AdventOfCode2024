# Advent of Code 2024 Puzzle 6

# Import necessary libraries

import re
from collections import defaultdict

# Open the file and read all lines into a list
f = open ("AoC_2024_Puzzle6Data.txt", "r")
data = f.readlines()
f.close()

# Define subfunctions
def replace_char_at_index(s, index, new_char):
    # Convert the string to a list of characters
    char_list = list(s)
    
    # Replace the character at the specified index
    char_list[index] = new_char
    
    # Convert the list back to a string
    return ''.join(char_list)

def count_unique_values(lst_of_lists):
    # Convert each list to a tuple and add to a set
    unique_values = set(tuple(sublist) for sublist in lst_of_lists)
    return len(unique_values)

def trace_path_in_area(o_pos, o_step, map):
    pos = [o_pos[0], o_pos[1]]
    next_step = [o_step[0], o_step[1]]
    path_points = []
    path_nextsteps = []

    map_loop_exit = True
    guard_in_map = True
    
    path_points.append([pos[0], pos[1]])
    path_nextsteps.append([next_step[0], next_step[1]]) 

    next_pos = [pos[0] + next_step[0], pos[1] + next_step[1]]
    new_next_step = [next_step[0], next_step[1]]

    while guard_in_map:   

        if map[next_pos[0]][next_pos[1]] == "#":
            if next_step == [0, 1]:
                new_next_step = [1, 0]
            if next_step == [1, 0]:
                new_next_step = [0, -1]
            if next_step == [0, -1]:
                new_next_step = [-1, 0]
            if next_step == [-1, 0]:
                new_next_step = [0, 1]
        
        next_step[0] = new_next_step[0]
        next_step[1] = new_next_step[1]
        
        pos[0] = pos[0] + next_step[0]
        pos[1] = pos[1] + next_step[1]
    
        pos_indices = [index for index, value in enumerate(path_points) if value == pos]
        next_step_indices = [index for index, value in enumerate(path_nextsteps) if value == next_step]
        
        for i in range(len(pos_indices)):
            if pos_indices[i] in next_step_indices:
                map_loop_exit = True
                guard_in_map = False 
        
        path_points.append([pos[0], pos[1]])
        path_nextsteps.append([next_step[0], next_step[1]])     
        
        next_pos[0] = pos[0] + next_step[0]
        next_pos[1] = pos[1] + next_step[1]
        
        if next_pos[0] >= len(map) or next_pos[1] >= len(map[0]) or next_pos[0] < 0 or next_pos[1] < 0:
            guard_in_map = False
            map_loop_exit = False

    return(path_points, map_loop_exit)

# Define variables and initialize
a = []
opos = []
first_step = []
pos = []
next_pos = []
next_step = []
new_next_step = []
index_X = []
sum_parta = 0
sum2_a = 0
sum2_b = 0
map_exits_count = 0
map_loops_count = 0

path_points = []
path_nextsteps =[]
pos_indices = []
temp_path = []
char_to_replace = "#"
reset_char = "."

for line in data:
    a.append(line.strip("\n"))

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == "^":
            opos.append(i)
            opos.append(j)
            first_step = [-1, 0]
        if a[i][j] == ">":
            opos.append(i)
            opos.append(j)
            first_step = [0, 1]
        if a[i][j] == "v":
            opos.append(i)
            opos.append(j)
            first_step = [1, 0]
        if a[i][j] == "<":
            opos.append(i)
            opos.append(j)
            first_step = [0, -1]     


temp_path, loop_exit = trace_path_in_area(opos, first_step, a)
sum_parta = count_unique_values(temp_path)

print("The number of guard positions for part a is", sum_parta)

for x in range(len(a)):
    for y in range(len(a[0])):
        if a[x][y] != "#" and a[x][y] != "^" and a[x][y] != "v" and a[x][y] != "<" and a[x][y] != ">":
            
            a[x] = replace_char_at_index(a[x], y, char_to_replace)

            pos = [opos[0], opos[1]]
            next_step = [first_step[0], first_step[1]]
            path_points = []
            path_nextsteps = []

            guard_in_map = True
            path_points.append([pos[0], pos[1]])
            path_nextsteps.append([next_step[0], next_step[1]]) 

            next_pos = [pos[0] + next_step[0], pos[1] + next_step[1]]
            new_next_step = [next_step[0], next_step[1]]

            while guard_in_map:   

                if a[next_pos[0]][next_pos[1]] == "#":
                    if next_step == [0, 1]:
                        new_next_step = [1, 0]
                    if next_step == [1, 0]:
                        new_next_step = [0, -1]
                    if next_step == [0, -1]:
                        new_next_step = [-1, 0]
                    if next_step == [-1, 0]:
                        new_next_step = [0, 1]
                
                next_step[0] = new_next_step[0]
                next_step[1] = new_next_step[1]
                
                pos[0] = pos[0] + next_step[0]
                pos[1] = pos[1] + next_step[1]
            
                pos_indices = [index for index, value in enumerate(path_points) if value == pos]
                next_step_indices = [index for index, value in enumerate(path_nextsteps) if value == next_step]
                
                for i in range(len(pos_indices)):
                    if pos_indices[i] in next_step_indices:
                        sum2_b += 1
                        map_loops_count += 1
                        guard_in_map = False 
                
                path_points.append([pos[0], pos[1]])
                path_nextsteps.append([next_step[0], next_step[1]])     
                
                next_pos[0] = pos[0] + next_step[0]
                next_pos[1] = pos[1] + next_step[1]
                
                if next_pos[0] >= len(a) or next_pos[1] >= len(a[0]) or next_pos[0] < 0 or next_pos[1] < 0:
                    guard_in_map = False
                    map_exits_count += 1 
            
            a[x] = replace_char_at_index(a[x], y, reset_char)   

sum2_a = count_unique_values(path_points)
    
# Print the results
print("Map exits count = ", map_exits_count)
print("Map loops count = ", map_loops_count)

#print("The sum of all middle values for re-ordering incorrectly ordered updates ", sumb)