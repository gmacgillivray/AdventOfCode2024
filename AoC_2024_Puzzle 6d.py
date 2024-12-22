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

def unique_values(lst_of_lists):
    
    unique_values = set(tuple(sublist) for sublist in lst_of_lists)
    
    return list(unique_values)

def trace_path_in_area(o_pos, o_step, map):
    pos = [o_pos[0], o_pos[1]]
    next_step = [o_step[0], o_step[1]]
    path_points = set()
    path_nextsteps = set()

    map_loop_exit = True
    guard_in_map = True
    
    path_points.add((pos[0], pos[1]))
    path_nextsteps.add((next_step[0], next_step[1])) 

    next_pos = [pos[0] + next_step[0], pos[1] + next_step[1]]
    new_next_step = [next_step[0], next_step[1]]

    while guard_in_map:   
        if map[next_pos[0]][next_pos[1]] == "#":
            if next_step == [0, 1]:
                new_next_step = [1, 0]
            elif next_step == [1, 0]:
                new_next_step = [0, -1]
            elif next_step == [0, -1]:
                new_next_step = [-1, 0]
            elif next_step == [-1, 0]:
                new_next_step = [0, 1]
        
        next_step = new_next_step[:]
        
        pos[0] += next_step[0]
        pos[1] += next_step[1]
    
        if (pos[0], pos[1]) in path_points and (next_step[0], next_step[1]) in path_nextsteps:
            map_loop_exit = True
            guard_in_map = False 
        
        path_points.add((pos[0], pos[1]))
        path_nextsteps.add((next_step[0], next_step[1]))     
        
        next_pos[0] = pos[0] + next_step[0]
        next_pos[1] = pos[1] + next_step[1]
        
        if next_pos[0] >= len(map) or next_pos[1] >= len(map[0]) or next_pos[0] < 0 or next_pos[1] < 0:
            guard_in_map = False
            map_loop_exit = False

    return list(path_points), list(path_nextsteps), map_loop_exit

# Define variables and initialize
a = []
opos = []
first_step = []
map_exits_count = 0
map_loops_count = 0
temp_path = []
temp_nextsteps = []
all_paths = []
all_nextsteps = []
obstacle_location_for_loop = []
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


temp_path, temp_nextsteps, loop_exit = trace_path_in_area(opos, first_step, a)
sum_parta = count_unique_values(temp_path)
points_to_place_obstacles = unique_values(temp_path)
all_paths.append(temp_path)
all_nextsteps.append(temp_nextsteps)

print("The number of guard positions for part a is", sum_parta)

print(all_paths[0])
print(len(all_paths[0]))

for i in range(len(points_to_place_obstacles)):
    
    x, y = points_to_place_obstacles[i] 
    
    print(i, x, y)
        
    if a[x][y] != "#" and a[x][y] != "^" and a[x][y] != "v" and a[x][y] != "<" and a[x][y] != ">":

        a[x] = replace_char_at_index(a[x], y, char_to_replace)

        opos = all_paths[0][all_paths[0].index([x, y]) - 1]
        first_step = all_nextsteps[0][all_paths[0].index([x, y])  - 1]

        temp_path, temp_nextsteps, loop_exit = trace_path_in_area(opos, first_step, a)
        
        if loop_exit:
            map_loops_count += 1
            obstacle_location_for_loop.append([x, y])
        else:
            map_exits_count += 1
        
        all_paths.append(temp_path)
    
        a[x] = replace_char_at_index(a[x], y, reset_char)   

# Print the results
print("Map exits count = ", map_exits_count)
print("Map loops count = ", map_loops_count)
print(obstacle_location_for_loop)