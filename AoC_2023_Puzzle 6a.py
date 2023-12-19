# Advent of Code 2023 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle6Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
Times = data[0].strip("Time:").strip().split("   ")
Distance = data[1].strip("Distance:").strip().split("  ")

for i in range(len(Times)):
    Times[i] = int(Times[i])
    Distance[i] = int(Distance[i])

Record_Break = []

for i in range(len(Times)):
    Record_Break.append(0)
    for j in range(Times[i]):
        d = (Times[i] - j) * j
        if d > Distance[i]:
            Record_Break[i] += 1

Total_Record_Breaks = 1

for i in range(len(Record_Break)):
    Total_Record_Breaks = Total_Record_Breaks * Record_Break[i]

f.close()

print("The Total Number of Record Breaks is = ", Total_Record_Breaks)


