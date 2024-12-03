# Advent of Code 2024 Puzzle 3

# Import necessary libraries
import re

# Open the file and read all lines into a list
f = open ("AoC_2024_Puzzle3Data.txt", "r")

data = f.readlines()

# Define variables and initialize
a = []
b = []
pattern = r"mul\((\d+),\s*(\d+)\)"
total_sum = 0
total_sum_b = 0

# Combine all lines into a single string and remove newlines
data_one_line = "".join(data).replace('\n', '')
print(data_one_line, "\n")

# Correct the regex pattern to remove text between "don't()" and "do()"
data_clean = re.sub(r"don't\(\).*?do\(\)", "", data_one_line)
print(data_clean)

# Find all matches for the pattern in the original data
for line in data:
    a += re.findall(pattern, line)

# Calculate the sum for part a
for line in a:
    num1, num2 = int(line[0]), int(line[1])
    total_sum += num1 * num2

# Find all matches for the pattern in the cleaned data
b += re.findall(pattern, data_clean)
print(b)

# Calculate the sum for part b
for line in b:
    num1, num2 = int(line[0]), int(line[1])
    total_sum_b += num1 * num2

f.close()

# Print the results
print("The sum of all multiplications for part a is", total_sum)
print("The sum of all multiplications for part b is", total_sum_b)