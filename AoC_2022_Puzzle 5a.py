# Advent of Code 2022 Puzzle 5a

# Import matrix funcationality
import numpy as np

# Open text file with all of the data
f = open ("Puzzle5Data.txt", "r")

# Read in all the lines of the file into a list of lines
all_data = f.readlines()
Container_Baseline = all_data[0:8]
Move_Data = all_data[10:]


#print(Container_Baseline)
#print(Move_Data)
matrix_rows = len(Container_Baseline)
matrix_cols = 9

for r in range(matrx_rows):
    for c in range(matrix_cols):
        Container_Matrix = np.array(Container_Baseline[r][4*c-2])
for line Container_Baseline:
    Container_Matrix = 


f.close()
#print("Total Number of Redundant Searches", sum0, sum1, sum2, sum3, sum4, sum, sum5, sum6, nonoverlap)

import numpy as np


arr = np.empty((3, 4))

# Value by value
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        arr[i, j] = i + j


# Row by row
for i in range(arr.shape[0]):
    row = range(arr.shape[1])
    arr[i, :] = row


# Column by column
for j in range(arr.shape[1]):
    row = range(arr.shape[0])
    arr[:, j] = row


# Or just all at once
arr = np.array([
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
])

# Or use one of many built-in functions
arr = np.arange(3 * 4).reshape(3, 4)