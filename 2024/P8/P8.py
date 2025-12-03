f = open("testinput.txt", "r")
# f = open("testinput2.txt", "r")
f = open("input.txt", "r")
lines = f.read().split("\n")

height = len(lines)
width = len(lines[0])

antennas = {}

antinodes = set()

for y, line in enumerate(lines):
    for x, location in enumerate(line):
        if location == ".":
            continue
        
        antinodes.add((x,y))
        
        if location not in antennas:
            antennas[location] = []
        
        for idenicalAntennas in antennas[location]:
            x_dist = x - idenicalAntennas[0]
            y_dist = y - idenicalAntennas[1]
            
            # pt1
            
            # if x + x_dist >= 0 and x + x_dist < width and y + y_dist >= 0 and y + y_dist < height:
            #     antinodes.add((x + x_dist, y + y_dist))
            
            # if idenicalAntennas[0] - x_dist >= 0 and idenicalAntennas[0] - x_dist < width and idenicalAntennas[1] - y_dist >= 0 and idenicalAntennas[0] - y_dist < height:
            #     antinodes.add((idenicalAntennas[0] - x_dist, idenicalAntennas[1] - y_dist))
                
            # pt2
            temp_x = x
            temp_y = y
            while temp_x + x_dist >= 0 and temp_x + x_dist < width and temp_y + y_dist >= 0 and temp_y + y_dist < height:
                temp_x += x_dist
                temp_y += y_dist
                antinodes.add((temp_x, temp_y))
            
                print(temp_x, temp_y)
            
            temp_x = idenicalAntennas[0]
            temp_y = idenicalAntennas[1]
            while temp_x - x_dist >= 0 and temp_x - x_dist < width and temp_y - y_dist >= 0 and temp_y - y_dist < height:
                temp_x -= x_dist
                temp_y -= y_dist
                antinodes.add((temp_x, temp_y))
                
                print(temp_x, temp_y)
            
        antennas[location].append((x,y))
    

print(antinodes)
print(len(antinodes))

map = [list(x) for x in lines]

for antinode in antinodes:
    map[antinode[1]][antinode[0]] = "#"
    
f = open("output", "w+")
f.write("\n".join(["".join(x) for x in map]))