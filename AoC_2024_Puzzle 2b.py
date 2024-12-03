# Advent of Code 2024 Puzzle 2a

# Open text file with all of the data
f = open ("AoC_2024_Puzzle2Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
a = []
b = []
safe_lines = 0
safe_lines_b = 0
min_increase_decrease = 0
max_increase_decrease = 4

for line in data:
    a.append([int(s) for s in line.split(" ")])

for line in a:
    c = []
    for j in range(len(line) - 1):
        c.append(line[j+1] - line[j])
    b.append(c)

def report_safety_check(list_to_check, min_check, max_check):

    safe = True

    if max(list_to_check) * min(list_to_check) <= 0:
        safe = False

    for j in range(len(list_to_check)):
        if abs(list_to_check[j]) <= min_check or abs(list_to_check[j]) >= max_check and safe:
            safe = False

    return safe
   
for i in range(len(a)):
    if report_safety_check(b[i], min_increase_decrease, max_increase_decrease):
        safe_lines += 1

    safe_lines_b_check = False
    
    for k in range(len(a[i])):
        c = []
        d = []
        for j in range(len(a[i])): 
            if k != j:
                c.append(a[i][j])
                
        for j in range(len(c)-1):
            d.append(c[j+1] - c[j])
        
        print(d)
        if not(safe_lines_b_check):
            if report_safety_check(d, min_increase_decrease, max_increase_decrease):
                safe_lines_b_check = True
                safe_lines_b += 1      

f.close()

print("The total number of safe lines for part a is", safe_lines, "\n")
print("The total number of safe lines for part b is", safe_lines_b, "\n")
