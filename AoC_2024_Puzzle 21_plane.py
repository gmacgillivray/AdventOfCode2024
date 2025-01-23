# Advent of Code 2024 Puzzle 18

# Import necessary libraries
from collections import defaultdict
import heapq

# define sub functions

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

# pseudo code
# Create a loop to go through the points
# will need a lookout to translate the symbol to a point which I think you've got
# start is on A
# end is the button to get to
# call find shortest path with weights and return all paths
# create an all paths list
# take all return paths and add to the paths list
# Add an A to the return paths
# Then loop back to create a new start based on the last end
# add new set of paths to existing list
# after getting to the end

#print("The shortest path length is", shortest_path)
for key, value in cheats.items():
    print("There are", value, "cheats that save", key, "nanoseconds")
    
print("There are", total_cheats_100, "cheats that save 100 nanoseconds or more")
