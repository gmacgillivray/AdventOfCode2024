# Advent of Code 2023 Puzzle 12a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle12Data.txt", "r")

# Read in all the lines of the file into a list of lines
temp_data = f.readlines()
data = []
instructions = []

# Close file
f.close()

# Add padding data for lines with no stars

for r in range(len(temp_data)):
    a, b = temp_data[r].strip().split(" ")
    data.append(a)
    instructions.append(b)

#for r in range(len(data)):
    #print(data[r]), instructions[r])
    #print(instructions[r])

def check_pattern(linetocheck):
    streak = 0
    symbol_pattern = []
    for c in range(len(linetocheck)):
        if linetocheck[c] == "#":
            streak += 1
        if (linetocheck[c] != "#" and streak >= 1) or (c == (len(linetocheck) - 1) and streak >= 1):
            symbol_pattern.append(streak)
            streak = 0
    return(symbol_pattern)   

running_matches = []

for r in range(len(data)):
    c_ref = []
    zero_ref = []
    one_ref = []
    count_question_marks = 0
    count_symbols = 0
    working_line = ""
    matches = 0

    line = data[r]

    for c in range(len(line)):
        check = line[c]
        if check == "?":
            c_ref.append(c)
            count_question_marks += 1
        if check == "#":
            count_symbols += 1
            one_ref.append(c)
        if check == ".":
            zero_ref.append(c)

    working_instruction = [] 
    working_instruction = instructions[r].strip().split(",")
    for n in range(len(working_instruction)):
        working_instruction[n] = int(working_instruction[n])
    
    sum_symbols = sum(working_instruction)
    diff_symbols = sum_symbols - count_symbols

  
    for p in range(2 ** len(c_ref)):
        insert_string = bin(p)[2:].zfill(len(c_ref))
        testline = ""
        for q in range(len(line)):
            if q in zero_ref:
                testline += "."
            if q in one_ref:
                testline += "#"
            if q in c_ref:
                digit_ref = c_ref.index(q)
                if insert_string[digit_ref] == "0":
                    testline += "."
                if insert_string[digit_ref] == "1":
                    testline += "#" 
        test_pattern = check_pattern(testline)
        if test_pattern == working_instruction:
            matches += 1
    
    running_matches.append(matches)

sum_matches = 0

for r in range(len(data)):
#    print(data[r], instructions[r], running_matches[r])
    sum_matches += running_matches[r]    

print("The sum of all the counts is", sum_matches)