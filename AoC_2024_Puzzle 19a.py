# Advent of Code 2024 Puzzle 19

# Import necessary libraries
from collections import defaultdict
import heapq

def find_match(match_components, string_to_match, max_length):
    
    string_components = []
    all_strings = []
    
    # Priority queue: (cost, current_node, previous_direction, path_so_far)
    pq = [("", string_components)]

    while pq:
        build_string, string_components = heapq.heappop(pq)

        # If we've reached the destination, return the path
        if build_string == string_to_match:
            return True, string_components

        # If the building string doesn't match the first part of the string match eliminate the option
        if build_string != string_to_match[:len(build_string)]:
            continue

        # Explore matches and create build string
        loop_start = len(build_string)
        loop_max = len(string_to_match)
        
        if max_length <= (loop_max - loop_start):
            iter_chars = max_length
        else:
            iter_chars = loop_max - loop_start
        
        for l in range(iter_chars):
            
            temp_build_string = build_string
            temp_string_components = string_components.copy()
            temp_string_to_match = string_to_match[loop_start:loop_start + l + 1]
            
            if temp_string_to_match in match_components:
                temp_build_string += temp_string_to_match
                temp_string_components.append(temp_string_to_match)
                if temp_build_string not in all_strings:
                    all_strings.append(temp_build_string)
                    heapq.heappush(pq, (temp_build_string, temp_string_components))

    # If no path is found
    return False, []

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle19Data.txt", "r") as f:
    data = f.readlines()

available_towells = []
towell_patterns = []
available_towells = data[0].strip("\n").strip(" ").split(",")
for t in range(len(available_towells)):
    available_towells[t] = available_towells[t].strip(" ")

for i in range(2, len(data)):
    towell_patterns.append(data[i].strip("\n").strip(" "))
    
max_length_components = 0

for i in range(len(available_towells)):
    if len(available_towells[i]) > max_length_components:
        max_length_components = len(available_towells[i])

patterns_found = 0
k = 0

for pattern in towell_patterns:
    
    found_a_match = False
    towells_used = []
    found_a_match, towells_used = find_match(available_towells, pattern, max_length_components)

    if found_a_match:
        patterns_found += 1
    
    k += 1
    print(k, found_a_match, patterns_found, pattern)

print("The number of patterns that can be matched is ", patterns_found)

#print("The total number of tokens to maximize prizes =", total_total)

