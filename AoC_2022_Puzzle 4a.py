# Advent of Code 2022 Puzzle 4a

# Open text file with all of the data
f = open ("Puzzle4Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

sum0 = 0
sum1 = 0
sum2 = 0

for line in data:
        elf1, elf2 = line.strip().split(",")
        a, b = elf1.split("-")
        c, d = elf2.split("-")
        if int(a) >= int(c) and int(b) <= int(d):
            sum0 += 1
 #           print(a, b, c, d)          
        if int(c) >= int(a) and int(d) <= int(b):
            sum1 += 1 
 #           print(a, b, c, d)
        if int(a) == int(c) and int(b) == int(d):
            sum2 -= 1
#            print(a, b, c, d)
sum = sum0 + sum1 + sum2

f.close()
print("Total Number of Redundant Searches", sum0, sum1, sum2, sum)
