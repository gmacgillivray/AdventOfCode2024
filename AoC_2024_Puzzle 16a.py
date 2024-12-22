# Advent of Code 2024 Puzzle 13

# Import necessary libraries
from collections import defaultdict

# define sub functions

def replace_char_at_index(s, index, new_char):
    # Convert the string to a list of characters
    char_list = list(s)
    
    # Replace the character at the specified index
    char_list[index] = new_char
    
    # Convert the list back to a string
    return ''.join(char_list)

def find_robot(m, robot_sym):
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == robot_sym:
                r_location = (x, y)
                break
    
    return r_location

def move_robot(p, move, map, walls, boxes):
    
    move_symbols = ["<", ">", "^", "v"]
    
    if move == move_symbols[0]:
        if map[p[0] - 1][p[1]] not in boxes and map[p[0] - 1][p[1]] not in walls:
            p = [p[0] - 1], [p[1]]
        
    new_pos_x = (position[0] + velocity[0] * t) % size[0]
    new_pos_y = (position[1] + velocity[1] * t) % size[1]

    return [new_pos_x, new_pos_y]

def draw_map(all_pos, size):
    
    visual_map = []
    row_string = ""
    
    for i in range(size[0]):
        row_string += "."
        
    for j in range(size[1]):
        visual_map.append(row_string)

    for i in range(len(all_pos)):
        if visual_map[all_pos[i][1]][all_pos[i][0]] == ".":
            new_character = "1"
        else:
            new_character = str(int(visual_map[all_pos[i][1]][all_pos[i][0]]) + 1)         
                        
        visual_map[all_pos[i][1]] = replace_char_at_index(visual_map[all_pos[i][1]], all_pos[i][0], new_character)
        
    return visual_map   

def count_quadrants(all_pos, size):
    
    middle_x = int(size[0]/2)
    middle_y = int(size[1]/2)
    
    quadrant_count = [0, 0, 0, 0]
    
    for i in range(len(all_pos)):
        if all_pos[i][0] < middle_x and all_pos[i][1] < middle_y:
            quadrant_count[0] += 1
        elif all_pos[i][0] > middle_x and all_pos[i][1] < middle_y:
            quadrant_count[1] += 1    
        elif all_pos[i][0] < middle_x and all_pos[i][1] > middle_y:
            quadrant_count[2] += 1
        elif all_pos[i][0] > middle_x and all_pos[i][1] > middle_y:
            quadrant_count[3] += 1
    
    return quadrant_count

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle15Data_test.txt", "r") as f:
    data = f.readlines()

map = []
instructions = ""
input_break = True

for line in data:
    
    if line != "\n":
        if input_break:
            map.append(line.strip("\n"))
        else:
            instructions += (line.strip("\n"))
    else: 
        input_break = False 

print(map)
print(instructions)

#print("The total number of tokens to maximize prizes =", total_total)
