# Advent of Code 2024 Puzzle 13

# Import necessary libraries
from collections import defaultdict
import heapq



# define sub functions

def combo_operand(reg, operand):
    
# Combo operands 0 through 3 represent literal values 0 through 3.
# Combo operand 4 represents the value of register A.
# Combo operand 5 represents the value of register B.
# Combo operand 6 represents the value of register C.
# Combo operand 7 is reserved and will not appear in valid programs.
    
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return reg["A"]
    elif operand == 5:
        return reg["B"]
    elif operand == 6:
        return reg["C"]
    else:
        return

def adv(reg, operand):
   
# The adv instruction (opcode 0) performs division. The numerator is the value in the A register. 
# The denominator is found by raising 2 to the power of the instruction's combo operand. 
# (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) 
# The result of the division operation is truncated to an integer and then written to the A register.
    
    reg["A"] = int(reg["A"]/(2 ** combo_operand(reg, operand)))
    
    return reg

def bxl(reg, operand):
   
# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's 
# literal operand, then stores the result in register B.

    reg["B"] = reg["B"] ^ operand
    
    return reg

def bst(reg, operand):
   
# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping
# only its lowest 3 bits), then writes that value to the B register.

    reg["B"] = combo_operand(reg, operand) % 8
    
    return reg
   

def bxc(reg, operand):
   
# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result
# in register B. (For legacy reasons, this instruction reads an operand but ignores it.)    
    
    reg["B"] = reg["B"] ^ reg["C"]
    
    return reg

def out(reg, operand, output):
   
# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. 
# (If a program outputs multiple values, they are separated by commas.)
    
    output.append(combo_operand(reg, operand) % 8)
    
    return output

def bdv(reg, operand):
   
# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the 
# B register. (The numerator is still read from the A register.)

    reg["B"] = int(reg["A"]/(2 ** combo_operand(reg, operand)))
    
    return reg

def cdv(reg, operand):
   
# The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. 
# (The numerator is still read from the A register.)

    reg["C"] = int(reg["A"]/(2 ** combo_operand(reg, operand)))
    
    return reg

def execute_instructions(registers, output, instructions, ins_pointer):
    
    operand = instructions[ins_pointer + 1]

    if instructions[ins_pointer] == 0:
        registers = adv(registers, operand)
    elif instructions[ins_pointer] == 1:
        registers = bxl(registers, operand)
    elif instructions[ins_pointer] == 2:
        registers = bst(registers, operand)    
    elif instructions[ins_pointer] == 3:
        if registers["A"] != 0:
            ins_pointer = operand - 2
    elif instructions[ins_pointer] == 4:
        registers = bxc(registers, operand)
    elif instructions[ins_pointer] == 5:
        output = out(registers, operand, output)
    elif instructions[ins_pointer] == 6:
        registers = bdv(registers, operand)
    elif instructions[ins_pointer] == 7:
        registers = cdv(registers, operand)
    
    return registers, output, ins_pointer

def run_program(registers, instructions):
    
    output = []
    ins_pointer = 0
    
    while ins_pointer < len(instructions):
        
        registers, output, ins_pointer = execute_instructions(registers, output, instructions, ins_pointer)
        ins_pointer += 2  
    
    return registers, output 

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle17Data.txt", "r") as f:
    data = f.readlines()

instructions = []
registers = {}
output = []
commands = []
op_codes = []
operands = []

for line in data:
    if line != "\n":
        str_one, str_two = (line.strip("\n").split(":"))      
        if str_one == "Register A":
            registers["A"] = int(str_two)
        elif str_one == "Register B":
            registers["B"] = int(str_two)
        elif str_one == "Register C":
            registers["C"] = int(str_two)
        elif str_one == "Program":
            commands = str_two.strip(" ").split(",")

input_string = ""

for i in range(len(commands)):
    instructions.append(int(commands[i]))
    if i == 0:
        input_string = commands[i]
    else:
        input_string += "," + commands[i]
        
reverse_input_string = ""

for i in range(len(commands) - 1, - 1, -1):
    reverse_input_string += commands[i]

int_input_string = int(reverse_input_string)
        
#k = 147999999999999
#k = 7999999999999
k = 10000000000000
orig_B = registers["B"]
orig_C = registers["C"]
reg_A_values = []
reg_A_values.append([0])
final_values = []

for i in range(len(instructions)):
    
    temp_A_reg = []
    temp_final = []
    
    for j in range(len(reg_A_values[i])):
        
        for remainder in range(8):
            
            ins_pointer = 0
            registers["A"] = reg_A_values[i][j] + remainder
            registers["B"] = orig_B
            registers["C"] = orig_C
            output = []

            registers, output = run_program(registers, instructions)
            
            if output != []:
#                temp_value = instructions[len(instructions) - 1 - i]
#                temp_value2 = int(output[0])
#                if temp_value == temp_value2:
                if instructions[len(instructions) - 1 - i] == output[0]:
                    temp_A_reg.append(8 * (reg_A_values[i][j] + remainder))
                    temp_final.append(reg_A_values[i][j] + remainder)
            
    reg_A_values.append(temp_A_reg)  
    final_values.append(temp_final)  

output_string = ""

for x in range(len(final_values)):

    for i in range(len(final_values[x])):
        registers["A"] = final_values[x][i]
        print(x, i, final_values[x][i])
        registers, output = run_program(registers,instructions)
        print(output)
        print(instructions[len(instructions) - len(output): len(instructions)])
        print(instructions)
        
for i in range(len(output)):
    if i == 0:
        output_string = str(output[i])
    else:
        output_string += "," + str(output[i])

print("The input pattern is  =", input_string)
print("The output pattern is =", output_string)
print("Register A = ", registers["A"])
print("Register B = ", registers["B"])
print("Register C = ", registers["C"])
print("The minimum value that generates the input pattern is =", min(final_values[15]))


