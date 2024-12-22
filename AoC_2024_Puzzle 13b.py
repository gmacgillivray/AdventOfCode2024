# Advent of Code 2024 Puzzle 13

# Import necessary libraries
from collections import defaultdict

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle13Data.txt", "r") as f:
    data = f.readlines()

button_A = []
button_B = []
prizes = []
total_total = 0

for line in data:
    if line != "\n":
        str_one, str_two = (line.strip("\n").split(":"))
        str_three, str_four = str_two.split(",")
        if str_one == "Button A":
            x = str_three.strip(" X+")
            y = str_four.strip(" Y+")
            button_A.append([int(x), int(y)])       
        elif str_one == "Button B":
            x = str_three.strip(" X+")
            y = str_four.strip(" Y+")
            button_B.append([int(x), int(y)])  
        
        elif str_one == "Prize":
            x = str_three.strip(" X=")
            y = str_four.strip(" Y=")
            prizes.append([int(x) + 10000000000000, int(y) + 10000000000000])  
        
for i in range(len(button_A)):
    #print(button_A[i], button_B[i], prizes[i])
    
    if button_A[i][0] != 0 and (button_B[i][1] - button_A[i][1] * button_B[i][0] / button_A[i][0]) != 0:
        b = (prizes[i][1] - ((button_A[i][1] * prizes[i][0]) / button_A[i][0])) / (button_B[i][1] - (button_A[i][1] * button_B[i][0] / button_A[i][0]))
        a = (prizes[i][0] - b * button_B[i][0]) / button_A[i][0]
#        print(a, b)
#        if a >= 0 and b >= 0:
        a = round(a)
        b = round(b)
        
        if a * button_A[i][0] + b * button_B[i][0] == prizes[i][0] and a >= 0 and b >= 0:
            token_per_game = 3 * a + b   
        
        else:
            token_per_game = 0
            a = 0
            b = 0
    else:
        token_per_game = 0
        a = 0
        b = 0
    
    total_total += token_per_game
      
#    if a != 0:  
#        print(round(a), round(b), token_per_game)    

print("The total number of tokens to maximize prizes =", total_total)
