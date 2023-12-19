# Advent of Code 2023 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle4Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
Winning_Ticket_Count = []
Winning_Ticket_BonusTickets = []
Winning_Ticket_Sum = 0
Winning_Ticket_Sum_Part1 = 0
Winning_Ticket_Sum_Part2 = 0

for l in range(len(data)):
        count_winning_numbers = 0
        Card, Numbers = data[l].strip().split(":")
        a, b = Numbers.strip().split("|")
        Winning_Numbers = a.strip().split()
        My_Numbers = b.strip().split()
        for win_num in My_Numbers:
            for i, e in enumerate(Winning_Numbers):
                if e == win_num:
                    count_winning_numbers += 1
        Winning_Ticket_Count.append(count_winning_numbers)
        Winning_Ticket_BonusTickets.append(1)

#Calculation of the Number of Tickets for Part 2
for i in range(len(Winning_Ticket_Count)):
    for j in range(Winning_Ticket_BonusTickets[i]):
        for k in range(Winning_Ticket_Count[i]):
            Winning_Ticket_BonusTickets[k+i+1] += 1

#Final Sums for Part 1 and 2
for i in range(len(Winning_Ticket_Count)):
    Winning_Ticket_Sum_Part2 += Winning_Ticket_BonusTickets[i]
    if Winning_Ticket_Count[i] != 0:    
        Winning_Ticket_Sum_Part1 += (2 ** (Winning_Ticket_Count[i] - 1))

f.close()

print("The sum of the winning tickets for part 1 is = ", Winning_Ticket_Sum_Part1)
print("The sum of the winning tickets for part 2 is = ", Winning_Ticket_Sum_Part2)


