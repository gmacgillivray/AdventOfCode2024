# Advent of Code 2024 Puzzle 11

from collections import defaultdict

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle11Data.txt", "r") as f:
    data = f.readlines()

# Define subfunctions
def rock_expansion_recursive(b, num_of_blinks):
    
    print(num_of_blinks)
    
    if num_of_blinks == 0:
        return b

    new_elements = []
    for j in range(len(b)):
        if b[j] == 0:
            b[j] = 1
        else:
            working_string = str(b[j])
            if len(working_string) % 2 == 0:
                half_digits = int(len(working_string) / 2)
                string_one = working_string[:half_digits]
                string_two = working_string[half_digits:]
                b[j] = int(string_one)
                new_elements.append(int(string_two))
            else:
                b[j] *= 2024

    b.extend(new_elements)
    return rock_expansion_recursive(b, num_of_blinks - 1)

# Define variables and initialize
a = []
b = []

for line in data:
    a.append(line.strip("\n").split(" "))

for i in range(len(a[0])):
    b.append(int(a[0][i]))

num_of_blinks = 75

# Call the recursive function
b = rock_expansion_recursive(b, num_of_blinks)

#print(b)

# Print the results
print("The total number of stones is =", len(b))