# Advent of Code 2024 Puzzle 10

# Import necessary libraries
from collections import defaultdict

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle12Data_test.txt", "r") as f:
    data = f.readlines()

# Define subfunctions
def fence_perimeter(plot_points):

    perim = 4 * len(plot_points)
    
    for i in range(len(plot_points)):
        for j in range(i+1, len(plot_points)):
            if [plot_points[i][0] + 1, plot_points[i][1]] == plot_points[j]:
                perim -= 2
            if [plot_points[i][0] - 1, plot_points[i][1]] == plot_points[j]:
                perim -= 2    
            if [plot_points[i][0], plot_points[i][1] + 1] == plot_points[j]:
                perim -= 2    
            if [plot_points[i][0], plot_points[i][1] - 1] == plot_points[j]:
                perim -= 2   
    
    return perim

def refine_plots(plot_points):
    
    all_temp_plot_points = defaultdict(list)
#    all_temp_plot_points = []
    
    for i in range(len(plot_points)):
        label = (plot_points[i][0],plot_points[i][1])
        all_temp_plot_points[label] = []
        all_temp_plot_points[label].append(plot_points[i])
        
        for j in range(len(plot_points)):
            if [plot_points[i][0] + 1, plot_points[i][1]] == plot_points[j] or [plot_points[i][0] - 1, plot_points[i][1]] == plot_points[j] or [plot_points[i][0], plot_points[i][1] + 1] == plot_points[j] or [plot_points[i][0], plot_points[i][1] - 1] == plot_points[j]:
                if plot_points[j] not in all_temp_plot_points[label]:
                    all_temp_plot_points[label].append(plot_points[j])   
    

    
    while still_plot_points == True:
        
        temp_plot_points = []
        temp_plot_points.append(plot)
        
        for point in plot_points: 
            
            if point not in temp_plot_points:
                temp_plot_points.append(point)
                plot_points.remove(point)
            
            for j in range(len(plot_points)):
                if [plot_points[i][0] + 1, plot_points[i][1]] == plot_points[j] or [plot_points[i][0] - 1, plot_points[i][1]] == plot_points[j] or [plot_points[i][0], plot_points[i][1] + 1] == plot_points[j] or [plot_points[i][0], plot_points[i][1] - 1] == plot_points[j]:
                    if plot_points[j] not in temp_plot_points:
                        temp_plot_points.append(plot_points[j])   
    
        for j in temp_plot_points:
            plot_points.remove(j)

        if not plot_points:
            still_plot_points = False 

        all_temp_plot_points.append(temp_plot_points)

        k += 1
    
    return (temp_plot_points, k)


# Define variables and initialize
a = []
garden_plots = defaultdict(list)
reachable = 0

for line in data:
    a.append(line.strip("\n"))

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] not in garden_plots:
            garden_plots[data[i][j]] = []
        garden_plots[a[i][j]].append([i,j])
        
for key, value in garden_plots.items():
    return_array = []
    return_array, num_return = refine_plots(value.copy())
    if num_return > 1:
        for a in range(len(return_array)):
            label = key + str(a)
            if a == 0:
                garden_plots[key] = return_array[a]
            else:
                garden_plots[label] = return_array[a]
                
# Print the results
#print("The total trailhead score is =", reachable)

value = []

fencing_price = 0

for key, value in garden_plots.items():
    print(f"{key}: {value}")
    area = len(value)
    perimeter = fence_perimeter(value)
    print(key, area, perimeter)
    fencing_price += area * perimeter

print("The total fencing price is =", fencing_price)