# Advent of Code 2023 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle2Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

colourlist = ['red', 'green', 'blue']
maxblocks = [12, 13, 14]
IDsum = 0

for line in data:
    include_game = 1
    Game_Num, Cubes = line.split(":")
    Game_Name, Game_ID = Game_Num.strip().split(" ")
    Cube_List = Cubes.split(";")
    for Sub_Game in Cube_List:
        Cubes_Game = Sub_Game.strip().split(",")
        for Blocks in Cubes_Game:
            a, colour = Blocks.strip().split(" ")
            a = int(a)
            for i in range(len(colourlist)):
 #               print(i)
                if colour == colourlist[i] and a > maxblocks[i]:
                    include_game = 0
    if include_game == 1:
        IDsum += int(Game_ID)


f.close()
print("The sum of the calibration values is", IDsum)


