# Advent of Code 2023 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle3Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

symbols = "*#+$&=-@/,%"
Part_Number_Sum = 0

for l in range(len(data)):
# Scan line for numbers
    for c in range(len(data[l])):
        Part_Number = -1
        if c == 0 and data[l][c].isdigit(): #First digit check for first character in the line
            Part_Num_Start = c
        if c > 0: # First digit check for every other character in the line
            if data[l][c].isdigit() and not(data[l][c-1].isdigit()):
                Part_Num_Start = c
        if data[l][c].isdigit() and c > 0 and c < (len(data[l])-1): #End digit check excluding last character in line
            if not(data[l][c+1].isdigit()):
                Part_Num_End = c + 1
                Part_Number = data[l][Part_Num_Start:Part_Num_End]
                Part_Number = int(Part_Number)
        if data[l][c].isdigit() and c == (len(data[l])-1): #End digit check if c is on the last character       
                Part_Num_End = c + 1
                Part_Number = data[l][Part_Num_Start:Part_Num_End]
                Part_Number = int(Part_Number)
        if Part_Number != -1: # Execute when a number is found
            check = -1
# Initial ranges to scan to find if there symbols around
            Range_Start = Part_Num_Start - 1
            Range_End = Part_Num_End + 1
            Start_line = l-1
            End_line = l+2
# Adjust range variables for the start/end characters or start/end lines
            if c == 0:
                Range_Start = Part_Num_Start
            if c == (len(data[l]) - 1):
                Range_End = Part_Num_End
            if l == 0:
                Start_line = l
            if l == (len(data)-1):
                End_line = l+1
            for r in range(Start_line, End_line):
                for s in range(Range_Start,Range_End):
                    s = int(s)
                    if symbols.find(data[r][s]) != -1:
                        check = 1
                        print(Part_Number)
                        print(data[r][s])
            if check == 1:
                Part_Number_Sum += Part_Number

f.close()
print("The sum of the calibration values is", Part_Number_Sum)


