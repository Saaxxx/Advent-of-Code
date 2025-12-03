# PT1

inputFile = "input.txt"

f = open(inputFile)

counter = 0
for line in f:
    largest_single = 0
    largest = 0
    for char in line.strip():
        largest = max(largest, int(str(largest_single) + char))
        largest_single = max(largest_single, int(char))
    
    counter += largest
print(counter)


# PT2
f = open(inputFile)

counter = 0
for line in f:    
    vals = []
    for char in line.strip()[:-13:-1]:
        vals.insert(0, int(char))
    
    
    for char in line.strip()[-13::-1]:
            last = int(char)
            for i in range(len(vals)):
                if last < vals[i]:
                    break
                
                last, vals[i] = vals[i], last
    
    print(vals)
    counter += int("".join(list(map(str, vals))))
print(counter)