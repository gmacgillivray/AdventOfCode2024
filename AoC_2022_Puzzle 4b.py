# Advent of Code 2022 Puzzle 4a

# Open text file with all of the data
f = open ("Puzzle4Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

sum0 = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0


for line in data:
        elf1, elf2 = line.strip().split(",")
        a, b = elf1.split("-")
        c, d = elf2.split("-")
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if a >= c and b <= d:
            sum0 += 1
 #           print(a, b, c, d)          
        if c >= a and d <= b:
            sum1 += 1 
 #           print(a, b, c, d)
        if a == c and b == d:
            sum2 -= 1
#            print(a, b, c, d)
        if (a != c and b != d) and a >= c and a <= d and b >= d :
            sum3 += 1
        if (a != c and b != d) and c >= a and c <=b and d >= b:
            sum4 += 1
            print(a, b, c, d)
        if a > d or c > b:
            sum5 += 1

sum6 = len(data)
sum = sum0 + sum1 + sum2 + sum3 + sum4
nonoverlap = sum6 - sum5

f.close()
print("Total Number of Redundant Searches", sum0, sum1, sum2, sum3, sum4, sum, sum5, sum6, nonoverlap)
