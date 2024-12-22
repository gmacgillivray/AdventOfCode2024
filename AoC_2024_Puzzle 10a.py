# Advent of Code 2024 Puzzle 10

# Import necessary libraries
from collections import defaultdict

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle10Data.txt", "r") as f:
    data = f.readlines()

# Define subfunctions
def count_paths(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    # If start and end are the same, there is one path
    if start == end:
        return 1

    # Mark the current node as visited
    visited.add(start)

    # Initialize path count
    path_count = 0

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            path_count += count_paths(graph, neighbor, end, visited.copy())

    return path_count

# Define variables and initialize
a = []
num_paths = 0
reachable = 0
starting_points = []
ending_points = []
points_graph = defaultdict(list)

for line in data:
    a.append(line.strip("\n"))

for i in range(len(a)):
    for j in range(len(a[i])):
        label = (i, j)

        if i + 1 < len(a) and j < len(a[i + 1]):
            if int(a[i + 1][j]) - int(a[i][j]) == 1:
                points_graph[label].append((i+1, j))
        if i - 1 >= 0 and j < len(a[i - 1]):
            if int(a[i - 1][j]) - int(a[i][j]) == 1:
                points_graph[label].append((i-1, j))
        if j + 1 < len(a[i]):
            if int(a[i][j + 1]) - int(a[i][j]) == 1:
                points_graph[label].append((i, j+1))
        if j - 1 >= 0:
            if int(a[i][j - 1]) - int(a[i][j]) == 1:
                points_graph[label].append((i, j-1))

        if a[i][j] == "0":
            starting_points.append((i, j))
        if a[i][j] == "9":
            ending_points.append((i, j))

for start in starting_points:
    
    for end in ending_points:
        temp_paths = count_paths(points_graph, start, end)
        num_paths += temp_paths
        if temp_paths > 0:
            reachable += 1    
    
# Print the results
print("The total trailhead score is =", reachable)
print("The total number of valid trails is =", num_paths)

#for key, value in points_graph.items():
#    print(f"{key}: {value}")
    
#print(starting_points)
#print(ending_points)