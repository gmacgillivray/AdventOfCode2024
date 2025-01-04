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
        return 0, curr_to_next
    if prev_dir == curr_to_next:  # No change in direction
        return 1, curr_to_next
    elif prev_dir == (-curr_to_next[0], -curr_to_next[1]):  # Reversal
        return 1, curr_to_next
    else:  # 90-degree turn
        return 1, curr_to_next

def find_shortest_path_with_weights(graph, start, end, start_dir=None):
    # Priority queue: (cost, current_node, previous_direction, path_so_far)
    pq = [(0, start, start_dir, [start])]

    # Store the minimum cost to reach each node
    min_cost = {start: 0}

    while pq:
        cost, current, prev_dir, path = heapq.heappop(pq)

        # If we've reached the destination, return the path
        if current == end:
            return path, cost

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
                    if new_pos not in walls:
                        points_graph[label].append(new_pos)

    return points_graph


# Open the file and read all lines into a list
with open("AoC_2024_Puzzle18Data.txt", "r") as f:
    data = f.readlines()

time_bytes = len(data)
grid_size = 71

map = []
potential_steps = []
path = []
walls = []
time_walls = []
wandh = [grid_size, grid_size]
start = (0, 0)
end = (grid_size - 1, grid_size - 1)


for line in data:
    temp_x, temp_y = line.strip("\n").strip(" ").split(",")
    walls.append([int(temp_x), int(temp_y)])

infinity = float("inf")
path_score = 0
k = 2900

while path_score != infinity:

    time_walls = []
    
    k += 1
    # define map for the first bytes that have fallen
    for i in range(k):
        time_walls.append(walls[i])

    #start_dir = (1, 0)
    start_dir = None
    potential_steps = map_potential_steps(wandh, time_walls)

    path, path_score = find_shortest_path_with_weights(potential_steps, start, end, start_dir)
    print(k, path_score, walls[k - 1])


#for key, value in potential_steps.items():
#    print(key, value)
for point in path:
    path[path.index(point)] = [point[0], point[1]]

final_map = draw_map(wandh, path, time_walls)
for line in final_map:
    print(line)

print("The first byte that prevents navigation is", walls[k - 1])
