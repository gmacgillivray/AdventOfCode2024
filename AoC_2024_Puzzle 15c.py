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

def find_symbols_in_map(m, sym):
    
    sym_loc = []

    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == sym:
                sym_loc.append([x, y])
    
    return sym_loc

def move_robot(p, move, walls, boxes):

    directions = {"<": [-1, 0], ">": [1, 0], "^": [0, -1], "v": [0, 1]}

    # Determine movement vector
    vector = directions.get(move)
    if vector is None:
        raise ValueError("Invalid move symbol")

    # Determine how many boxes can be moved if any by looking ahead to see if there are free spaces to move
    found_a_wall = False
    found_a_space = False
    new_pos = [p[0] + vector[0], p[1] + vector[1]]
    k = 0

    while not found_a_wall and not found_a_space:
        if new_pos in walls:
            found_a_wall = True
            k = 0
        elif new_pos in boxes:
            k += 1
        else:
            found_a_space = True

        new_pos = [new_pos[0] + vector[0], new_pos[1] + vector[1]]

    # Calculate new positions
    if found_a_space:
        p = [p[0] + vector[0], p[1] + vector[1]]
        if k > 0:
            box_new_pos = [p[0] + k * vector[0], p[1] + k * vector[1]]
            boxes[boxes.index([p[0], p[1]])] = box_new_pos
    
    return p, boxes

def move_robot_2(p, move, boxes_l, boxes_r, walls):

    directions = {"<": [-1, 0], ">": [1, 0], "^": [0, -1], "v": [0, 1]}

    # Determine movement vector
    vector = directions.get(move)
    if vector is None:
        raise ValueError("Invalid move symbol")

    # Determine how many boxes can be moved if any by looking ahead to see if there are free spaces to move
    found_a_wall = False
    found_a_space = False
    new_pos = [p[0] + vector[0], p[1] + vector[1]]
    k = 0

    while not found_a_wall and not found_a_space:
        if new_pos in walls:
            found_a_wall = True
            k = 0
        elif new_pos in boxes_l or new_pos in boxes_r:
            k += 1
        else:
            found_a_space = True

        new_pos = [new_pos[0] + vector[0], new_pos[1] + vector[1]]

    if vector[1] == 0:
#        k = int(k/2)
        step = 2
    else:
        step = 1

    new_boxes_l = boxes_l.copy()
    new_boxes_r = boxes_r.copy()

    # Calculate new positions
    if found_a_space:
        p = [p[0] + vector[0], p[1] + vector[1]]
        if k > 0:
            for i in range(0,k,step):
                box_new_pos = [p[0] + i * vector[0], p[1] + i * vector[1]]
                if [box_new_pos[0], box_new_pos[1]] in boxes_l and vector[1] == 0:
                    index_l = boxes_l.index([box_new_pos[0], box_new_pos[1]])
                    new_boxes_l[index_l] = [box_new_pos[0] + 1, box_new_pos[1]]
                    new_boxes_r[index_l] = [box_new_pos[0] + 2, box_new_pos[1]]
                elif [box_new_pos[0], box_new_pos[1]] in boxes_r and vector[1] == 0:
                    index_r = boxes_r.index([box_new_pos[0], box_new_pos[1]])
                    new_boxes_r[index_r] = [box_new_pos[0] - 1, box_new_pos[1]]
                    new_boxes_l[index_r] = [box_new_pos[0] - 2, box_new_pos[1]]
                elif [box_new_pos[0], box_new_pos[1]] in boxes_l and vector[0] == 0:
                    index_l = boxes_l.index([box_new_pos[0], box_new_pos[1]])
                    new_boxes_l[index_l] = [box_new_pos[0], box_new_pos[1] + vector[1]]
                    new_boxes_r[index_l] = [box_new_pos[0] + 1, box_new_pos[1] + vector[1]] 
                elif [box_new_pos[0], box_new_pos[1]] in boxes_r and vector[0] == 0:
                    index_r = boxes_r.index([box_new_pos[0], box_new_pos[1]])
                    new_boxes_r[index_r] = [box_new_pos[0], box_new_pos[1] + vector[1]]
                    new_boxes_l[index_r] = [box_new_pos[0] - 1, box_new_pos[1] + vector[1]]
    
    return p, new_boxes_l, new_boxes_r

def replace_characters_in_map(p, c, m):
    for y in range(len(m)):
        for x in range(len(m[y])):     
            if len(p) != 2:
                if [x, y] in p:
                    m[y] = replace_char_at_index(m[y], x, c)
            else:
                if [x, y] == [p[0], p[1]]:
                    m[y] = replace_char_at_index(m[y], x, c)
    
    return(m)

def draw_map(r_pos, wandh, boxes, walls):
    
    visual_map = []
    row_string = ""
    
    for i in range(wandh[0]):
        row_string += "."
        
    for j in range(wandh[1]):
        visual_map.append(row_string)

    visual_map = replace_characters_in_map(boxes, "O", visual_map)
    visual_map = replace_characters_in_map(walls, "#", visual_map)
    visual_map = replace_characters_in_map(r_pos, "@", visual_map)
        
    return visual_map

def draw_map_2(r_pos, wandh, boxes_l, boxes_r, walls):
    
    visual_map = []
    row_string = ""
    
    for i in range(wandh[0]):
        row_string += "."
        
    for j in range(wandh[1]):
        visual_map.append(row_string)

    visual_map = replace_characters_in_map(boxes_l, "[", visual_map)
    visual_map = replace_characters_in_map(boxes_r, "]", visual_map)
    visual_map = replace_characters_in_map(walls, "#", visual_map)
    visual_map = replace_characters_in_map(r_pos, "@", visual_map)
        
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
boxes_l = []
boxes_r = []
walls_2 = []

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
wandh = [2 * len(map[0]) ,len(map)]

for i in range(len(walls)):
    walls_2.append([2 * walls[i][0], walls[i][1]])
    walls_2.append([2 * walls[i][0] + 1, walls[i][1]])

for i in range(len(boxes)):
    boxes_l.append([2 * boxes[i][0], boxes[i][1]])
    boxes_r.append([2 * boxes[i][0] + 1, boxes[i][1]])

robot_pos = [2 * robot_pos[0], robot_pos[1]]

final_map = draw_map_2(robot_pos, wandh, boxes_l, boxes_r, walls_2)
for line in final_map:
    print(line)

for i in range(len(instructions)):
    robot_pos, boxes_l, boxes_r = move_robot_2(robot_pos, instructions[i], boxes_l, boxes_r, walls_2)
    final_map = draw_map_2(robot_pos, wandh, boxes_l, boxes_r, walls_2)
    print("After step", i+1, instructions[i])
    for line in final_map:
        print(line)

gps_total = 0
x_factor = 1
y_factor = 100

for box in boxes_l:
    gps_total += x_factor * box[0] + y_factor * box[1]

#for line in final_map:
#    print(line)
    
print("The total of the GPS coordinates iss =", gps_total)
