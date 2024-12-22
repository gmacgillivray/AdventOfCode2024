# Advent of Code 2024 Puzzle 3

# Import necessary libraries
import re
from collections import defaultdict

# Open the file and read all lines into a list
f = open ("AoC_2024_Puzzle5Data.txt", "r")
data = f.readlines()
f.close()

# Define variables and initialize
a = []
b = []
c = []
d = []
sum = 0
page_order = defaultdict(dict)

for line in data:
    if line != "\n":
        if line[2] == "|":
            a.append(line.strip("\n").split("|"))
        else: 
            b.append(line.strip("\n"))

print(b)

for line in a:
    label = int(line[0])
    page_num = int(line[1])
    
    if label not in page_order:
        page_order[label] = []
    
    page_order[label].append(page_num)

#for key, value in page_order.items():
#    print(f"{key}: {value}")

for i in range(len(b)):
    c = []
    d = []
    c = [int(num) for num in b[i].split(',')]
    
    check = True
    
    for j in range(len(c)):
        if c[j] in page_order:
             for k in range(j):
                if c[k] in page_order[c[j]]:
                    check = False
    
    if check:
        print(c[int(len(c)/2)])
        sum += c[int(len(c)/2)] 

# Print the results
print("The sum of all middle values for correctly ordered updates ", sum)
#print("The sum of all instances of XMAS for part b is", sum2)