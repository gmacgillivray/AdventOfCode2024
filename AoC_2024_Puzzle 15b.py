# Advent of Code 2024 Puzzle 15

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

def find_symbols_in_map(m, sym):
    
    sym_loc = []

    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == sym:
                sym_loc.append([x, y])
    
    return sym_loc

def move_robot(p, move, walls, boxes, x_scale):

    directions = {"<": [-1, 0], ">": [1, 0], "^": [0, -1], "v": [0, 1]}

    # Determine movement vector
    vector = directions.get(move)
    if vector is None:
        raise ValueError("Invalid move symbol")

    # Determine how many boxes can be moved if any by looking ahead to see if there are free spaces to move
    found_a_wall = False
    found_a_space = False
    if vector[0] == -1:
        new_pos = [p[0] + 2 * vector[0], p[1] + vector[1]]
    else:
        new_pos = [p[0] + vector[0], p[1] + vector[1]]
    k = 0

    if vector[1] == 0:
        while not found_a_wall and not found_a_space:
            if [new_pos[0], new_pos[1]] in walls:
                found_a_wall = True
                k = 0
            elif [new_pos[0], new_pos[1]] in boxes:
                k += 1
            else:
                found_a_space = True

            if vector[0] == -1:
                new_pos = [new_pos[0] + 2 * vector[0], new_pos[1] + vector[1]]
            else:
                new_pos = [new_pos[0] + vector[0], new_pos[1] + vector[1]]
    elif vector[0] == 0:
        while not found_a_wall and not found_a_space:
            if [new_pos[0], new_pos[1]] in walls or [new_pos[0] - 1, new_pos[1]] in walls:
                found_a_wall = True
                k = 0
            elif [new_pos[0], new_pos[1]] in boxes or [new_pos[0] - 1, new_pos[1]] in boxes:
                k += 1
            else:
                found_a_space = True

            if vector[0] == -1:
                new_pos = [new_pos[0] + 2 * vector[0], new_pos[1] + vector[1]]
            else:
                new_pos = [new_pos[0] + vector[0], new_pos[1] + vector[1]]
    
    # Calculate new positions
    if found_a_space:
        p = [p[0] + vector[0], p[1] + vector[1]]
        if k > 0:
            if [p[0], p[1]] in boxes:
                box_new_pos = [p[0] + k * vector[0], p[1] + k * vector[1]]
                boxes[boxes.index([p[0], p[1]])] = box_new_pos
            elif [p[0] - 1, p[1]] in boxes:
                box_new_pos = [p[0] - 1 + k * vector[0], p[1] -1 + k * vector[1]]
                boxes[boxes.index([p[0] - 1, p[1]])] = box_new_pos
    
    return p, boxes

def replace_characters_in_map(p, c, m):
    for y in range(len(m)):
        for x in range(len(m[y])):     
            if len(p) != 2:
                if [x, y] in p:
                    for i in range(len(c)):
                        m[y] = replace_char_at_index(m[y], x + i, c[i])
            else:
                if [x, y] == [p[0], p[1]] and x%2 == 0:
                    m[y] = replace_char_at_index(m[y], x, c[0])
                    m[y] = replace_char_at_index(m[y], x + 1, c[1])
                elif [x, y] == [p[0], p[1]] and x%2 != 0:
                    m[y] = replace_char_at_index(m[y], x, c[1])
                    m[y] = replace_char_at_index(m[y], x + 1, c[0])
    return(m)

def draw_map(r_pos, wandh, boxes, walls, xscale):
    
    visual_map = []
    row_string = ""
    
    for i in range(wandh[0]):
        row_string += "."
        
    for j in range(wandh[1]):
        visual_map.append(row_string)

    visual_map = replace_characters_in_map(boxes, "[]", visual_map)
    visual_map = replace_characters_in_map(walls, "##", visual_map)
    visual_map = replace_characters_in_map(r_pos, "@.", visual_map)
        
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
with open("AoC_2024_Puzzle15Data_test3.txt", "r") as f:
    data = f.readlines()

map = []
instructions = ""
input_break = True
wandh = []
x_scale = 2

for line in data:
    
    if line != "\n":
        if input_break:
            map.append(line.strip("\n"))
        else:
            instructions += (line.strip("\n"))
    else: 
        input_break = False 

robot_pos = find_robot(map, "@")
walls = find_symbols_in_map(map, "#")
boxes = find_symbols_in_map(map, "O")
wandh = [x_scale * len(map[0]) ,len(map)]

#Scale Points in Walls, Boxes and Robot Position
for i in range(len(walls)):
    walls[i] = [x_scale * walls[i][0], walls[i][1]]
for i in range(len(boxes)):
    boxes[i] = [x_scale * boxes[i][0], boxes[i][1]]
robot_pos = [x_scale * robot_pos[0], robot_pos[1]]

final_map = draw_map(robot_pos, wandh, boxes, walls, x_scale)
for line in final_map:
    print(line)

for i in range(len(instructions)):
    robot_pos, boxes = move_robot(robot_pos, instructions[i], walls, boxes, x_scale)
    final_map = draw_map(robot_pos, wandh, boxes, walls, x_scale)
    print("After step", i+1, instructions[i])
    for line in final_map:
        print(line)

final_map = draw_map(robot_pos, wandh, boxes, walls, x_scale)

gps_total = 0
x_factor = 1
y_factor = 100

for box in boxes:
    gps_total += x_factor * box[0] + y_factor * box[1]

#for line in final_map:
#    print(line)
    
print("The total of the GPS coordinates iss =", gps_total)
