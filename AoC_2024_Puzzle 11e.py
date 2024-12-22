# Advent of Code 2024 Puzzle 11

from collections import defaultdict

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle11Data_test.txt", "r") as f:
    data = f.readlines()

# Define subfunctions
def rock_expansion_function(rock_num, num_iters):
    d = [rock_num]

    def expand(d, num_iters):
        if num_iters == 0:
            return d

        new_d = []
        for num in d:
            if num == 0:
                new_d.append(1)
            else:
                working_string = str(num)
                if len(working_string) % 2 != 0:
                    new_d.append(num * 2024)
                else:
                    half_digits = int(len(working_string) / 2)
                    string_one = working_string[:half_digits]
                    string_two = working_string[half_digits:]
                    new_d.append(int(string_one))
                    new_d.append(int(string_two))
        return expand(new_d, num_iters - 1)

    return expand(d, num_iters)

def recursive_rock_expansion(b, num_of_blinks, rock_compression):
    if num_of_blinks == 0:
        return b

    new_b = []
    # Create a temp dictionary to store previous rock compression values and zero new compression values
    temp_rocks_dict = defaultdict(list)
    temp_rocks_dict = rock_compression.copy()
        
    for num in b:
        if num not in rock_compression:
            rock_compression[num] = 1
            expanded_rocks = rock_expansion_function(num, 1)
            for rock_num in expanded_rocks:
                if rock_num not in rock_compression:
                    rock_compression[rock_num] = 1
                    new_b.append(rock_num)
                else:
                    rock_compression[rock_num] += rock_compression[num]
                    if rock_num not in new_b:
                        new_b.append(rock_num)
        else:
            new_b.extend(rock_expansion_function(num, 1))

    for rock_num in rock_compression.keys():
        if rock_num not in new_b:
            rock_compression[rock_num] = 0
        elif rock_num in temp_rocks_dict:
            rock_compression[rock_num] -= temp_rocks_dict[rock_num]
    
    return recursive_rock_expansion(new_b, num_of_blinks - 1, rock_compression)

# Define variables and initialize
a = []
b = []
rock_compression = defaultdict(int)

for line in data:
    a.append(line.strip("\n").split(" "))

for i in range(len(a[0])):
    b.append(int(a[0][i]))

num_of_blinks = 6

# Call the recursive function
b = recursive_rock_expansion(b, num_of_blinks, rock_compression)

# Calculate the total number of stones
total = sum(rock_compression.values())

print(b)

for key, value in rock_compression.items():
    print(f"{key}: {value}")

# Print the results
print("The total number of stones is =", total)
