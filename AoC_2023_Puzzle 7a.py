# Advent of Code 2023 Puzzle 7a

# Open text file with all of the data
f = open ("AoC_2023_Puzzle7Data.txt", "r")

# Read in all the lines of the file into a list of lines
data = f.readlines()
Hands = []
Bids = []
Hand_Values = []
Hand_Rank = []
Total_Winnings = 0 

for l in range(len(data)):
    a, b = data[l].strip().split(" ")
    Hands.append(a)
    Bids.append(int(b))

def isfullHouse(hand):
    return sorted(hand.count(card) for card in set(hand)) == [2,3]

def istwopair(hand):
    return sorted(hand.count(card) for card in set(hand)) == [1,2,2]

def hand_value(h):
    Card_Values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    i = 0
    v = 0
    max_matches = 0
    for c in h:
        i += 1
        matches = 0
        for j in range(i, len(h)):
            check = h[j]
            if c == check:
                matches += 1
        if matches > max_matches:
            max_matches = matches
        v += Card_Values.index(c) * (100 ** (5 - i))
    if max_matches > 2:
        max_matches += 2
    if max_matches == 2:
        max_matches += 1
        if isfullHouse(h):
            max_matches += 1
    if max_matches == 1:
        if istwopair(h):
            print("two_pair", h)
            max_matches += 1
    v += (max_matches) * (100 ** 5)
    return v

for line in Hands:
    Hand_Values.append(hand_value(line))

Hand_Rank = [sorted(Hand_Values).index(x) for x in Hand_Values]

for x in range(len(Bids)):
    Total_Winnings += Bids[x] * (Hand_Rank[x] + 1)
    print(Hands[x], Hand_Values[x], Hand_Rank[x], Bids[x])


#print(Hands, Bids, Hand_Values, Hand_Rank)

f.close()

print("The total winnings of all hands is = ", Total_Winnings)


