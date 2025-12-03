def expand_rows(data):
    
    new = []
    
    for i,x in enumerate(data):
        if "#" not in x:
            new.append(x.copy())
        new.append(x)
            
    return new

def expand_cols(data):
    
    counter = 0
    new = data
    cols = []
    for i in range(len(data[0])):
        for j in range(len(data)):
            if data[j][i] == "#":
                break
        else:
            cols.append(i)
    
    for i,row in enumerate(new):
        for j,col in enumerate(cols):
            new[i].insert(j+col, ".")
            
    return new

def find_hashes(data):
    locations = []
    for i,x in enumerate(data):
        for j,y in enumerate(x):
            if y == "#":
                locations.append([i,j])
    
    return locations

def find_empty_rows(data):
    
    rows = []
    
    for i,x in enumerate(data):
        if "#" not in x:
            rows.append(i)
    
    return rows

def find_empty_cols(data):
    cols = []
    for i in range(len(data[0])):
        for j in range(len(data)):
            if data[j][i] == "#":
                break
        else:
            cols.append(i)
    return cols

f = open("p11input.txt", "r").read().strip()

data = [[y for y in x] for x in f.split("\n")]

data = expand_rows(data)
data = expand_cols(data)

locations = find_hashes(data)

# print(locations)
# for x in data:
#     print(*x, sep = "")

counter = 0
for i,x in enumerate(locations):
    for y in locations[i+1:]:
        counter += abs(y[0] - x[0]) + abs(y[1] - x[1])

print(counter)

data = [[y for y in x] for x in f.split("\n")]

rows = find_empty_rows(data)
cols = find_empty_cols(data)

row_sizes = [1]*len(data)
col_sizes = [1]*len(data[0])

multiplier = 1000000
counter = 0

for r in rows:
    row_sizes[r] = multiplier
for c in cols:
    col_sizes[c] = multiplier
    
c = 0
for i,r in enumerate(row_sizes):
    c += r
    row_sizes[i] = c
    
c = 0
for i,r in enumerate(col_sizes):
    c += r
    col_sizes[i] = c
    
# print(row_sizes, col_sizes)

# locations = find_hashes(data)
# for i,x in enumerate(locations):
#     for j,y in enumerate(locations[i+1:]):
#         add = 0
#         for r in rows:
#             if r in range(min(y[0], x[0]), max(y[0], x[0])+1):
#                 add += multiplier-1
                
#         for c in cols:
#             if c in range(min(y[1], x[1]), max(y[1], x[1])+1):
#                 add += multiplier-1
            
#         counter += abs(y[0]-x[0]) + abs(y[1] - x[1]) + add

locations = find_hashes(data)
for i,x in enumerate(locations):
    for j,y in enumerate(locations[i+1:]):
            
        counter += abs(row_sizes[y[0]]-row_sizes[x[0]]) + abs(col_sizes[y[1]] - col_sizes[x[1]])
        
        

print(counter)