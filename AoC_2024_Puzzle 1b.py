# Advent of Code 2024 Puzzle 1a & 1b

# Open text file with all of the data
f = open ("AoC_2024_Puzzle1Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
a = []
b = []
sum_part_a = 0
sum_part_b = 0

for line in data:
    temp_a, temp_b = line.split("   ") 
    a.append(int(temp_a))
    b.append(int(temp_b))

a.sort()
b.sort()

for i in range(len(a)):
    sum_part_a += abs(a[i] - b[i])
    sum_part_b += a[i] * b.count(a[i])

f.close()

print("The total difference between the lists is for part a is", sum_part_a)
print("The similarity score for the lists for part b is", sum_part_b)