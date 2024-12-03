# Advent of Code 2024 Puzzle 2a

# Open text file with all of the data
f = open ("AoC_2024_Puzzle2Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
a = []
b = []
safe_lines = 0
min_increase_decrease = 0
max_increase_decrease = 4

for line in data:
    a.append([int(s) for s in line.split(" ")])

for line in a:
    c = []
    for j in range(len(line) - 1):
        c.append(line[j+1] - line[j])
    b.append(c)

   
for i in range(len(b)):
    safe = True
    if max(b[i]) * min(b[i]) <= 0:
        safe = False
        print(i, "Increasing and Decreasing")
    for j in range(len(b[i])):
        if abs(b[i][j]) <= min_increase_decrease or abs(b[i][j]) >= max_increase_decrease and safe:
            safe = False
            print("Line ", i, " ", max(b[i]), " ", min(b[i]), b[i], " ", " is not safe")     
    if safe:
        safe_lines += 1
        print("Line ", i, " ", max(b[i]), " ", min(b[i]), b[i], " ", " is safe")      

f.close()

print("The total number of safe lines is", safe_lines)
