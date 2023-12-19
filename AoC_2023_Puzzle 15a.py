# Advent of Code 2023 Puzzle 14b

# Open text file with all of the data
f = open ("AoC_2023_Puzzle14Data_Test.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

# Close file
f.close()

working_data = []
loaded_data = []
sum = 0

def transpose_list(list_to_transpose):

    return_array = []

    for j in (range(len(list_to_transpose[0]))):
        transpose_string = ""    
        for i in (range(len(list_to_transpose))):
            transpose_string += (list_to_transpose[i][j])
        return_array.append(transpose_string)

    return return_array

for i in range(len(data)):
    data[i] = data[i].strip()

def resort_grid(data_to_resort):
    num_O = 0
    num_space = 0
    sorted_data = []

    for i in (range(len(data_to_resort))):
        temp_string = ""    
        for j in (range(len(data_to_resort[0]))):
            if data_to_resort[i][j] == "O":
                num_O += 1
            if data_to_resort[i][j] == ".":
                num_space += 1
            if data_to_resort[i][j] == "#":
                for k in range(num_O):
                    temp_string += "O"
                for k in range(num_space):
                    temp_string += "."
                temp_string += "#"
                num_O = 0
                num_space = 0
            if j == (len(data_to_resort[0])-1):
                for k in range(num_O):
                    temp_string += "O"
                for k in range(num_space):
                    temp_string += "."
                num_O = 0
                num_space = 0
        sorted_data.append(temp_string)
    return sorted_data

for i in range(1000000000):
    working_data = transpose_list(data)
    loaded_data = resort_grid(working_data)
    data = loaded_data

for i in range(len(loaded_data)):
    line = loaded_data[i]
    line_sum = 0
    for j in range(len(line)):
        if line[j] == "O":
            sum += len(line) - j
            line_sum += len(line) - j
#    print(loaded_data[i], line_sum)


print("The total loading on the baseline is", sum)

