# Advent of Code 2024 Puzzle 3

# Import necessary libraries
import re

# Open text file with all of the data
f = open ("AoC_2024_Puzzle3Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

# Define variables and initialize
a = []
b = []
pattern = r"mul\((\d+),\s*(\d+)\)"
sum = 0

for line in data:
    a += re.findall(pattern, line)

for line in a:
    num1, num2 = int(line[0]), int(line[1])
    sum += num1 * num2

f.close()

print("The sum of all multiplications is", sum)
