# Advent of Code 2023 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle2Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

colourlist = ['red', 'green', 'blue']
PowerSum = 0

for line in data:
    min_cube = [-1, -1, -1]
    Game_Num, Cubes = line.split(":")
    Game_Name, Game_ID = Game_Num.strip().split(" ")
    Cube_List = Cubes.split(";")
    for Sub_Game in Cube_List:
        Cubes_Game = Sub_Game.strip().split(",")
        for Blocks in Cubes_Game:
            a, colour = Blocks.strip().split(" ")
            a = int(a)
            for i in range(len(colourlist)):
                if colour == colourlist[i] and min_cube[i] == -1:
                    min_cube[i] = a
                if colour == colourlist[i] and a > min_cube[i]:
                    min_cube[i] = a
    PowerSum += min_cube[0] * min_cube[1] * min_cube[2]

f.close()
print("The sum of the calibration values is", PowerSum)


