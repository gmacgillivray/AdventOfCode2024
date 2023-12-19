# Advent of Code 2022 Puzzle 1a

# Open text file with all of the data
f = open ("Puzzle1Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

elf = 0
elf1 = 0
elf2 = 0
elf3 = 0

for i in data:
        if (i=="\n"):
            if elf > elf3 and elf < elf2:
                elf3 = elf
            if elf > elf2 and elf < elf1:
                elf3 = elf2
                elf2 = elf
            if elf > elf1:
                   elf3 = elf2
                   elf2 = elf1
                   elf1 = elf
            elf = 0
            continue
        elf += int(i)

f.close()
print("Elf1", elf1, "Elf2", elf2, "Elf3", elf3)
print("Total Calories of Top 3", elf1 + elf2 + elf3)