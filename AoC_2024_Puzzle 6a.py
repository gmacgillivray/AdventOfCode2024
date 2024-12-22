# Advent of Code 2024 Puzzle 6

# Import necessary libraries
import re
from collections import defaultdict

# Open the file and read all lines into a list
f = open ("AoC_2024_Puzzle6Data.txt", "r")
data = f.readlines()
f.close()

# Define subfunctions
def replace_char_at_index(s, index, new_char):
    # Convert the string to a list of characters
    char_list = list(s)
    
    # Replace the character at the specified index
    char_list[index] = new_char
    
    # Convert the list back to a string
    return ''.join(char_list)

# Define variables and initialize
a = []
b = []
pos = []
next_pos = []
next_step = []
new_next_step = []
index_X = []
sum = 0
sumb = 0
page_order = defaultdict(dict)
char_to_replace = "X"

for line in data:
    a.append(line.strip("\n"))
    b.append(line.strip("\n"))


for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == "^":
            pos.append(i)
            pos.append(j)
            next_step = [-1, 0]
        if a[i][j] == ">":
            pos.append(i)
            pos.append(j)
            next_step = [0, 1]
        if a[i][j] == "v":
            pos.append(i)
            pos.append(j)
            next_step = [1, 0]
        if a[i][j] == "<":
            pos.append(i)
            pos.append(j)
            next_step = [0, -1]     

guard_in_map = True

b[pos[0]] = replace_char_at_index(b[pos[0]], pos[1], char_to_replace)

next_pos = [pos[0] + next_step[0], pos[1] + next_step[1]]
new_next_step = [next_step[0], next_step[1]]

if next_pos[0] > len(a) or next_pos[1] > len(a[0]) or next_pos[0] < 0 or next_pos[1] < 0:
    guard_in_map = False

while guard_in_map:   

    if a[next_pos[0]][next_pos[1]] == "#":
        if next_step == [0, 1]:
            new_next_step = [1, 0]
        if next_step == [1, 0]:
            new_next_step = [0, -1]
        if next_step == [0, -1]:
            new_next_step = [-1, 0]
        if next_step == [-1, 0]:
            new_next_step = [0, 1]
    
    next_step[0] = new_next_step[0]
    next_step[1] = new_next_step[1]
    
    pos[0] = pos[0] + next_step[0]
    pos[1] = pos[1] + next_step[1]
    
    b[pos[0]] = replace_char_at_index(b[pos[0]], pos[1], char_to_replace)
    
    next_pos[0] = pos[0] + next_step[0]
    next_pos[1] = pos[1] + next_step[1]
    
    print(len(a), len(a[0]), next_pos[0], next_pos[1])
    
    if next_pos[0] >= len(a) or next_pos[1] >= len(a[0]) or next_pos[0] < 0 or next_pos[1] < 0:
        guard_in_map = False    

print(data)
print(a)
print(b)

for i in range(len(b)):
    for j in range(len(b[0])):
        if b[i][j] == "X":
            sum += 1

# Print the results
print("The sum of all squares where the guard has occupied is", sum)
#print("The sum of all middle values for re-ordering incorrectly ordered updates ", sumb)