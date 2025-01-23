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

def find_shortest_path_with_weights_2(graph, start, end, start_dir=None):
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

def is_prefix(path, ignored_paths):
    """Check if the given path matches any ignored path."""
    
#    for ignored in ignored_paths:
#        if len(path) <= len(ignored) and path == ignored[:len(path)]:
#            return True

    for i in range(len(ignored_paths)):
        if len(path) <= len(ignored_paths[i]) and path == ignored_paths[i][:len(path)]:
            return True
           
    return False

def find_shortest_path_with_weights_3(graph, start, end, start_dir=None, max_score=float('inf'), ignore_paths=None):
    # Priority queue: (cost, current_node, previous_direction, path_so_far)
    pq = [(0, start, start_dir, [start])]
    all_paths = []
    all_costs = []
    alternate_paths = {}

    # Store the minimum cost to reach each node
    min_cost = {start: 0}

    # Convert ignore_paths to sets for easier comparison
    #ignore_paths = set(tuple(path) for path in (ignore_paths or []))

    while pq:
        cost, current, prev_dir, path = heapq.heappop(pq)

        # Add check for a max score to speed up calculation
        if cost > max_score:
            continue

        # Check if the current path matches any ignored path
        # If the current path is a prefix of any ignored path, skip it
#        if is_prefix(path, ignore_paths):
#            continue

        # If we've reached the destination, save the path to the list
        if current == end and not is_prefix(path, ignore_paths):
#            all_paths.append(path)
#            all_costs.append(cost)
#            max_score = min(all_costs)
#            continue
            return path, cost

        if current == end and is_prefix(path, ignore_paths):
            continue

        # Explore neighbors
        for neighbor in graph.get(current, []):
            turn_cost, new_dir = calculate_turn_cost(prev_dir, current, neighbor)
            new_cost = cost + turn_cost

            # Only process the neighbor if the new cost is lower
#            if neighbor not in min_cost or new_cost < min_cost[neighbor]:
#                min_cost[neighbor] = new_cost
#                heapq.heappush(pq, (new_cost, neighbor, new_dir, path + [neighbor]))

            # If this path is cheaper, or we haven't visited this node
            if not is_prefix(path, ignore_paths):
                if neighbor not in min_cost:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, new_dir, path + [neighbor]))
            # If this path is cheaper and not a prefix of any ignored path
                elif new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, new_dir, path + [neighbor]))
            # Continue to follow the path of an ignored path in case there are variants further down
            elif is_prefix(path, ignore_paths):
                heapq.heappush(pq, (new_cost, neighbor, new_dir, path + [neighbor]))
#                if neighbor in alternate_paths:
#                    alternate_paths.pop(neighbor)
#            elif new_cost == min_cost[neighbor]:
#                if neighbor not in alternate_paths:
#                   alternate_paths[neighbor] = [path + [neighbor]]
#                else:
#                    alternate_paths[neighbor].append(path + [neighbor])

    # Return

    #return all_paths, all_costs

  # If no path is found
    return [], float('inf')

def find_shortest_path_with_weights_3(graph, start, end, start_dir=None, max_score=float('inf')):
    # Priority queue: (cost, current_node, previous_direction, path_so_far)
    pq = [(0, start, start_dir, [start])]
    all_paths = []
    all_costs = []

    # Store the minimum cost to reach each node
    min_cost = {start: 0}

    # Convert ignore_paths to sets for easier comparison
    #ignore_paths = set(tuple(path) for path in (ignore_paths or []))

    while pq:
        cost, current, prev_dir, path = heapq.heappop(pq)

        # Add check for a max score to speed up calculation
        if cost > max_score:
            continue

        # If we've reached the destination, save the path to the list
        if current == end:
            all_paths.append(path)
            all_costs.append(cost)
            max_score = min(all_costs)
            continue

        # Explore neighbors
        for neighbor in graph.get(current, []):
            turn_cost, new_dir = calculate_turn_cost(prev_dir, current, neighbor)
            new_cost = cost + turn_cost

            # Only process the neighbor if we haven't visited the node, the new cost is lower or equal to account for multiple paths
            if neighbor not in min_cost or new_cost <= min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, new_dir, path + [neighbor]))

    return all_paths, all_costs

def convert_path_to_symbols(path):
    
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    step_symbols = ["<", ">", "v", "^"]
    
    for i in range(len(path) - 1)
        path_string = ""
        step = [path[i + 1][0] - path[i][0], path[i+1][1] - path[i][1]]
# need to validate the function to find the index of a value in a list
        index_step = index(step, directions)
        path_string += step_symbols[index_step]

    return path_string
