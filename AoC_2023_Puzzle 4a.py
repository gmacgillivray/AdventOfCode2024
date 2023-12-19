# Advent of Code 2023 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle4Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
Winning_Ticket_Sum = 0

for line in data:
        count_winning_numbers = 0
        Card, Numbers = line.strip().split(":")
        a, b = Numbers.strip().split("|")
        Winning_Numbers = a.strip().split()
        My_Numbers = b.strip().split()
        for win_num in My_Numbers:
            for i, e in enumerate(Winning_Numbers):
                if e == win_num:
                    count_winning_numbers += 1
        if count_winning_numbers > 0:
            Winning_Ticket_Sum += (2 ** (count_winning_numbers - 1))
            print(count_winning_numbers, Winning_Ticket_Sum)
            
f.close()

print("The sum of the calibration values is", Winning_Ticket_Sum)


