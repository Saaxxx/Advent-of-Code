# f = open("testinput.txt", "r")
f = open("input.txt", "r")

# pt1

lines = [list(x) for x in f.read().split("\n")]
path = [x.copy() for x in lines]
visited = set()

height = len(lines)
width = len(lines[0])

# print(lines)

x = 0
y = 0
y_dir = 0
x_dir = 0
found = False

state = 0
states = [[0,1], [1,0], [0,-1], [-1,0]]
dir_states = [">", "v", "<", "^"]

for row, line in enumerate(lines):
    for column, space in enumerate(line):
        match space:
            case "<":
                state = 2
                x_dir = -1
            case ">":
                state = 0
                x_dir = 1
            case "^":
                state = 3
                y_dir = -1
            case "v":
                state = 1
                y_dir = 1
        
        if y_dir + x_dir != 0:
            x = column
            y = row
            break
        
    if y_dir + x_dir != 0:
            break

start_state = state
start_x = x
start_x_dir = x_dir
start_y = y
start_y_dir = y_dir


while (x+x_dir >= 0 and x+x_dir < width and y+y_dir >= 0 and y+y_dir < height):
    
    while lines[y+y_dir][x+x_dir] == "#":
        state = (state+1)%4
        y_dir = states[state][0]
        x_dir = states[state][1]
        
    visited.add((x,y))
    # print(y,x, path)
    path[y][x] = dir_states[state]
    x = x+x_dir
    y = y+y_dir
    # print(x,y)
    
visited.add((x,y))
    
    
print(len(visited)) 

f = open("output", "w+")
f.write("\n".join(["".join(x) for x in path]))

# pt2

def has_cycle(map, x, y, x_dir, y_dir, state):
    thisMapCycle = set()
    while (x+x_dir >= 0 and x+x_dir < width and y+y_dir >= 0 and y+y_dir < height):
    
        while map[y+y_dir][x+x_dir] == "#":
            state = (state+1)%4
            y_dir = states[state][0]
            x_dir = states[state][1]
        
        if (x,y,(x_dir,y_dir)) in thisMapCycle:
            # print(x,y)
            return True
        
        thisMapCycle.add((x,y,(x_dir,y_dir)))
        
        x = x+x_dir
        y = y+y_dir
    
    return False
        
cycles = 0
for loc in visited:
    if loc[1] == start_y and loc[0] == start_x:
        continue
    
    lines[loc[1]][loc[0]] = "#"
    
    if has_cycle(lines, start_x, start_y, start_x_dir, start_y_dir, start_state):
        # print(loc)
        cycles += 1
    
    lines[loc[1]][loc[0]] = "."

print(cycles)
print((7,9) in visited)