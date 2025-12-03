# PT1
inputFile = "input.txt"

position = 50
count = 0

f = open(inputFile)

for line in f:
    direction = line[0]
    amount = int(line[1:])
    
    # print(direction, int(amount))
    if direction == "L":
        amount *= -1
        
    position = (position + amount) % 100
    if position == 0:
        count += 1
        
print(count)

# PT2
position = 50
count = 0

f = open(inputFile)

for line in f:
    direction = line[0]
    amount = int(line[1:])
    
    # print(direction, int(amount))
    if direction == "L":
        position = (100 - position) % 100
        
    position += amount
    count += position // 100
    # print("moved to", position)
    position %= 100
    
    if direction == "L":
        position = (100 - position) % 100
    # print("final", position)
        
print(count)