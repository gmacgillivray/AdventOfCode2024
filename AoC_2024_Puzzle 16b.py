# Advent of Code 2024 Puzzle 13

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

# Define subfunctions

def calculate_turn_cost(prev_dir, curr, next_):
    # Calculate movement direction as (dx, dy)
    curr_to_next = (next_[0] - curr[0], next_[1] - curr[1])

    if prev_dir is None:  # Starting point, no cost for direction change
        return 0, curr_to_next
    
    if prev_dir == curr_to_next:  # No change in direction
        return 1, curr_to_next
    elif prev_dir == (-curr_to_next[0], -curr_to_next[1]):  # Reversal
        return 2001, curr_to_next
    else:  # 90-degree turn
        return 1001, curr_to_next

def is_prefix(path, ignored_paths):
    """Check if the given path matches any ignored path."""
    path = tuple(path)

    for ignored in ignored_paths:
        if len(path) == len(ignored) and path == ignored:
            return True
    return False

def find_shortest_path_with_weights(
    graph, start, end, start_dir=None, ignore_full_paths=None, max_score=float('inf')
):
    """
    Find the shortest path with weights, ignoring specific full paths and stopping if the cost exceeds `max_score`.
    
    :param graph: Dictionary where keys are nodes and values are lists of neighboring nodes.
    :param start: Starting node.
    :param end: Destination node.
    :param start_dir: Starting direction as a tuple (dx, dy).
    :param ignore_full_paths: List of full paths to ignore.
    :param max_score: Maximum allowable cost for the path.
    :return: Tuple (shortest_path, cost) or ([], inf) if no valid path exists.
    """
    # Priority queue: (cost, current_node, previous_direction, path_so_far)
    pq = [(0, start, start_dir, [start])]

    # Convert ignored paths to tuples for efficient comparison
    ignore_full_paths = [tuple(p) for p in (ignore_full_paths or [])]

    # Store the minimum cost to reach each path
    min_cost = {}

    while pq:
        cost, current, prev_dir, path = heapq.heappop(pq)

        # If the current path cost exceeds max_score, skip further exploration
        if cost > max_score:
            continue

        # If the current path is a prefix of any ignored path, skip it
        if is_prefix(path, ignore_full_paths):
            continue

        # If we've reached the destination, return the path
        if current == end:
            return path, cost

        # Explore neighbors
        for neighbor in graph.get(current, []):
            turn_cost, new_dir = calculate_turn_cost(prev_dir, current, neighbor)
            new_cost = cost + turn_cost

            new_path = path + [neighbor]

            # If this path is cheaper, or we haven't visited this path
            if tuple(new_path) not in min_cost or new_cost < min_cost[tuple(new_path)]:
                min_cost[tuple(new_path)] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, new_dir, new_path))

    # If no path is found
    return [], float('inf')


def move_reinder(p, move, walls, boxes):

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
with open("AoC_2024_Puzzle16Data_test2.txt", "r") as f:
    data = f.readlines()

map = []
instructions = ""
wandh = []
potential_steps = []
path = []

for line in data:
    map.append(line.strip("\n"))

start = find_robot(map, "S")
end = find_robot(map, "E")
walls = find_symbols_in_map(map, "#")
wandh = [len(map[0]) ,len(map)]
start_dir = (1, 0)
potential_steps = map_potential_steps(wandh, walls)
ignore_paths = []

path, path_score = find_shortest_path_with_weights(potential_steps, start, end, start_dir)
temp_path_score = path_score

k = 0

while temp_path_score == path_score and k <= 100:
    print(k)
#    path.remove(end)
    ignore_paths.append(path)
    path, temp_path_score = find_shortest_path_with_weights(potential_steps, start, end, start_dir, ignore_paths, path_score)
    k += 1

seating_tiles = []

for i in range(len(ignore_paths)):
    for point in ignore_paths[i]:
        if point not in seating_tiles:
            seating_tiles.append(point)

#for key, value in potential_steps.items():
#    print(key, value)
for point in seating_tiles:
    seating_tiles[seating_tiles.index(point)] = [point[0], point[1]]

final_map = draw_map(wandh, seating_tiles, walls)
for line in final_map:
    print(line)

print("The number of seating tiles is", len(seating_tiles))
