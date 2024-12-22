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

def recursive_rock_expansion(rocks, blinks):
    
    rock_expansion = defaultdict(list)

# Define variables and initialize
a = []
b = []
c = []
rock_expansion = defaultdict(list)

for line in data:
    a.append(line.strip("\n").split(" "))

for i in range(len(a[0])):
    b.append(int(a[0][i]))

#for key, value in rock_expansion.items():
#    print(f"{key}: {value}")

num_of_blinks = 75 
sub_loops = 3

for i in range(1000):
    rock_expansion[i] = []
    rock_expansion[i].extend(rock_expansion_function(i, int(num_of_blinks/sub_loops)))
    print(i)

print("check")

for j in range(sub_loops):
    
    c = []
    print(j)
    
    for i in range(len(b)):
        temp_rocks = []
        
        if b[i] not in rock_expansion:
            rock_expansion[b[i]] = []
            temp_rocks = rock_expansion_function(b[i], int(num_of_blinks/sub_loops))
            for j in range(len(temp_rocks)):
                c.append(temp_rocks[j])
            rock_expansion[b[i]].extend(temp_rocks)
        else:
            c.extend(rock_expansion[b[i]])

    b = c
    
#print(c)

#for key, value in rock_expansion.items():
#    print(f"{key}: {value}")
   
#Print the results
print("The total number of stones is =", len(b))

