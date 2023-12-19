# Advent of Code 2023 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle1Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

calibration = 0
numtext = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for line in data:
    line = line.strip()
    index_low = len(line)+1
    index_high = -1
    value = 0
    a = 0
    b = 0
    for test_case in numtext:
        value += 1
        if value == 10:
            value = 1
        test_index_low = line.find(test_case)
        test_index_high = line.rfind(test_case)
        if test_index_low != -1 and test_index_low < index_low:
            index_low = test_index_low
            a = value
        if test_index_high != -1 and test_index_high > index_high:
            index_high = test_index_high
            b = value
    calibration += a*10 + b

f.close()
print("The sum of the calibration values is", calibration)


