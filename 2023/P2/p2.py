import re

def possible_games(data):
    total = 0
    lines = data.split("\n")
    # games = [re.findall(r'(?<=Game )\w+', line) for line in lines]
    # greens = [re.findall(r'(?<=green)', line) for line in lines]
    # reds = [re.findall(r'(?<=red)', line) for line in lines]
    # blues = [re.findall(r'(?<=blue)', line) for line in lines]
    # print(games)

    for line in lines:
        possible = 1
        games = line.split(":")
        tests = games[1].split(";")
        for test in tests:
            prep_test = test.strip().replace(",", "").split()
            # print(prep_test)
            for dice in prep_test:
                if "red" in dice:
                    if int(prep_test[prep_test.index("red")-1]) > 12:
                        possible = 0
                elif "blue" in dice:
                    if int(prep_test[prep_test.index("blue")-1]) > 14:
                        possible = 0
                elif "green" in dice:
                    if int(prep_test[prep_test.index("green")-1]) > 13:
                        possible = 0
        if possible:
            total += int(games[0].split()[1])

    print(total)

def power_of_games(data):
    total = 0
    lines = data.split("\n")

    for line in lines:
        games = line.split(":")
        tests = games[1].split(";")
        reds = 0
        greens = 0
        blues = 0
        for test in tests:
            prep_test = test.strip().replace(",", "").split()
            # print(prep_test)
            for dice in prep_test:
                if "red" in dice:
                    if int(prep_test[prep_test.index("red")-1]) > reds:
                        reds = int(prep_test[prep_test.index("red")-1])
                elif "blue" in dice:
                    if int(prep_test[prep_test.index("blue")-1]) > blues:
                        blues = int(prep_test[prep_test.index("blue")-1])
                elif "green" in dice:
                    if int(prep_test[prep_test.index("green")-1]) > greens:
                        greens = int(prep_test[prep_test.index("green")-1])

        total += greens*blues*reds

    print(total)

f = open("p2input.txt", "r")
data = f.read().strip()

possible_games(data)
power_of_games(data)
