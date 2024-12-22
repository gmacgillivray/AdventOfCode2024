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

def plot_point_next_steps(pts):
    
    return_graph_points = defaultdict(list)
  
    for i in range(len(pts)):
        label = (pts[i][0],pts[i][1])
        return_graph_points[label] = []
        
        for j in range(len(pts)):
            if [pts[i][0] + 1, pts[i][1]] == pts[j] or [pts[i][0] - 1, pts[i][1]] == pts[j] or [pts[i][0], pts[i][1] + 1] == pts[j] or [pts[i][0], pts[i][1] - 1] == pts[j]:
                if pts[j] not in return_graph_points[label]:
                    return_graph_points[label].append((pts[j][0],pts[j][1])) 

    return return_graph_points

def longest_path(graph, start, visited=None):
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(start)

    # Initialize the maximum path length
    max_length = 0

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            current_length = 1 + longest_path(graph, neighbor, visited.copy())
            max_length = max(max_length, current_length)

    # Unmark the current node as visited (backtrack)
    visited.remove(start)

    return max_length

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle14Data.txt", "r") as f:
    data = f.readlines()

pos = []
vel = []
total_total = 0
map_size = [101, 103]
robot_visual_map = []
quadrant_totals = []

for line in data:
    if line != "\n":
        str_one, str_two = (line.strip("\n").split(" "))
        x, y = str_one.strip("p=").split(",")
        vx, vy = str_two.strip("v=").split(",")
        pos.append([int(x), int(y)])
        vel.append([int(vx), int(vy)])

#robot_visual_map = draw_map(pos, map_size)
#for line in robot_visual_map:
#    print(line)

#print("\n")

time = 10000
t = 0    
graph_points = defaultdict(list)
found_pattern = False

while not found_pattern and t < time:
    
    print(t)
    
    connected_points_total = 0
       
    pos = move_robot_fleet(pos, vel, 1, map_size)
    graph_points = plot_point_next_steps(pos)    
    for key, value in graph_points.items():
        if value != []:
            connected_points_total += 1

    if connected_points_total > 300:
        found_pattern = True     

    t += 1

robot_visual_map = draw_map(pos, map_size)

for i in range(len(robot_visual_map)):
    print(robot_visual_map[i])
    
quadrant_totals = count_quadrants(pos, map_size)

for i in range(len(quadrant_totals)):
    if i == 0:
        total_total = quadrant_totals[i]
    else:
        total_total *= quadrant_totals[i]
print(quadrant_totals, t)
print("The total number of tokens to maximize prizes =", total_total)
