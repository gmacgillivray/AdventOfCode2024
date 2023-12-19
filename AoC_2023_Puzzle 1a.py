# Advent of Code 2023 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle1Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

sum = 0
a = 0
b = 0

for line in data:
    line = line.strip()
#    test_str = str(line)
    for c in line:
        if c.isdigit() and a == 0:
            a = int(c)
        if c.isdigit() and a != 0:   
            b = int(c)
    sum += a*10 + b
    a = 0
    b = 0

f.close()
print("The sum of the calibration values is", sum)
