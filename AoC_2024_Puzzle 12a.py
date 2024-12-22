# Advent of Code 2024 Puzzle 10

# Import necessary libraries
from collections import defaultdict

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle12Data.txt", "r") as f:
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
    return_plot_points = []
    
    for i in range(len(plot_points)):
        label = (plot_points[i][0],plot_points[i][1])
        all_temp_plot_points[label] = []
#Might not need the line below        
#        all_temp_plot_points[label].append(plot_points[i])
        
        for j in range(len(plot_points)):
            if [plot_points[i][0] + 1, plot_points[i][1]] == plot_points[j] or [plot_points[i][0] - 1, plot_points[i][1]] == plot_points[j] or [plot_points[i][0], plot_points[i][1] + 1] == plot_points[j] or [plot_points[i][0], plot_points[i][1] - 1] == plot_points[j]:
                if plot_points[j] not in all_temp_plot_points[label]:
                    all_temp_plot_points[label].append(plot_points[j])   
       
    m = 0
    
    while plot_points != []:
    
        temp_plot_points = []
        k = 0
        temp_plot_points.append(plot_points[k])
        
        while k < len(temp_plot_points):
                
            label = (temp_plot_points[k][0],temp_plot_points[k][1])
            temp_list_points = []
            temp_list_points = all_temp_plot_points[label]
            
            for point in temp_list_points: 
                
                if point not in temp_plot_points:
                    temp_plot_points.append(point)
            
            k +=1
        
        for j in temp_plot_points:
            plot_points.remove(j)

        return_plot_points.append(temp_plot_points)
        
        m += 1
   
    return (return_plot_points, m)


# Define variables and initialize
a = []
garden_plots = defaultdict(list)
refined_garden_plots = defaultdict(list)
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
                refined_garden_plots[key] = return_array[a]
            else:
                refined_garden_plots[label] = return_array[a]
    else:
        refined_garden_plots[key] = garden_plots[key]
                
# Print the results
#print("The total trailhead score is =", reachable)

value = []

fencing_price = 0

for key, value in refined_garden_plots.items():
#    print(f"{key}: {value}")
    area = len(value)
    perimeter = fence_perimeter(value)
    print(key, area, perimeter, area * perimeter)
    fencing_price += area * perimeter

print("The total fencing price is =", fencing_price)