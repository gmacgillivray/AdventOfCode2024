# Advent of Code 2024 Puzzle 11

# Import necessary libraries
from collections import defaultdict

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle11Data.txt", "r") as f:
    data = f.readlines()
f.close()

# Define subfunctions

# Define variables and initialize
a = []
b = []
num_paths = 0
reachable = 0
starting_points = []
ending_points = []
points_graph = defaultdict(list)

for line in data:
    a.append(line.strip("\n").split(" "))

for i in range(len(a[0])):
    b.append(int(a[0][i]))
    
num_of_blinks = 25

for i in range(num_of_blinks):
    for j in range(len(b)):
        if b[j] == 0:
            b[j] = 1
        else:
            working_string = str(b[j])
            if len(working_string) % 2 == 0:
                half_digits = int(len(working_string) / 2)
                string_one = working_string[0:half_digits]
                string_two = working_string[half_digits:2 * half_digits]
                b[j] = int(string_one)
                b.append(int(string_two))
            else:
                b[j] *= 2024

print(b)
   
#Print the results
print("The total number of stones is =", len(b))

