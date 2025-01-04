# Advent of Code 2024 Puzzle 18

# Import necessary libraries
from collections import defaultdict
import heapq

# define sub functions

def replace_char_at_index(s, index, new_char):
    # Convert the string to a list of characters
    char_list = list(s)
    
    # Replace the character at the specified index
    char_list[index] = new_char
    
    # Convert the list back to a string
    return ''.join(char_list)

def find_symbol(m, sym):
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == sym:
                s_location = (x, y)
                break
    
    return s_location

def find_symbols_in_map(m, sym):
    
    sym_loc = []

    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == sym:
                sym_loc.append([x, y])
    
    return sym_loc

# Define subfunctions

def calculate_turn_cost(prev_dir, curr, next_):
    # Calculate movement direction as (dx, dy)
    curr_to_next = (next_[0] - curr[0], next_[1] - curr[1])

    if prev_dir is None:  # Starting point, no cost for direction change
        return 1, curr_to_next
    if prev_dir == curr_to_next:  # No change in direction
        return 1, curr_to_next
    elif prev_dir == (-curr_to_next[0], -curr_to_next[1]):  # Reversal
        return 1, curr_to_next
    else:  # 90-degree turn
        return 1, curr_to_next

def find_shortest_path_with_weights(graph, start, end, max_time=None, start_dir=None):
    # Priority queue: (cost, current_node, previous_direction, path_so_far)
    pq = [(0, start, start_dir, [start])]

    # Store the minimum cost to reach each node
    min_cost = {start: 0}

    while pq:
        cost, current, prev_dir, path = heapq.heappop(pq)

        # If we've reached the destination, return the path
        if current == end:
            return path, cost
        
        if max_time is not None:
            if cost > max_time:
                continue

        # Explore neighbors
        for neighbor in graph.get(current, []):
            turn_cost, new_dir = calculate_turn_cost(prev_dir, current, neighbor)
            new_cost = cost + turn_cost

            # If this path is cheaper, or we haven't visited this node
            if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, new_dir, path + [neighbor]))

    # If no path is found
    return [], float('inf')

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

def replace_character_in_map(point, c, m):
    if point[0] < len(m[0]) and point[1] < len(m):
        m[point[1]] = replace_char_at_index(m[point[1]], point[0], c)
    
    return(m)

def draw_map(wandh, path, walls):
    
    visual_map = []
    row_string = ""
    
    for i in range(wandh[0]):
        row_string += "."
        
    for j in range(wandh[1]):
        visual_map.append(row_string)

    visual_map = replace_characters_in_map(walls, "#", visual_map)
    visual_map = replace_characters_in_map(path, "*", visual_map)
        
    return visual_map

def map_potential_steps(wandh, walls):

    points_graph = defaultdict(list)
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for y in range(wandh[1]):
        for x in range(wandh[0]):
            
            if [x, y] not in walls:
                label = (x, y)
                points_graph[label] = []

                for coords in directions:
                    new_pos = (x + coords[0], y + coords[1])
                    if [new_pos[0], new_pos[1]] not in walls:
                        points_graph[label].append(new_pos)

    return points_graph

def find_shortcuts(walls, wandh, delta_time):

    walls_to_pass = []
    # Define the list of coordinates
    coordinates = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(len(walls)):
        if walls[i][0] > 0 and walls[i][0] < wandh[0] and walls[i][1] > 0 and walls[i][1] < wandh[1]:
            
            point_check = 0

            # Enumerate through the coordinates
            for index, (x, y) in enumerate(coordinates):
                if [walls[i][0] + x, walls[i][1] + y] not in walls:
                    point_check += 1
            
            if point_check >= 2:            
                walls_to_pass.append(walls[i])

    return walls_to_pass

def adjust_graph(points_graph, walls, wandh, wall_to_remove):
    
    points_graph[(wall_to_remove[0], wall_to_remove[1])] = []
    
    if (wall_to_remove[0] - 1, wall_to_remove[1]) in points_graph:
        points_graph[(wall_to_remove[0] - 1, wall_to_remove[1])].append((wall_to_remove[0], wall_to_remove[1]))
        points_graph[(wall_to_remove[0], wall_to_remove[1])].append((wall_to_remove[0] - 1, wall_to_remove[1]))
    if (wall_to_remove[0] + 1, wall_to_remove[1]) in points_graph:
        points_graph[(wall_to_remove[0] + 1, wall_to_remove[1])].append((wall_to_remove[0], wall_to_remove[1]))
        points_graph[(wall_to_remove[0], wall_to_remove[1])].append((wall_to_remove[0] + 1, wall_to_remove[1]))
    if (wall_to_remove[0], wall_to_remove[1] - 1) in points_graph:
        points_graph[(wall_to_remove[0], wall_to_remove[1] - 1)].append((wall_to_remove[0], wall_to_remove[1]))
        points_graph[(wall_to_remove[0], wall_to_remove[1])].append((wall_to_remove[0], wall_to_remove[1]) - 1)
    if (wall_to_remove[0], wall_to_remove[1] + 1) in points_graph:
        points_graph[(wall_to_remove[0], wall_to_remove[1] + 1)].append((wall_to_remove[0], wall_to_remove[1]))
        points_graph[(wall_to_remove[0], wall_to_remove[1])].append((wall_to_remove[0], wall_to_remove[1]) + 1)
    
    return points_graph

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle20Data_test.txt", "r") as f:
    data = f.readlines()

map = []
wandh = []
potential_steps = []
path = []

for line in data:
    map.append(line.strip("\n"))

start = find_symbol(map, "S")
end = find_symbol(map, "E")
walls = find_symbols_in_map(map, "#")
wandh = [len(map[0]) ,len(map)]
potential_steps = map_potential_steps(wandh, walls)
potential_shortcuts = []

#start_dir = (1, 0)
start_dir = None
max_time = None
delta_time = 2
cheats = {}
total_cheats_100 = 0

path, max_time = find_shortest_path_with_weights(potential_steps, start, end, max_time, start_dir)

potential_shortcuts = find_shortcuts(walls, wandh, delta_time)

for wall_shortcut in walls:
    if wall_shortcut in potential_shortcuts:
        print(wall_shortcut)
        new_walls = walls.copy()
        new_walls.remove(wall_shortcut)
#        potential_steps = map_potential_steps(wandh, new_walls)

        working_potential_steps = adjust_graph(potential_steps.copy(), walls, wandh, wall_shortcut)
    
        path, path_score = find_shortest_path_with_weights(working_potential_steps, start, end, max_time, start_dir)
           
        if (max_time - path_score) not in cheats and path_score < max_time:
            cheats[max_time - path_score] = 1
        elif (max_time - path_score) in cheats and path_score < max_time:
            cheats[max_time - path_score] += 1
        
        if max_time - path_score >= 100:
            total_cheats_100 += 1

#for key, value in potential_steps.items():
#    print(key, value)
#for point in path:
#    path[path.index(point)] = [point[0], point[1]]

#final_map = draw_map(wandh, path, walls)
#final_map = replace_character_in_map(start, "S", final_map)
#final_map = replace_character_in_map(end, "E", final_map)

#for line in final_map:
#    print(line)

#print("The shortest path length is", shortest_path)
for key, value in cheats.items():
    print("There are", value, "cheats that save", key, "nanoseconds")
    
print("There are", total_cheats_100, "cheats that save 100 nanoseconds or more")
