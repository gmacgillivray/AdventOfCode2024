# Advent of Code 2024 Puzzle 6

# Import necessary libraries

import re
from collections import defaultdict

# Open the file and read all lines into a list
f = open ("AoC_2024_Puzzle7Data.txt", "r")
data = f.readlines()
f.close()

# Define variables and initialize
a = []
b = []
calib_total = 0

for line in data:
    temp_a = []
    temp_a = line.strip("\n").split(": ")
    a.append(int(temp_a[0]))
    temp_b = temp_a[1].split(" ")
    for i in range(len(temp_b)):
        temp_b[i] = int(temp_b[i])
    b.append(temp_b)
    
#print(a)
#print(b)

for i in range(len(a)):
    
    total = 0
    num_patterns = len(b[i])
    bin_string = f"0{num_patterns - 1}b"
    match_check = True
    
    for j in range(2**(num_patterns - 1)):
        pattern2 = f'{j:{bin_string}}'
        pattern_string = str(pattern2)
        total = b[i][0]
        
        if match_check:
            for k in range(len(pattern_string)):
                if pattern_string[k] == "0":
                    total += b[i][k+1]
                if pattern_string[k] == "1":
                    total *= b[i][k+1]
            if total == a[i]:
                match_check = False
                calib_total += a[i]
            
#            print(i, j, pattern_string, total)
                   
print("Sum of calibration totals = ", calib_total)
#print("Map loops count = ", map_loops_count)
