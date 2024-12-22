# Advent of Code 2024 Puzzle 8

# Import necessary libraries

from collections import defaultdict

# Open the file and read all lines into a list
f = open ("AoC_2024_Puzzle8Data.txt", "r")
data = f.readlines()
f.close()

# Define variables and initialize
a = []
b = []
c = []
d = []
total = 0
dish_locations = defaultdict(dict)
anti_resonance_points = []

def replace_char_at_index(s, index, new_char):
    # Convert the string to a list of characters
    char_list = list(s)
    
    # Replace the character at the specified index
    char_list[index] = new_char
    
    # Convert the list back to a string
    return ''.join(char_list)

for line in data:
    a.append(line.strip("\n"))
    
for i in range(len(a)):
    for j in range(len(a[i])):
        label = a[i][j]
        point_location = [i, j]
        
        if label != ".":
            if label not in dish_locations:
                dish_locations[label] = []
            
            dish_locations[label].append(point_location)
        
for key in dish_locations:
    points_list = dish_locations[key]
    for i in range(len(points_list)-1):
        for j in range(i+1, len(points_list)):
            delta_x = points_list[j][0] - points_list[i][0] 
            delta_y = points_list[j][1] - points_list[i][1] 
            
            anti_resonance = [points_list[i][0] - delta_x, points_list[i][1] - delta_y]
            
            if anti_resonance[0] >= 0 and anti_resonance[0] < len(a[0]) and anti_resonance[1] >= 0 and anti_resonance[1] < len(a):
                if [anti_resonance[0], anti_resonance[1]] not in anti_resonance_points:
                    total += 1
                    anti_resonance_points.append([anti_resonance[0], anti_resonance[1]])
                    
            anti_resonance = [points_list[j][0] + delta_x, points_list[j][1] + delta_y]                
            
            if anti_resonance[0] >= 0 and anti_resonance[0] < len(a[0]) and anti_resonance[1] >= 0 and anti_resonance[1] < len(a):
                if [anti_resonance[0], anti_resonance[1]] not in anti_resonance_points:
                    total += 1
                    anti_resonance_points.append([anti_resonance[0], anti_resonance[1]])
            
print("The number of unique anti_node locations is = ", total)

#print(anti_resonance_points)

#anti_node_symbol = "#"

#for i in range(len(anti_resonance_points)):
#    x = anti_resonance_points[i][0]
#    y = anti_resonance_points[i][1] 
#    a[x] = replace_char_at_index(a[x], y, anti_node_symbol)

#print(a)