# Advent of Code 2023 Puzzle 9a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle9Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

# Close file
f.close()

next_set = []
sumend = 0 
sumstart = 0

for l in range(len(data)):
    starting_set = data[l].strip().split(" ")
    for i in range(len(starting_set)):
        starting_set[i] = int(starting_set[i])
    working_set = starting_set
    SetReduced = False
    Num_Reductions = 0
    last_value = []
    first_value = []
    while not(SetReduced):
        last_value.append(working_set[len(working_set)-1])
        first_value.append(working_set[0])
        for i in range(len(working_set) - 1):
            next_set.append(working_set[i+1] - working_set[i])
        working_set = next_set
        if all([v == 0 for v in next_set]):
            SetReduced = True
        next_set = []
    
    for x in last_value:
        sumend += x
    
    s = 1
    temp_first_num = first_value[len(first_value)-1]

    for y in range(len(first_value)-2, -1, -1):
        calc_num = first_value[y]
        temp_first_num = calc_num - temp_first_num

    print(temp_first_num, starting_set[0], starting_set[1])  
    sumstart += temp_first_num

#    print(sumstart - sumin)

print("The total sum of the extrapolated values for part 1 is = ", sumend)
print("The total sum of the extrapolated values for part 2 is = ", sumstart)


