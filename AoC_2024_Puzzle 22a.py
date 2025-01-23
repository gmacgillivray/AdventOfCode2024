# Advent of Code 2024 Puzzle 13

# Import necessary libraries
from collections import defaultdict
import heapq

# define sub functions

def mix(secret, mix_value):

# To mix a value into the secret number, calculate the bitwise XOR of the given value and 
# the secret number. Then, the secret number becomes the result of that operation. 
#(If the secret number is 42 and you were to mix 15 into the secret number, the secret number 
# would become 37.)

    secret = secret ^ mix_value

    return secret

def prune(secret):

# To prune the secret number, calculate the value of the secret number modulo 16777216. 
# Then, the secret number becomes the result of that operation. (If the secret number is 
# 100000000 and you were to prune the secret number, the secret number would become 16113920.)

 secret = secret % 16777216
 
 return secret

def execute_secrete_round(secret):
    # Calculate the result of multiplying the secret number by 64. Then, mix this result 
    # into the secret number. Finally, prune the secret number.
    # Calculate the result of dividing the secret number by 32. Round the result down to the 
    # nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
    # Calculate the result of multiplying the secret number by 2048. Then, mix this result into 
    # the secret number. Finally, prune the secret number.
    
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, int(secret/32)))
    secret = prune(mix(secret, secret * 2048)) 

    return secret

# Open the file and read all lines into a list
with open("AoC_2024_Puzzle22Data.txt", "r") as f:
    data = f.readlines()

secret_values = []

for line in data:
    secret_values.append(int(line))
    
print(secret_values)

num_secret_iterations = 2000

for i in range(num_secret_iterations):
    for j in range(len(secret_values)):
        secret_values[j] = execute_secrete_round(secret_values[j])

sum_secrets = 0   
       
for s in secret_values:
    sum_secrets += s

print(secret_values)

print("The sum of the secret values is = ", sum_secrets)            
    

