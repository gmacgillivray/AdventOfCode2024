# Advent of Code 2023 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle5Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
minlocation = 0

seedlist = data[0].strip("seeds:").strip().split(" ")
#seedlist = (3205462428, 3205462429, 3205462430)

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

Setmin = True

for seed in seedlist:
    seed = int(seed)
    soil = convert(seed_to_soil_start+1, soil_to_fertilizer_start-1, data, seed)
    fertilizer = convert(soil_to_fertilizer_start+1, fertilizer_to_water_start-1, data, soil)
    water = convert(fertilizer_to_water_start+1, water_to_light_start-1, data, fertilizer)
    light = convert(water_to_light_start+1, light_to_temperature_start-1, data, water)
    temperature = convert(light_to_temperature_start+1, temperature_to_humidity_start-1, data, light)
    humidity = convert(temperature_to_humidity_start+1, humidity_to_location_start-1, data, temperature)
    location = convert(humidity_to_location_start+1, len(data), data, humidity)
    print(seed, soil, fertilizer, water, light, temperature, humidity, location)
    if Setmin:
        minlocation = location
        Setmin = False
    if location < minlocation:
        minlocation = location
#        print(seed, soil, fertilizer, water, light, temperature, humidity, location)

f.close()

print("The minimum location of the seeds is = ", minlocation)


