from functools import reduce
from operator import mul

f = open("testinput.txt", "r")
f = open("input.txt", "r")

lines = f.read().split("\n")

totals = [int(x.split(": ")[0]) for x in lines]
values = [list(map(int, x.split(": ")[1].split(" "))) for x in lines]

# print(totals)
# print(values)

res = 0

for i in range(len(totals)):
    bfs = [values[i][0]]
    for j, value in enumerate(values[i][1:len(values[i])]):
        
        
        
        temp = []
        for x in bfs:
            # temp2 = [l for l in x]
            # temp2.append(value)
            temp.append(x+value)
            # x[-1] *= value
            temp.append(x*value)
            
                
            # pt2
            temp.append(int(str(x)+str(value)))
            
            
            
        # print(temp)
        bfs = [x for x in temp]
        
    # print(totals[i], bfs)
    
    for x in bfs:
        if x == totals[i]:
            res += totals[i]
            break
    
print(res)