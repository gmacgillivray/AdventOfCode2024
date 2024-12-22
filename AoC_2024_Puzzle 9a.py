# Advent of Code 2024 Puzzle 8

# Import necessary libraries

from collections import defaultdict

# Open the file and read all lines into a list
f = open ("AoC_2024_Puzzle9Data.txt", "r")
data = f.readlines()
f.close()

data[0] = data[0].strip("\n")

# Define sub-functions
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
total = 0

for i in range(len(data[0])):
    a.append(int(data[0][i]))

print(a)

for i in range(int(len(a)/2) + 1):
#    print(i, a[2*i], a[2 * i + 1])
    for j in range(a[2 * i]):
        b.append(i)
    if (2 * i + 1) <= len(a) - 1:
        for j in range(a[2 * i + 1]):
            b.append(".")

print(b)

last_char_point = len(b) - 1

for i in range(len(b)):
    while b[last_char_point] == ".":
        last_char_point -= 1
    
    if b[i] == "." and i < last_char_point:
        b[i] = b[last_char_point]
        b[last_char_point] = "."
        last_char_point -= 1

#print("condensed matrix")
print(b)


for i in range(len(b)):
    if b[i] != ".":
        total += i * int(b[i])

print("The checksum is = ", total)


