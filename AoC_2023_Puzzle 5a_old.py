# Advent of Code 2023 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle5Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
Winning_Ticket_Count = []
seed_to_soil_index = []

seed_to_soil_start = data.index("seed-to-soil map:\n")
soil_to_fertilizer_start = data.index("soil-to-fertilizer map:\n")
fertilizer_to_water_start = data.index("fertilizer-to-water map:\n")
water_to_light_start = data.index("water-to-light map:\n")
light_to_temperature_start = data.index("light-to-temperature map:\n")
temperature_to_humidity_start = data.index("temperature-to-humidity map:\n")
humidity_to_location_start = data.index("humidity-to-location map:\n")

def populate_conversion_index(index_start, index_end, data_list):
    working_list = data_list[index_start:index_end]
    conversion_list = []
    maxa = 0
    for line in working_list:
        a, b, c = line.strip().split(" ")
        if int(a) + int(c) > maxa:
            maxa = int(a) + int(c)
    print(maxa)
    for i in range(maxa):
        conversion_list.append(i)
    for line in working_list:
        a, b, c = line.strip().split(" ")
        for i in range(int(c)):
            conversion_list[int(a)+i] = int(b)+i
    return conversion_list

c = populate_conversion_index(seed_to_soil_start+1, soil_to_fertilizer_start-1, data)
print(seed_to_soil)
f.close()

#print("The sum of the winning tickets for part 1 is = ", Winning_Ticket_Sum_Part1)
#print("The sum of the winning tickets for part 2 is = ", Winning_Ticket_Sum_Part2)


