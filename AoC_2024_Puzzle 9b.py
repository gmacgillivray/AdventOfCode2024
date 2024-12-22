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
ID_blocks = []
Blank_blocks = []

total = 0

for i in range(len(data[0])):
    a.append(int(data[0][i]))

print(a)

for i in range(int(len(a)/2) + 1):
    for j in range(a[2 * i]):
        b.append(i)
    if (2 * i + 1) <= len(a) - 1:
        for j in range(a[2 * i + 1]):
            b.append(".")

print(b)

last_char_point = len(b) - 1

i = len(b) - 1

while i > 0:
    
    reading_a_file = True
    found_a_file = False
    empty_block_length_needed = 0
    
    if b[i] != ".":
        found_a_file = True
        end_of_file = i
        empty_block_length_needed += 1
        while reading_a_file:
            i -= 1
            if b[i+1] == b[i]:
                empty_block_length_needed += 1
            else:
                reading_a_file = False
    else:
        i -=1
                
    
    if found_a_file:
        
        found_a_spot = False
        j = 0
        spot_length = 0
        match_spot = False
        
        while not found_a_spot:    
            spot_length = 0
            
            if b[j] == ".":
                in_a_spot = True
                spot_start = j
                spot_length += 1
                while in_a_spot:
                    j += 1
                    if b[j] == ".":
                        spot_length += 1            
                    else:
                        in_a_spot = False
            else:
                j += 1
                
            if j >= i:
                found_a_spot = True
            
            if empty_block_length_needed <= spot_length:
                found_a_spot = True
                match_spot = True    
        
        if match_spot:
            for k in range(empty_block_length_needed):
                b[spot_start + k] = b[end_of_file - k]
                b[end_of_file - k] = "."

#print("condensed matrix")
print(b)


for i in range(len(b)):
    if b[i] != ".":
        total += i * int(b[i])

print("The checksum is = ", total)


