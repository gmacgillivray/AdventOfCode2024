# Advent of Code 2024 Puzzle 3

# Import necessary libraries
import re

# Open the file and read all lines into a list
f = open ("AoC_2024_Puzzle4Data.txt", "r")

data = f.readlines()

# Define variables and initialize
a = []
b = []
c = []
d = []
sum = 0
string1 = "XMAS"
string2 = "SAMX"

for line in data:
    a.append(line.strip("\n"))

print(a)

def transpose_list(list_to_transpose):

    return_array = []

    for j in (range(len(list_to_transpose[0]))):
        transpose_string = ""    
        for i in (range(len(list_to_transpose))):
            transpose_string += (list_to_transpose[i][j])
        return_array.append(transpose_string)

    return return_array

def diagonalize_list_LR(list_to_transpose):
    
    return_array = []

    for i in (range(len(list_to_transpose))):
        transpose_string = ""    
        if i < len(list_to_transpose):
            k = 0
            for j in (range(len(list_to_transpose[0]) - i - 1, len(list_to_transpose[0]))):
                transpose_string += (list_to_transpose[k][j])
                k += 1
            return_array.append(transpose_string)

    for i in (range(1, len(list_to_transpose))):
        transpose_string = ""
        k = i
        for j in (range(len(list_to_transpose[0]))):
            if k < len(list_to_transpose):
                transpose_string += (list_to_transpose[k][j])
                k += 1
        
        return_array.append(transpose_string)        
    
    return return_array

def diagonalize_list_RL(list_to_transpose):
    return_array = []
   
    for i in range(len(list_to_transpose)):
        transpose_string = ""
        k = i
        for j in range(i + 1):
            transpose_string += list_to_transpose[k][j]
            k -= 1
        return_array.append(transpose_string)
    
    for i in range(1, len(list_to_transpose[0])):
        transpose_string = ""
        k = len(list_to_transpose) - 1
        for j in range(i, len(list_to_transpose[0])):
            transpose_string += list_to_transpose[k][j]
            k -= 1
        return_array.append(transpose_string)
    
    return return_array

b = transpose_list(a)
c = diagonalize_list_LR(a)
d = diagonalize_list_RL(a)

for line in a:
    sum += line.count(string1) + line.count(string2)

for line in b:
    sum += line.count(string1) + line.count(string2)

for line in c:
    sum += line.count(string1) + line.count(string2) 

for line in d:
    sum += line.count(string1) + line.count(string2) 

f.close()

# Print the results
print("The sum of all instances of XMAS", sum)
