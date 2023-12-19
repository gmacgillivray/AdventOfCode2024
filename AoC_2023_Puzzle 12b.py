# Advent of Code 2023 Puzzle 12a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle12Data.txt", "r")

# Read in all the lines of the file into a list of lines
temp_data = f.readlines()
data = []
instructions = []
instructions_double = []
instructions_full = []

# Close file
f.close()

for r in range(len(temp_data)):
    a, b = temp_data[r].strip().split(" ")
    a_string = ""
    b_string = ""
    a_string_double = ""
    b_string_double = ""
    a_string_full = ""
    b_string_full = ""

#   a_string_double = a + "?"
    b_string_double = b + ','

    for i in range(4):
#        a_string_full += a
#        a_string_full += "?"
        b_string_full += b
        b_string_full += ","

#    a_string_double += a
    b_string_double += b

#    a_string_full += a
    b_string_full += b
    
    data.append(a)
    instructions.append(b)
    instructions_double.append(b_string_double)
    instructions_full.append(b_string_full)

#for r in range(len(data)):
#   print(data[r], instructions[r], instructions_double[r], instructions_full[r])
#   print(instructions[r], instructions_double[r], instructions_full[r])

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

def evaluate_line(line_to_check, s_symbols, instruction_to_check):
    does_pattern_match = 0
    count_question_marks = 0
    count_symbols = 0
    c_ref = []
    zero_ref = []
    one_ref = []

    for c in range(len(line_to_check)):
        check = line_to_check[c]
        if check == "?":
            c_ref.append(c)
            count_question_marks += 1
        if check == "#":
            count_symbols += 1
            one_ref.append(c)
        if check == ".":
            zero_ref.append(c)

    diff_symbols = s_symbols - count_symbols
    f_l_check = False

    for p in range(2 ** len(c_ref)):
        insert_string = bin(p)[2:].zfill(len(c_ref))
        insert_string_one_check = 0
        for d in range(len(insert_string)):
            if insert_string[d] == "1":
                insert_string_one_check += 1
        testline = ""
        if insert_string_one_check == diff_symbols:
            for q in range(len(line_to_check)):
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
            if test_pattern == instruction_to_check:
                does_pattern_match += 1
                if (testline[0] == "#" and testline[(len(testline)-1)] == "#"):
                    f_l_check = True

    return does_pattern_match, f_l_check

running_matches_start = []
running_matches = []
running_matches_end = []
running_matches_double = []
running_first_last = []
working_instruction_list = []
running_matches_full = []

sum_matches_part_one = 0
sum_matches_part_two = 0

for r in range(len(data)):

    print("Row = ", r)
    line = data[r]
    line_start = '?' + line
    line_end = line + '?'
    line_double = line + '?' + line

    working_instruction = []
    working_instruction_double = []
    working_instruction_full = []

    working_instruction = instructions[r].strip().split(",")
    working_instruction_double = instructions_double[r].strip().split(",")
    working_instruction_full = instructions_full[r].strip().split(",")
    
    for n in range(len(working_instruction)):
        working_instruction[n] = int(working_instruction[n])
    
    for n in range(len(working_instruction_double)):
        working_instruction_double[n] = int(working_instruction_double[n])

    for n in range(len(working_instruction_full)):
        working_instruction_full[n] = int(working_instruction_full[n])

    sum_symbols = sum(working_instruction)
    sum_symbols_double = sum(working_instruction_double)
    sum_symbols_full = sum(working_instruction_full)

    matches, first_last = evaluate_line(line, sum_symbols, working_instruction)

    running_matches_start.append(evaluate_line(line_start, sum_symbols, working_instruction)[0])
    running_matches.append(matches)
    running_matches_end.append(evaluate_line(line_end, sum_symbols, working_instruction)[0])
    running_first_last.append(first_last)
    working_instruction_list.append(working_instruction)
    running_matches_double.append(evaluate_line(line_double, sum_symbols_double, working_instruction_double)[0])

    sum_matches_part_one += running_matches[r] 

    option_one = (running_matches_start[r] ** 4) * running_matches[r]
    option_two = (running_matches_end[r] ** 4) * running_matches[r]

    if (running_matches[r] == 1 and running_first_last[r]):
        sum_matches_part_two += running_matches[r]
        option_print = running_matches[r]
        running_matches_full.append(0)
    else:
        if (running_matches_double[r] > (running_matches_start[r] * running_matches[r])) and (running_matches_double[r] > (running_matches_end[r] * running_matches[r])):
            line_full = line + '?' + line + '?' + line + '?' + line + '?' + line
            running_matches_full.append(evaluate_line(line_full, sum_symbols_full, working_instruction_full)[0])
            sum_matches_part_two += running_matches_full[r]
        else:
            if (option_one > option_two):
                sum_matches_part_two += option_one
                option_print = option_one
                running_matches_full.append(0)
            else:
                sum_matches_part_two += option_two
                option_print = option_two
                running_matches_full.append(0)


#    if (line[0] == "?" and line[1] == "?"):
#        print(line, working_instruction_list[r], running_matches[r], option_print, running_first_last[r])

#    if (line[len(line)-1] == "?" and line[len(line)-2] == "?"):
#        print(line, working_instruction_list[r], running_matches[r], option_print, running_first_last[r])


print("The sum of all the counts for part one is", sum_matches_part_one)
print("The sum of all the counts for part two is", sum_matches_part_two)