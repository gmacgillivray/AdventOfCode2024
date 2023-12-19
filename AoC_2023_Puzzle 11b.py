# Advent of Code 2023 Puzzle 11a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle11Data.txt", "r")

# Read in all the lines of the file into a list of lines
temp_data = f.readlines()
data = []


# Close file
f.close()

# Add padding data for lines with no stars

expand_factor = 1000000
#expansion_string = ""
#for e in range(expand_factor-1):
#    expansion_string += "."

blank_rows = []

for r in range(len(temp_data)):
    line = temp_data[r].strip()
    data.append(line)
    check = True
    for c in range(len(line)):
        if line[c] != '.':
            check = False
    if check:
        blank_rows.append(r)
 #       for e in range(expand_factor-1):
 #           data.append(line)

#print(blank_rows)

blank_columns = []
line_length = len(data[0])


for c in range(line_length):
    check = True
    for r in range(len(data)):
        line = data[r]
        if line[c] != '.':
            check = False
    if check:
        blank_columns.append(c)

#print(blank_columns)

#for i in (range(len(blank_columns))):
#    column_insert = blank_columns[i] + i
#    for r in range(len(data)):
#        data[r] = data[r][:column_insert] + expansion_string + data[r][column_insert:]

star_coordinates = []

for l in range(len(data)):
    line = data[l]
    for c in range(len(line)):
        if line[c] == "#":
            star_coordinates.append([l, c])

sum_distances = []
sumofalldistances = 0

for i in range(len(star_coordinates)):
    a = star_coordinates[i][0]
    b = star_coordinates[i][1]
    for j in range(i+1, len(star_coordinates)):
        c = star_coordinates[j][0]
        d = star_coordinates[j][1]
        add_rows = 0
        add_columns = 0
        for r in range(len(blank_rows)):
            if (blank_rows[r] > a and blank_rows[r] < c) or (blank_rows[r] > c and blank_rows[r] < a):
                add_rows += 1
        for k in range(len(blank_columns)):
            if (blank_columns[k] > b and blank_columns[k] < d) or (blank_columns[k] > d and blank_columns[k] < b):
                add_columns += 1
        sum_distances.append(abs(c - a) + abs(d - b) + (add_rows + add_columns) * (expand_factor - 1))

for i in range(len(sum_distances)):
    sumofalldistances += int(sum_distances[i])

print("The sum of all the lengths is = ", sumofalldistances)

