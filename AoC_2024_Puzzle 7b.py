# Advent of Code 2024 Puzzle 6

# Import necessary libraries

import re
from collections import defaultdict

# Open the file and read all lines into a list
f = open ("AoC_2024_Puzzle7Data_test.txt", "r")
data = f.readlines()
f.close()

# Define variables and initialize
a = []
b = []
c = []
d = []

calib_total = 0
calib_total2 = 0

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
        
    if match_check:
        c.append(a[i])
        d.append(b[i])

for i in range(len(c)):
    total = 0

    for l in range(len(d[i])-1):
        e = []
        replace_bool = False
        for m in range(len(d[i])-1):
            if replace_bool:
                e.append(d[i][m+1])
            if not replace_bool:
                if l == m:
                    temp_string = str(d[i][m]) + str(d[i][m+1])
                    e.append(int(temp_string))
                    replace_bool = True
                else:
                    e.append(d[i][m])
        
        total = 0
        num_patterns = len(e)
        bin_string = f"0{num_patterns - 1}b"
        match_check = True
            
        for j in range(2**(num_patterns - 1)):
            pattern2 = f'{j:{bin_string}}'
            pattern_string = str(pattern2)
            total = e[0]
            
            if total == c[i]:
                calib_total2 += c[i]
                match_check = False
            
            if match_check and len(pattern_string) > 1:
                for k in range(len(pattern_string)):
                    if pattern_string[k] == "0":
                        total += e[k+1]
                    if pattern_string[k] == "1":
                        total *= e[k+1]
                if total == c[i]:
                    match_check = False
                    calib_total2 += c[i]
                   
print("Sum of calibration totals for part a is = ", calib_total)
print("Sum of calibration totals for part b is =", calib_total + calib_total2)
#print("Map loops count = ", map_loops_count)
