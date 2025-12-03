def find_pattern(line):
    
    if line.count(0) == len(line):
        return 0
    
    pattern = [y-x for x,y in zip(line[0:len(line)-1], line[1:])]
    
    return line[-1] + find_pattern(pattern)

f = open("p9input.txt", "r").read().strip()

total = 0
for line in f.split("\n"):
    total += find_pattern(list(map(int, line.split())))

print(total)

total = 0
for line in f.split("\n"):
    total += find_pattern(list(map(int, line.split()))[::-1])
print(total)