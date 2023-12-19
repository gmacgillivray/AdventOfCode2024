# Advent of Code 2023 Puzzle 10a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle10Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

# Close file
f.close()

for r in range(len(data)):
    line = data[r]
    for c in range(len(line)):
        if line[c] == 'S':
            start_row = r
            start_col = c

Symbols = ['|', '-', 'L', 'J', '7', 'F', '.']
Next_Col = [0,2,1,-1,-1,1,0]
Next_Row = [2,0,-1,-1,1,1,0]
Next_Step_One = [0, 0]
Next_Step_Two = [0, 0]

line = data[start_row]
checkstep = line[start_col - 1]
checksymbol = Symbols.index(checkstep)
Col_Value = Next_Col[checksymbol]
if Col_Value == 2 or Col_Value == 1:
    Next_Step_One = [0,-1]

line = data[start_row]
checkstep = line[start_col + 1]
checksymmbol = Symbols.index(checkstep)
Col_Value = Next_Col[checksymbol]
if Col_Value == 2 or Col_Value == -1:
    if Next_Step_One == [0, 0]:
        Next_Step_One = [0, 1]
    if Next_Step_One != [0, 0]:
        Next_Step_Two = [0, 1]

line = data[start_row - 1]
checkstep = line[start_col]
checksymbol = Symbols.index(checkstep)
Row_Value = Next_Row[checksymbol]
if Row_Value == 2 or Row_Value == 1:
    if Next_Step_One == [0, 0]:
        Next_Step_One = [-1, 0]
    if Next_Step_One != [0, 0]:
        Next_Step_Two = [-1, 0]

line = data[start_row + 1]
checkstep = line[start_col]
checksymbol = Symbols.index(checkstep)
Row_Value = Next_Row[checksymbol]
if Row_Value == 2 or Row_Value == -1:
    if Next_Step_One == [0, 0]:
        Next_Step_One = [1, 0]
    if Next_Step_One != [0, 0]:
        Next_Step_Two = [1, 0]

#print(Next_Step_One)
#print(Next_Step_Two)


def nextstep(previous, current):
    return_pos = []
    rowcurrent = current[0]
    colcurrent = current[1]
    line = data[rowcurrent]
    checkstep = line[colcurrent]
    checksymbol = Symbols.index(checkstep)
    Row_Value = Next_Row[checksymbol]
    Col_Value = Next_Col[checksymbol]
    if Row_Value == 2:
        if rowcurrent + 1 == previous[0]:
            nextrow = rowcurrent - 1
        if rowcurrent - 1 == previous[0]:
            nextrow = rowcurrent + 1
        nextcol = colcurrent
    if Col_Value == 2:
        if colcurrent + 1 == previous[1]:
            nextcol = colcurrent - 1
        if colcurrent - 1 == previous[1]:
            nextcol = colcurrent + 1
        nextrow = rowcurrent
    if Row_Value == -1 or Row_Value == 1:
        if rowcurrent + Row_Value != previous[0]:
            nextrow = rowcurrent + Row_Value
            nextcol = colcurrent
    if Col_Value == 1 or Col_Value == -1:
        if colcurrent + Col_Value != previous[1]:
            nextcol = colcurrent + Col_Value
            nextrow = rowcurrent
    return_pos.append(nextrow)
    return_pos.append(nextcol)
    return return_pos

Max_Distance_One = 0
Max_Distance_Two = 0
Previous_Coordinates = []
Current_Coordinates = []
Next_Coordinates = [0,0]
Origin = []

Previous_Coordinates.append(start_row)
Previous_Coordinates.append(start_col)

Origin = Previous_Coordinates
history_of_row_pos = []
history_of_col_pos = []
history_of_row_pos.append(Origin[0])
history_of_col_pos.append(Origin[1])

Current_Coordinates.append(start_row + Next_Step_One[0])
Current_Coordinates.append(start_col + Next_Step_One[1])

Steps_Taken = 1

while Next_Coordinates != Origin:
    Steps_Taken += 1
    history_of_row_pos.append(Current_Coordinates[0])
    history_of_col_pos.append(Current_Coordinates[1])
    Next_Coordinates = nextstep(Previous_Coordinates, Current_Coordinates)
    Previous_Coordinates = Current_Coordinates
    Current_Coordinates = Next_Coordinates

min_row = min(history_of_row_pos)
max_row = max(history_of_row_pos)
min_col = min(history_of_col_pos)
max_col = max(history_of_col_pos)

area_one = 0
for i in range(0, len(history_of_row_pos) - 2, 2):
    area_one += history_of_row_pos[i+1] * (history_of_col_pos[i+2] - history_of_col_pos[i]) + history_of_col_pos[i+1] * (history_of_row_pos[i] - history_of_row_pos[i+2])

area_one = abs(area_one/2)
points = []

for r in range(len(history_of_row_pos)):
    points.append((history_of_row_pos[r], history_of_col_pos[r]))

# e.g. corners = [(2.0, 1.0), (4.0, 5.0), (7.0, 8.0)]
def Area(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

area_two = Area(points)

print(min_row, max_row, min_col, max_col)
print("The total number of steps to complete the loop = ", Steps_Taken)
print("The max distance from the starting position is = ", int(Steps_Taken/2))
print("The number of tiles enclosed by the loop is = ", area_one-int(Steps_Taken/2))
print("The number of tiles enclosed by the loop is = ", area_two-int(Steps_Taken/2))

new_map = []
new_points = []
length_line = len(data[0])

for r in range(len(points)-1):
    new_points.append((points[r][0]*2,points[r][1]*2))
    if r != len(points):
        new_points.append((points[r][0] + points[r+1][0], points[r][1] + points[r+1][1]))

for r in range(len(data)*2):
    line_fill = ""
    for l in range(length_line):
        check = []
        check.append((r, l))
        if check[0] in points:
            line_fill += "*"
        else:
            line_fill += "."
    new_map.append(line_fill)

for r in range(len(new_map)):
    print(new_map[r])