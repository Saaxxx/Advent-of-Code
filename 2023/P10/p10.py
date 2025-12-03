north = ["|", "7", "F", "S"]
south = ["|", "J", "L", "S"]
east = ["-", "J", "7", "S"]
west = ["-", "L", "F", "S"]

def find_start_char(grid, start_location):
    north_ = False
    south_ = False
    east_ = False
    west_ = False
    
    if start_location[0] != 0 and grid[start_location[0]-1][start_location[1]] in north:
        north_ = True

    if start_location[0] != len(grid)-1 and grid[start_location[0]+1][start_location[1]] in south:
        if north_:
            return "|"
        south_ = True

    if start_location[1] != 0 and grid[start_location[0]][start_location[1]-1] in west:
        if north_:
            return "J"
        if south_:
            return "7"
        west_ = True

    if start_location[1] != len(grid[0])-1 and grid[start_location[0]][start_location[1]+1] in east:
        if north_:
            return "L"
        if south_:
            return "F"
        if west_:
            return "-"
        
    return "S"

def find_loc_from_start(grid, start_location):

    if start_location[0] != 0 and grid[start_location[0]-1][start_location[1]] in north:
        return [start_location[0]-1, start_location[1]]

    if start_location[0] != len(grid)-1 and grid[start_location[0]+1][start_location[1]] in south:
        return [start_location[0]+1, start_location[1]]

    if start_location[1] != 0 and grid[start_location[0]][start_location[1]-1] in west:
        return [start_location[0], start_location[1]-1]

    if start_location[1] != len(grid[0])-1 and grid[start_location[0]][start_location[1]+1] in east:
        return [start_location[0], start_location[1]+1]

    return start_location

def next_location(grid, current_location, last_location):

    if current_location[0] != 0 and current_location[0]-1 != last_location[0] and grid[current_location[0]-1][current_location[1]] in north and grid[current_location[0]][current_location[1]] in south:
        return [current_location[0]-1,current_location[1]], current_location

    if current_location[0] != len(grid)-1 and current_location[0]+1 != last_location[0] and grid[current_location[0]+1][current_location[1]] in south and grid[current_location[0]][current_location[1]] in north:
        return [current_location[0]+1,current_location[1]], current_location

    if current_location[1] != 0 and current_location[1]-1 != last_location[1] and grid[current_location[0]][current_location[1]-1] in west and grid[current_location[0]][current_location[1]] in east:
        return [current_location[0],current_location[1]-1], current_location

    if current_location[0] != len(grid[0])-1 and current_location[1]+1 != last_location[1] and grid[current_location[0]][current_location[1]+1] in east and grid[current_location[0]][current_location[1]] in west:
        return [current_location[0],current_location[1]+1], current_location

    return [0,0], current_location

def same_line(last_char, char):
    if char == "7" and last_char == "L":
        return True
    if char == "J" and last_char == "F":
        return True
    
    return False

f = open("p10input.txt", "r").read().strip()

grid = f.split("\n")

start_location = [0,0]
current_location = [0,0]
last_location = [0,0]

for i,row in enumerate(grid):
    if "S" in row:
        start_location = [i, row.index("S")]
        break

last_location = start_location
counter = 1
current_location = find_loc_from_start(grid, start_location)
# pipe_locations = [start_location]*15000
# print(pipe_locations)

temp_grid = [[x for x in string] for string in grid]
temp_grid[start_location[0]][start_location[1]] = " "

while grid[current_location[0]][current_location[1]] != "S":

    # pipe_locations.append(current_location)
    # pipe_locations[counter] = current_location
    temp_grid[current_location[0]][current_location[1]] = " "
    current_location, last_location = next_location(grid, current_location, last_location)
    counter += 1

print(counter/2)

counter = 0

# temp_grid = [[x for x in string] for string in grid]
# for i,x in enumerate(temp_grid):
#     for j,y in enumerate(x):
#         if [i,j] not in pipe_locations:
#             temp_grid[i][j] = " "

for i,x in enumerate(temp_grid):
    for j,y in enumerate(x):
        if temp_grid[i][j] == " ":
            temp_grid[i][j] = grid[i][j]
        else:
            temp_grid[i][j] = " "

for i,row in enumerate(temp_grid):
    within_pipe = False
    last_char = ""
    
    for j,col in enumerate(row):
        
        if col == "S":
            col = find_start_char(grid, start_location)
        
        # if last_char == "" and col in "JL7F|" and [i,j] in pipe_locations:
        if last_char == "" and col in "JL7F|":
            last_char = col
            within_pipe = not within_pipe
            continue
            
        # if col in "JL7F|" and [i,j] in pipe_locations and not same_line(last_char, col):
        if col in "JL7F|" and not same_line(last_char, col):
            within_pipe = not within_pipe
            last_char = col
            
        # if within_pipe and [i,j] not in pipe_locations:
        if within_pipe and col == " ":
            # temp_grid[i][j] = "0"
            counter += 1

for x in temp_grid:
    print(*x)
print(counter)