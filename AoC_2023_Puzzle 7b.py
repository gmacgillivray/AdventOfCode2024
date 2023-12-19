# Advent of Code 2023 Puzzle 7a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle7Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()

# Close file
f.close()

Hands = []
Bids = []
Hand_Values = []
Hand_Rank = []
Total_Winnings = 0 

for l in range(len(data)):
    a, b = data[l].strip().split(" ")
    Hands.append(a)
    Bids.append(int(b))

def isfiveofakind(hand):
    return sorted(hand.count(card) for card in set(hand)) == [5]

def isfourofakind(hand):
    return sorted(hand.count(card) for card in set(hand)) == [1,4]

def isfullhouse(hand):
    return sorted(hand.count(card) for card in set(hand)) == [2,3]

def isthreeofakind(hand):
    return sorted(hand.count(card) for card in set(hand)) == [1,1,3]

def istwopair(hand):
    return sorted(hand.count(card) for card in set(hand)) == [1,2,2]

def isapair(hand):
    return sorted(hand.count(card) for card in set(hand)) == [1,1,1,2]

def isahighcard(hand):
    return sorted(hand.count(card) for card in set(hand)) == [1,1,1,1,1]

def hand_value(h):
#    Card_Values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    Card_Values = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    i = 0
    v = 0
    jokers = 0
    max_matches = 0

    # Calculate hand ranking value based on individual cares
    for c in h:
        i += 1
        v += Card_Values.index(c) * (100 ** (5 - i))
    
    # Count number of jokers
    jokers = h.count("J")

    # Determine type of hand
    if isfiveofakind(h):
        max_matches = 6
    if isfourofakind(h):
        max_matches = 5
        if jokers >= 1:
            max_matches = 6
    if isfullhouse(h):
        max_matches = 4
        if jokers >= 1:
            max_matches = 6
    if isthreeofakind(h):
        max_matches = 3
        if jokers >= 1:
            max_matches = 5
    if istwopair(h):
        max_matches = 2
        if jokers == 1:
            max_matches = 4
        if jokers == 2:
            max_matches = 5
    if isapair(h):
        max_matches = 1
        if jokers >= 1:
            max_matches = 3
    if isahighcard(h):
        max_matches = 0
        if jokers == 1:
            max_matches = 1

    # Calculate score based on hand ranking
    v += (max_matches) * (100 ** 5)
    return v

for line in Hands:
    Hand_Values.append(hand_value(line))

Hand_Rank = [sorted(Hand_Values).index(x) for x in Hand_Values]

for x in range(len(Bids)):
    Total_Winnings += Bids[x] * (Hand_Rank[x] + 1)
    print(Hands[x], Hand_Values[x], Hand_Rank[x], Bids[x])


#print(Hands, Bids, Hand_Values, Hand_Rank)

print("The total winnings of all hands is = ", Total_Winnings)


