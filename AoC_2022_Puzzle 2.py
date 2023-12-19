# Advent of Code 2022 Puzzle 2

# Open text file with all of the data
f = open ("Puzzle2Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
Points = 0 

print(data)

for i in data:
    if (i=="A X\n"): Points+=4
    if (i=="A Y\n"): Points+=8
    if (i=="A Z\n"): Points+=3
    if (i=="B X\n"): Points+=1
    if (i=="B Y\n"): Points+=5
    if (i=="B Z\n"): Points+=9
    if (i=="C X\n"): Points+=7
    if (i=="C Y\n"): Points+=2
    if (i=="C Z\n"): Points+=6

f.close()

print("Point Total = ", Points)