# Advent of Code 2023 Puzzle 8a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle8Data_Test1.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

# Close file
f.close()

instructions = data[0].strip()
nodes = []
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
    print(nodes[i], directions_left[i], directions_right[i])

i = 0
loops = 0
current_node = "AAA"

while current_node != "ZZZ":
    node_index = nodes.index(current_node)
    if instructions[i] == "L":
        current_node = directions_left[node_index]
    if instructions[i] == "R":
        current_node = directions_right[node_index]
    i += 1
    print(i)
    if i == len(instructions):
        i = 0
        loops += 1

Total_Steps = i + (loops * len(instructions))
print(i, loops, len(instructions))

print("The total number of steps is = ", Total_Steps)


