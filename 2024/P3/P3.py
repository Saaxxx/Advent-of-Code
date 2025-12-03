import re
def pt1(inputTxt):
    rePattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    p = re.compile(rePattern)

    res = 0

    for match in p.finditer(txt):
        # print(len(match.groups()))
        # print(match.groups())
        # print(match.group(0))
        # print(match.group(1))
        # print(match.group(2))
    
        res += int(match.group(1)) * int(match.group(2))
        
    return res

def pt2(inputTxt):
    add = True
    rePattern = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"
    p = re.compile(rePattern)
    
    res = 0
    
    for match in p.finditer(inputTxt):
        for group in match.groups():
            if group == None:
                continue
            print(group)
            
            if group.startswith("mul"):
                print(match.group(2), match.group(3))
                res += int(match.group(2)) * int(match.group(3)) * add
                
            elif group == "do()":
                add = True
                
            elif group == "don't()":
                add = False
    return res
    

# f = open("testinput.txt", "r")
f = open("input.txt", "r")
txt = f.read()

# res = pt1(txt)
res = pt2(txt)

print(res)

