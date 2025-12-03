f = open("p4input.txt", "r")

data = f.read().strip()

lines = data.split("\n")
games = [n.split(":") for n in lines]
wins_and_cards = [n[1].split("|") for n in games]
winning_scores = [n[0].split() for n in wins_and_cards]
cards = [n[1].split() for n in wins_and_cards]

total = 0
matches_per_game = [0]*len(cards)
# print(matches_per_game)

for i in range(len(cards)):
    matches = -1
    for j in cards[i]:
        if j in winning_scores[i]:
            matches += 1
    if matches > -1:
        matches_per_game[i] = matches+1
        total += 2**matches

print(total)
# print(matches_per_game)

total_cards = [1]*len(cards)
for i in range(len(cards)):
    # total_cards[i+1:i+matches_per_game[i]] *= 2
    for j in range(matches_per_game[i]):
        total_cards[i+j+1] += total_cards[i]

print(sum(total_cards))
