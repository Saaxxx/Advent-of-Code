# f = open("testinput.txt", "r")
f = open("input.txt", "r")
lines = [list(x) for x in f.read().split("\n")]
letters = ["X","M","A","S"]

width = len(lines[0])
height = len(lines)

def findNext(depth, x, y, x_dir, y_dir):
    if (x < 0 or y < 0 or x >= width or y >= height or depth >= len(letters) or lines[y][x] != letters[depth]):
        return False
    
    if (depth == 3):
        return True

    
    return findNext(depth+1, x+x_dir, y+y_dir, x_dir, y_dir)

res = 0
for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if (lines[y][x] == "X"):
            for y_dir in range(-1,2):
                for x_dir in range(-1,2):
                    if(findNext(1, x+x_dir, y+y_dir, x_dir, y_dir)):
                        res += 1
print(res)

def findCross(x, y):
    if (lines[y-1][x-1] == "M" and lines[y+1][x+1] == "S" or lines[y-1][x-1] == "S" and lines[y+1][x+1] == "M") \
        and (lines[y+1][x-1] == "M" and lines[y-1][x+1] == "S" or lines[y+1][x-1] == "S" and lines[y-1][x+1] == "M"):
        return True
    return False
                    
res = 0         
for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if (lines[y][x] == "A"):
            if (x-1 >= 0 and x+1 < width and y-1 >= 0 and y+1 < height and findCross(x, y)):
                # print(x+1,y+1)
                res += 1

print(res)