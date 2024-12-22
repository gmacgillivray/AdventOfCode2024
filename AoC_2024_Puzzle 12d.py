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

def trace_perimeter(pos, next_step, plot_points):

    path_points = []
    path_nextsteps = []
    possible_steps = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    left_check = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    right_check = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    turn_around = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    tracing_perimeter = True

    path_points.append([pos[0], pos[1]])
    path_nextsteps.append([next_step[0], next_step[1]])

    pos = [pos[0] + next_step[0], pos[1] + next_step[1]]

#    Get next point    
 
    while tracing_perimeter:   
        
        path_points_temp = []
        path_nextsteps_temp = []
        
        # check to see if there is an area to the left of the position, if there is turn left
        if [pos[0] + left_check[possible_steps.index(next_step)][0], pos[1] + left_check[possible_steps.index(next_step)][1]] in plot_points:
            next_step = [left_check[possible_steps.index(next_step)][0], left_check[possible_steps.index(next_step)][1]]
            
            #save point and next step vector (position doesn't change only vector)
            path_points_temp.append([pos[0], pos[1]])
            path_nextsteps_temp.append([next_step[0], next_step[1]]) 
        
        # check to see if the area in front is a valid position, if so step forward
        elif [pos[0] + next_step[0], pos[1] + next_step[1]] in plot_points:
            
            #save point and next step vector (position and vector do not change)
            path_points_temp.append([pos[0], pos[1]])
            path_nextsteps_temp.append([next_step[0], next_step[1]])      

        # check to see if the area to the right is a valid position, if so step right
        elif [pos[0] + right_check[possible_steps.index(next_step)][0], pos[1] + right_check[possible_steps.index(next_step)][1]] in plot_points:
            
            #save point and next step vector for no position in front for perimeter calculations, this is a pivot step.
            path_points_temp.append([pos[0], pos[1]])
            path_nextsteps_temp.append([next_step[0], next_step[1]])
            
            next_step = [right_check[possible_steps.index(next_step)][0], right_check[possible_steps.index(next_step)][1]]
            path_points_temp.append([pos[0], pos[1]])
            path_nextsteps_temp.append([next_step[0], next_step[1]])
        
        # otherwise turn around or go 180 degrees
        else:
            
            #save point and next step vector for no position in front for perimeter calculations, this is a pivot step.
            path_points_temp.append([pos[0], pos[1]])
            path_nextsteps_temp.append([next_step[0], next_step[1]])
            
            #save point and next step vector for no position on right for perimeter calculations, this is a pivot step.
            
            next_step_temp = [right_check[possible_steps.index(next_step)][0], right_check[possible_steps.index(next_step)][1]]
            path_points_temp.append([pos[0], pos[1]])
            path_nextsteps_temp.append([next_step_temp[0], next_step_temp[1]])
            
            #save point and next step vector for turn around coordindates, this is a pivot step.
            next_step = [turn_around[possible_steps.index(next_step)][0], turn_around[possible_steps.index(next_step)][1]] 
            path_points_temp.append([pos[0], pos[1]])
            path_nextsteps_temp.append([next_step[0], next_step[1]])      
        
        for i in range(len(path_points_temp)):
            pos = [path_points_temp[i][0], path_points_temp[i][1]]
            next_step = [path_nextsteps_temp[i][0], path_nextsteps_temp[i][1]]                            
            pos_indices = [index for index, value in enumerate(path_points) if value == pos]
            next_step_indices = [index for index, value in enumerate(path_nextsteps) if value == next_step]
        
            for i in range(len(pos_indices)):
                if pos_indices[i] in next_step_indices:
#                    path_points.append([pos[0], pos[1]])
#                    path_nextsteps.append([next_step[0], next_step[1]])
                    tracing_perimeter = False

            if tracing_perimeter:
                path_points.append([pos[0], pos[1]])
                path_nextsteps.append([next_step[0], next_step[1]])
        
        pos = [pos[0] + next_step[0], pos[1] + next_step[1]]
    
    return (path_points, path_nextsteps)

def number_sides(plot_points):

    if len(plot_points) == 1:
        return(4, 4)

    temp_graph_points = defaultdict(list)
    temp_graph_points = plot_point_next_steps(plot_points)
    sides = 0
    sides_b = 0
    perim = 0
    perim_b = 0

    path_points = []
    path_nextsteps = []
    perim_points = []
    possible_steps = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    left_check = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    potential_starting_points = []
    
    for i in range(len(plot_points)):
        label = (plot_points[i][0],plot_points[i][1])
        if len(temp_graph_points[label]) < 4:
            potential_starting_points.append([plot_points[i][0], plot_points[i][1]])

    while potential_starting_points != []:

        path_points = []
        path_nextsteps = []
        perim_points = []

        for i in range(len(potential_starting_points)): #find starting point
            label = (potential_starting_points[i][0],potential_starting_points[i][1])
            if len(temp_graph_points[label]) < 4:
                pos = [potential_starting_points[i][0], potential_starting_points[i][1]]
                break        
             
        for i in range(len(possible_steps)): # find a valid starting direction by checking perimeter on left
            if len(plot_points) == 1:
                next_step = possible_steps[0]      
            elif [pos[0] + left_check[i][0], pos[1] + left_check[i][1]] not in plot_points and [pos[0] + possible_steps[i][0], pos[1] + possible_steps[i][1]] in plot_points:
                next_step = possible_steps[i]
                break
        
        path_points, path_nextsteps = trace_perimeter(pos, next_step, plot_points)    
        
        for val in path_points:
            if val not in perim_points:
                perim_points.append(val) 
                
        perim_points_b = []
        perim_nextsteps_b = []
        
        for i in range(len(path_points)):
            
            if i == 0:
                perim_points_b.append(path_points[i])
                perim_nextsteps_b.append(path_nextsteps[i])   

            elif left_check[possible_steps.index(path_nextsteps[i - 1])] != path_nextsteps[i]:
                perim_points_b.append(path_points[i])
                perim_nextsteps_b.append(path_nextsteps[i])  
        
        for i in range(len(perim_points)):
            label = (perim_points[i][0],perim_points[i][1])
            perim += 4 - len(temp_graph_points[label])        

        perim_b += len(perim_points_b)

        # check for enclosed surfaces
        for i in range(len(perim_points)):
            
        
        for i in range(len(path_nextsteps) - 1):
            if i < len(path_nextsteps) - 1:   
                if path_nextsteps[i] != path_nextsteps[i + 1]:
                    sides += 1
            elif path_nextsteps[i] != path_nextsteps[0]:               
                    sides += 1
                    
        for i in range(len(perim_nextsteps_b)):
            if i < len(perim_nextsteps_b) - 1:        
                if perim_nextsteps_b[i] != perim_nextsteps_b[i + 1]:
                    sides_b += 1
            else:
                if perim_nextsteps_b[i] != perim_nextsteps_b[0]: 
                    sides_b += 1
        
        for i in range(len(path_points)):
            if path_points[i] in potential_starting_points:
                potential_starting_points.remove(path_points[i])
                
    return(perim_b, sides_b)

def plot_point_next_steps(pts):
    
    return_graph_points = defaultdict(list)
  
    for i in range(len(pts)):
        label = (pts[i][0],pts[i][1])
        return_graph_points[label] = []
        
        for j in range(len(pts)):
            if [pts[i][0] + 1, pts[i][1]] == pts[j] or [pts[i][0] - 1, pts[i][1]] == pts[j] or [pts[i][0], pts[i][1] + 1] == pts[j] or [pts[i][0], pts[i][1] - 1] == pts[j]:
                if pts[j] not in return_graph_points[label]:
                    return_graph_points[label].append(pts[j]) 

    return return_graph_points

def refine_plots(plot_points):
    
    all_temp_plot_points = defaultdict(list)
    return_plot_points = []
    all_temp_plot_points = plot_point_next_steps(plot_points)      
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
fencing_pricea_two = 0
fencing_priceb = 0

for key, value in refined_garden_plots.items():
#    print(f"{key}: {value}")
    area = len(value)
    perimeter = fence_perimeter(value)
    perimeter_b, sides = number_sides(value)
    if area * perimeter_b != area * perimeter:
        print(key, area, perimeter, area * perimeter, "Path Algorithm", area, perimeter_b, area * perimeter_b, "Sides Algorithm", area, sides, area * sides)
        for i in range(len(value)):
            print(value[i])
    fencing_price += area * perimeter
    fencing_pricea_two += area * perimeter_b
    fencing_priceb += area * sides

print("The total fencing price is for part a =", fencing_price)
print("The total fencing price is for part a using perimeter path algorirhm =", fencing_pricea_two)
print("The total fencing price is for part b =", fencing_priceb)