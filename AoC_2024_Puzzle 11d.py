# Advent of Code 2024 Puzzle 11

# Import necessary libraries
from collections import defaultdict

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle11Data.txt", "r") as f:
    data = f.readlines()

# Define subfunctions

def rock_expansion_function(rock_num, num_iters):
    
    d = []
#    e = []
    
    d.append(rock_num)

    for i in range(num_iters):
        
        j = 0
        
        while j < len(d):
            if d[j] == 0:
                d[j] = 1
                j += 1
            else:
                working_string = str(d[j])
                
                if len(working_string) % 2 != 0:
                    d[j] *= 2024
                    j += 1
                else:
                    half_digits = int(len(working_string) / 2)
                    string_one = working_string[0:half_digits]
                    string_two = working_string[half_digits:2 * half_digits]
                    d[j] = int(string_one)
                    d.insert(j + 1, int(string_two))
                    j += 2
    return d


# Define variables and initialize
a = []
b = []
c = []
rock_compression = defaultdict(list)
total = 0

for line in data:
    a.append(line.strip("\n").split(" "))

for i in range(len(a[0])):
    b.append(int(a[0][i]))

#for key, value in rock_expansion.items():
#    print(f"{key}: {value}")

num_of_blinks = 75 

for i in range(len(b)):
    rock_compression[b[i]] = 1

for j in range(num_of_blinks):
    
    c = []
    print(j)
    
    # Create a temp dictionary to store previous rock compression values and zero new compression values
    temp_rocks_dict = defaultdict(list)
    temp_rocks_dict = rock_compression.copy()
    
    for i in range(len(b)):
        temp_rocks = []
        
        # Create a temp dictionary to store previous rock compression values and zero new compression values
              
        if b[i] not in rock_compression:
            rock_compression[b[i]] = 1
              
        temp_rocks = rock_expansion_function(b[i], 1)
               
        for rock_num in temp_rocks:     
            if rock_num not in rock_compression:
                rock_compression[rock_num] = temp_rocks_dict[b[i]]
                c.append(rock_num)
            else:
                rock_compression[rock_num] += temp_rocks_dict[b[i]]
                if rock_num not in c:
                    c.append(rock_num)      
         
    for rock_num in rock_compression.keys():
        if rock_num not in c:
            rock_compression[rock_num] = 0
        elif rock_num in temp_rocks_dict.keys():
            rock_compression[rock_num] -= temp_rocks_dict[rock_num]
    
#    total = sum(rock_compression.values())
    b = c
    
#print(c)

# Calculate the total number of stones
total = sum(rock_compression.values())

#for key, value in rock_compression.items():
#    print(f"{key}: {value}")
 
#for key, value in rock_expansion.items():
#    total += value
 
#Print the results
print("The total number of stones is =", total)

