# Advent of Code 2023 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle5Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
seedlist = data[0].strip("seeds:").strip().split(" ")

seed_to_soil_start = data.index("seed-to-soil map:\n")
soil_to_fertilizer_start = data.index("soil-to-fertilizer map:\n")
fertilizer_to_water_start = data.index("fertilizer-to-water map:\n")
water_to_light_start = data.index("water-to-light map:\n")
light_to_temperature_start = data.index("light-to-temperature map:\n")
temperature_to_humidity_start = data.index("temperature-to-humidity map:\n")
humidity_to_location_start = data.index("humidity-to-location map:\n")

def convert(index_start, index_end, data_list, start_ref):
    working_list = data_list[index_start:index_end]
    match = False
    for line in working_list:
        a, b, c = line.strip().split(" ")
        if start_ref >= int(b) and start_ref < (int(b) + int(c)):
            return_ref = start_ref - int(b) + int(a)
            match = True
    if not(match):
        return_ref = start_ref
    return return_ref

def reverse_convert(index_start, index_end, data_list, end_ref):
    working_list = data_list[index_start:index_end]
    match = False
    for line in working_list:
        a, b, c = line.strip().split(" ")
        if end_ref >= int(a) and end_ref < (int(a) + int(c)):
            start_ref = end_ref - int(a) + int(b)
            match = True
    if not(match):
        start_ref = end_ref
    return start_ref

Setmin = True

test_location = int(77435349/2)
low_range_location = 0
high_range_location = 77435349

minlocation = 77435349
seedminlocation = 0

#while low_range_location != high_range_location:

while ((high_range_location - low_range_location) >= 2):
#for test_location in range(77435350, 77435346, -1):    
    humidity = reverse_convert(humidity_to_location_start+1, len(data), data, test_location)
    temperature = reverse_convert(temperature_to_humidity_start+1, humidity_to_location_start-1, data, humidity)
    light = reverse_convert(light_to_temperature_start+1, temperature_to_humidity_start-1, data, temperature)
    water = reverse_convert(water_to_light_start+1, light_to_temperature_start-1, data, light)        
    fertilizer = reverse_convert(fertilizer_to_water_start+1, water_to_light_start-1, data, water)
    soil = reverse_convert(soil_to_fertilizer_start+1, fertilizer_to_water_start-1, data, fertilizer)       
    seed = reverse_convert(seed_to_soil_start+1, soil_to_fertilizer_start-1, data, soil)
    
    Match = False

    for r in range(0,len(seedlist),2):
        seedstart = int(seedlist[r])
        seedend = seedstart + int(seedlist[r+1])
        if seed > int(seedstart):
            if seed < int(seedend):
                Match = True
                minlocation = test_location 
                seedminlocation = seed
                seedstartlocation = seedstart
                seedendlocation = seedend
                print(test_location, seed, seedstart, seedend)

    print(test_location, minlocation)      
    if Match:
        high_range_location = test_location
        minlocation = test_location
        print(minlocation)
    else:
        low_range_location = test_location

    test_location = int((high_range_location - low_range_location)/2 + low_range_location)
#    print(minlocation, low_range_location, high_range_location, test_location)

f.close()

print("The minimum location of the seeds is = ", minlocation, seedminlocation, seedstartlocation, seedendlocation)


