# Advent of Code 2024 Puzzle 21

# Import necessary libraries
from collections import defaultdict
import heapq

# define sub functions

def keypad_door(code):
    
    keypad_map = {'7': (0,0), '8': (1,0), '9': (2,0), '4': (0,1), '5': (1,1), '6': (2,1), '1': (0,2), '2': (1,2), '3': (2,2), '0': (1,3), 'A': (2,3)}
    start = (2, 3)
    current = start
    button_pushes = []
    
    for c in code:

        end = keypad_map[c]
        
        steps_x = end[0] - current[0]
        if steps_x < 0:
            button_char = "<"
        else:
            button_char = ">"
        for i in range(abs(steps_x)):
            button_pushes.append(button_char)
        
        steps_y = end[1] - current[1]
        if steps_y < 0:
            button_char = "^"
        else:
            button_char = "v"
        for i in range(abs(steps_y)):
            button_pushes.append(button_char)
        
        button_pushes.append("A")
        
        current = end
    
    return button_pushes

def keypad_robot(code):

    keypad_map = {'^': (1,0), 'A': (2,0), '<': (0,1), 'v': (1,1), '>': (2,1)}
    start = (2, 0)
    current = start
    button_pushes = []

    for c in code:
        
        end = keypad_map[c]
        
        steps_x = end[0] - current[0]
        
        if steps_x < 0:
            button_char = "<"
        else:
            button_char = ">"
        for i in range(abs(steps_x)):
            button_pushes.append(button_char)
        
        steps_y = end[1] - current[1]
        if steps_y < 0:
            button_char = "^"
        else:
            button_char = "v"
        for i in range(abs(steps_y)):
            button_pushes.append(button_char)
        
        button_pushes.append("A")
        
        current = end
    
    return button_pushes

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle21Data.txt", "r") as f:
    data = f.readlines()

path = []
all_codes = []
final_sum = 0

for line in data:
    all_codes.append(line.strip("\n"))

for code in all_codes:

    button_pushes = []

    button_pushes = keypad_door(code)

    string_pattern = ""
    for button in button_pushes:
        string_pattern += button

    print(code, ":", string_pattern)

    for i in range(2):
        button_pushes = keypad_robot(button_pushes)

        string_pattern = ""
        for button in button_pushes:
            string_pattern += button

        print(code, ":", string_pattern)
    
#    print(code,":", string_pattern)

    # Calculate the score
    # first adjust code to an int
    if code[0] == "0":
        code = int(code[1:len(code) - 1])
    else:
        code = int(code[0:len(code) - 1])

    final_sum += code * len(button_pushes)
    print("Code:", code, "Total Steps:", len(button_pushes), "Current Sum:", code * len(button_pushes))
 
print("The sum of the complexities of the five codes on the list is =", final_sum)
