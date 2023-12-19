# Advent of Code 2023 Puzzle 1a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle6Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
Times = data[0].strip("Time:").strip().split("   ")
Distances = data[1].strip("Distance:").strip().split("  ")

for i in range(len(Times)):
    Times[i] = Times[i].strip(" ")

for i in range(len(Distances)):
    Distances[i] = Distances[i].strip(" ")

Time = Times[0]
Distance = Distances[0]

for i in range(1,len(Times)):
    Time += Times[i]
    Distance += Distances[i]

Time = int(Time)
Distance = int(Distance)
min_speed = int(Distance/Time)
max_speed = Time
Record_Break = 0
first_button_time = 0
last_button_time = 0

j = min_speed
d = 0 

while d <= Distance:
    j += 1000
    d = (Time - j) * j

j -= 2000
d = 0 
while d <= Distance:
    j += 1
    d = (Time - j) * j

Min_Button_Time = j

j = max_speed
d = 0 
while d <= Distance:
    j -= 1000
    d = (Time - j) * j

j += 2000
d = 0 
while d<= Distance:
    j -= 1
    d = (Time - j) * j

Max_Button_Time = j

#print("Button Time=", j, "Distance =", Distance, "Record_Break =", Record_Break, "First_Button_Time =", first_button_time, "Last_Button_Time =", last_button_time)

print(Min_Button_Time, Max_Button_Time)
Record_Break = Max_Button_Time - Min_Button_Time + 1

f.close()

print("The Total Number of Record Breaks is = ", Record_Break)


