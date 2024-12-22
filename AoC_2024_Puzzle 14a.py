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

def move_robot(position, velocity, t, size):
    
    new_pos_x = (position[0] + velocity[0] * t) % size[0]
    new_pos_y = (position[1] + velocity[1] * t) % size[1]

    return [new_pos_x, new_pos_y]

def move_robot_fleet(all_pos, all_vel, t, size):
    
    for i in range(len(all_pos)):
        all_pos[i] = move_robot(all_pos[i], all_vel[i], t, size)
    
    return all_pos

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
with open("AoC_2024_Puzzle14Data_test.txt", "r") as f:
    data = f.readlines()

pos = []
vel = []
total_total = 0
map_size = [11, 7]
time = 100
robot_visual_map = []
quadrant_totals = []

for line in data:
    if line != "\n":
        str_one, str_two = (line.strip("\n").split(" "))
        x, y = str_one.strip("p=").split(",")
        vx, vy = str_two.strip("v=").split(",")
        pos.append([int(x), int(y)])
        vel.append([int(vx), int(vy)])

robot_visual_map = draw_map(pos, map_size)
for line in robot_visual_map:
    print(line)

print("\n")

pos = move_robot_fleet(pos, vel, time, map_size)
robot_visual_map = draw_map(pos, map_size)

for line in robot_visual_map:
    print(line)

quadrant_totals = count_quadrants(pos, map_size)



for i in range(len(quadrant_totals)):
    if i == 0:
        total_total = quadrant_totals[i]
    else:
        total_total *= quadrant_totals[i]

print(quadrant_totals)
print("The total number of tokens to maximize prizes =", total_total)
