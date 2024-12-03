# Advent of Code 2024 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2024_Puzzle1Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
a = []
b = []
sum = 0

for line in data:
    temp_a, temp_b = line.split("   ") 
    a.append(int(temp_a))
    b.append(int(temp_b))

a.sort()
b.sort()

for i in range(len(a)):
    sum += abs(a[i] - b[i])

f.close()

print("The total difference between the lists is", sum)
