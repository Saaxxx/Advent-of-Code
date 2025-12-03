def invalidAdjacent(int1, int2, increasing):
    diff = abs(int1 - int2)
    # print(int1 == int2, diff > 3, (int1 > int2 and increasing), (int1 < int2 and not increasing))
    return int1 == int2 or diff > 3 or (int1 > int2 and increasing) or (int1 < int2 and not increasing)

def validAdjacent(int1, int2, increasing):
    diff = abs(int1 - int2)
    return diff != 0 and diff <= 3 and ((int1 < int2 and increasing) or (int1 > int2 and not increasing))

f = open("input.txt", "r")
# f = open("testinput.txt", "r")

lines = f.read().split("\n")

# pt1
# res = 0
# for lineNum, line in enumerate(lines):
#     arr = line.split(" ")
    
#     increasing = False
#     if (int(arr[0]) < int(arr[1])):
#         increasing = True
    
#     for i in range(1, len(arr)):
#         int1 = int(arr[i-1])
#         int2 = int(arr[i])
#         diff = abs(int1 - int2)
        
#         # print(int1 == int2, (int1 > int2 and increasing), (int1 < int2 and not increasing), diff > 3)
#         # if (int1 == int2 or diff > 3 or (int1 > int2 and increasing) or (int1 < int2 and not increasing)):
#         if (invalidAdjacent(int1, int2, increasing)):
#             print(int1, int2, increasing, i)
#             break
#     else:
#         res += 1
#         # print(lineNum)
        
# print(res)

# pt2
res = 0
for lineNum, line in enumerate(lines):
    arr = line.split(" ")
    
    increasing = int(arr[0]) < int(arr[1])
    
    levelRemoved = False
    continueNext = False
    for i in range(1, len(arr)):
        if (continueNext):
            continueNext = False
            continue
        int1 = int(arr[i-1])
        int2 = int(arr[i])
        diff = abs(int1 - int2)
        
        # print(int1 == int2, (int1 > int2 and increasing), (int1 < int2 and not increasing), diff > 3)
        if (not validAdjacent(int1, int2, increasing)):
            if (not levelRemoved):
                levelRemoved = True
                continueNext = True
                
                # more checking
                if (i == len(arr)-1):
                    continue
                
                if (i == 1 or i == 2):
                    if i == 2:
                        continueNext = False
                        
                    if (validAdjacent(int(arr[0]), int(arr[2]), int(arr[2]) < int(arr[3]))):
                        increasing = int(arr[2]) < int(arr[3])
                        continue
                        
                    if (validAdjacent(int(arr[1]), int(arr[2]), int(arr[2]) < int(arr[3]))):
                        increasing = int(arr[2]) < int(arr[3])
                        continue
                    
                    # print(int1, int2, increasing, lineNum+1)
                    break
                
                # print(int(arr[i-2]), int2, increasing, "|", int1, int(arr[i+1]), increasing)
                # print(validAdjacent(int(arr[i-2]), int2, increasing), validAdjacent(int1, int(arr[i+1]), increasing))
                
                if (validAdjacent(int1, int(arr[i+1]), increasing)):
                    continue
                
                if (validAdjacent(int(arr[i-2]), int2, increasing)):
                    continueNext = False
                    continue
                    
            # print(int1, int2, increasing, lineNum+1)
            break
    else:
        res += 1
        print("Valid:", lineNum+1)
        
print(res)