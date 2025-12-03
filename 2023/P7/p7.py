card_levels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_levels_joker = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def inital_card_greater(first_set, second_set):

    num_same_cards = [0,0]
    pairs = [[],[]]

    for i,card in enumerate(first_set[0]):
        num = first_set[0].count(card)

        if num == 2:
            if len(pairs[0]) == 0:
                pairs[0].append(card)
            elif len(pairs[0]) == 1 and pairs[0][0] != card:
                pairs[0].append(card)

        if num > num_same_cards[0]:
            num_same_cards[0] = num

    for i,card in enumerate(second_set[0]):
        num = second_set[0].count(card)

        if num == 2:
            if len(pairs[1]) == 0:
                pairs[1].append(card)
            elif len(pairs[1]) == 1 and pairs[1][0] != card:
                pairs[1].append(card)

        if num > num_same_cards[1]:
            num_same_cards[1] = num

    scores = [0,0]
    for i,n in enumerate(num_same_cards):
        scores[i] = n
        if (n == 2 and len(pairs[i]) == 2) or (n == 3 and len(pairs[i]) == 1):
            scores[i] += 0.5

    if scores[0] == scores[1]:
        for i,card in enumerate(first_set[0]):
            if card != second_set[0][i]:
                return True if card_levels.index(card) < card_levels.index(second_set[0][i]) else False

    return True if scores[0] > scores[1] else False

def inital_card_greater_jokers(first_set, second_set):

    num_same_cards = [0,0]
    pairs = [[],[]]

    for i,card in enumerate(first_set[0]):

        if card == "J":
            continue

        num = first_set[0].count(card)

        if num == 2:
            if len(pairs[0]) == 0:
                pairs[0].append(card)
            elif len(pairs[0]) == 1 and pairs[0][0] != card:
                pairs[0].append(card)

        if num > num_same_cards[0]:
            num_same_cards[0] = num

    for i,card in enumerate(second_set[0]):
        num = second_set[0].count(card)

        if card == "J":
            continue

        if num == 2:
            if len(pairs[1]) == 0:
                pairs[1].append(card)
            elif len(pairs[1]) == 1 and pairs[1][0] != card:
                pairs[1].append(card)

        if num > num_same_cards[1]:
            num_same_cards[1] = num

    cards = [first_set, second_set]
    scores = [0,0]

    for i,n in enumerate(num_same_cards):
        scores[i] = n
        if (n == 2 and len(pairs[i]) == 2) or (n == 3 and len(pairs[i]) == 1):
            scores[i] += 0.5
        if "J" in cards[i][0]:
            scores[i] += cards[i][0].count("J")
            # print(scores[i])

    if scores[0] == scores[1]:
        for i,card in enumerate(first_set[0]):
            if card != second_set[0][i]:
                return True if card_levels_joker.index(card) < card_levels_joker.index(second_set[0][i]) else False

    return True if scores[0] > scores[1] else False

f = open("p7input.txt", "r").read().strip()

card_scores = [x.split() for x in f.split("\n")]

ordered_cards = []
ordered_cards.append(card_scores[0])

for i in range(1, len(card_scores)):
    for j in range(len(ordered_cards)):
        if inital_card_greater(card_scores[i], ordered_cards[j]):
            ordered_cards.insert(j, card_scores[i])
            break
    else:
        ordered_cards.append(card_scores[i])

total = 0
for i,score in enumerate(ordered_cards):
    total += int(score[1])*(len(ordered_cards)-i)

# print(ordered_cards)
print(total)

ordered_cards = []
ordered_cards.append(card_scores[0])

for i in range(1, len(card_scores)):
    for j in range(len(ordered_cards)):
        if inital_card_greater_jokers(card_scores[i], ordered_cards[j]):
            ordered_cards.insert(j, card_scores[i])
            break
    else:
        ordered_cards.append(card_scores[i])

total = 0

for i,score in enumerate(ordered_cards):
    total += int(score[1])*(len(ordered_cards)-i)
print(total)
