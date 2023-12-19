# Advent of Code 2023 Puzzle 8a

import math

# Open text file with all of the data
f = open ("AoC_2023_Puzzle8Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

# Close file
f.close()

instructions = data[0].strip()
nodes = []
current_nodes = []
directions_left = []
directions_right = []

for r in range(2, len(data)):
    a, b = data[r].strip().split("=")
    a = a.strip()
    nodes.append(a)
    c, d = b.strip().split(",")
    c = c.strip("(").strip()
    d = d.strip(")").strip()
    directions_left.append(c)
    directions_right.append(d)

for i in range(len(nodes)):
    current_node = nodes[i]
    if current_node[2] == 'A':
        current_nodes.append(current_node)

#for j in range(len(current_nodes)):
#    print("Ends with A", current_nodes[j])

b_intercepts = []
m_slopes = []
b_totals = 0
m_totals = 0

for j in range(len(current_nodes)):
    working_node = current_nodes[j]
    
    i = 0
    loops = 0
    NotFinished = True
    print("Initial Working Node = ", working_node)
    while working_node[2] != "Z":
        node_index = nodes.index(working_node)
        if instructions[i] == "L":
            working_node = directions_left[node_index]
        if instructions[i] == "R":
            working_node = directions_right[node_index]
        i += 1
        in_loop_counter = i
        if i == len(instructions):
            i = 0
            loops += 1        
    
    b_intercepts.append(i + (loops * len(instructions)))
    b_totals += i + (loops * len(instructions))

    initial_i = i
    loops = 0
    NotFinished = True

    node_index = nodes.index(working_node)
    if instructions[i] == "L":
        working_node = directions_left[node_index]
    if instructions[i] == "R":
        working_node = directions_right[node_index]
    i += 1

    while working_node[2] != "Z":
        node_index = nodes.index(working_node)
        if instructions[i] == "L":
            working_node = directions_left[node_index]
        if instructions[i] == "R":
            working_node = directions_right[node_index]
        i += 1
        if i == len(instructions):
            i = 0
            loops += 1  
    
    m_slopes.append(i - initial_i + (loops * len(instructions)))
    m_totals += i - initial_i + (loops * len(instructions))

Total_Steps = math.lcm(m_slopes[0], m_slopes[1],m_slopes[2], m_slopes[3],m_slopes[4], m_slopes[5])

print("The total number of steps is = ", Total_Steps)


